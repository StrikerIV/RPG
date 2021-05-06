from colored import fg, bg, attr
from os import system, name
import json
import numpy as np
import random
import time
import re


class Player:
    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]


class Attribute:
    def __init__(self, culture, attribute, percent):
        self.culture = culture
        self.attribute = attribute
        self.percent = percent

class Variables:
    playerPosition = Player((0, 0))
    currentlyTyping = ""
    playerName = ""
    inventory = {
        "logs": 0
    }
    ogWorld = []
    world = []

def render_tree(view, position):
    # render a tree at given position in player world
    # base of the tree starts at supplied position
    try:
        view[position[0]][position[1]] = "C"

        #move one up for next log
        view[position[0] - 1][position[1]] = "C"

        #move up, left, right, then up again for leaves
        view[position[0] - 2][position[1]] = "&"
        view[position[0] - 2][position[1] - 1] = "&"
        view[position[0] - 2][position[1] + 1] = "&"
        view[position[0] - 3][position[1]] = "&"

    except IndexError:
        # render of tree is outside view of player, just return
        # this is why we start from the bottom to make sure the
        # tree is rendered properly and not cut off
        return


def get_terrain_around_player(send, world, player):

    pX = player.x
    pY = player.y

    viewAroundPlayer = 10
    aroundPlayerGridHeight = (viewAroundPlayer * 2) + 1
    aroundPlayerGridWidth = (viewAroundPlayer * 2) + 1
    aroundPlayerArray = np.tile("X", (aroundPlayerGridHeight, aroundPlayerGridWidth))
    
    startPositionInWorld = (pX - viewAroundPlayer, pY - viewAroundPlayer)
    for xPos, rowOfTiles in enumerate(aroundPlayerArray):
        for yPos, _ in enumerate(rowOfTiles):
            # check to see if indexe are out of bounds
            if((startPositionInWorld[0] + xPos) < 0 or (startPositionInWorld[1] + yPos) < 0):
                # out of bounds
                aroundPlayerArray[xPos][yPos] = "X"
            else:
                #print(startPositionInWorld[0] + xPos, startPositionInWorld[1] + yPos)
                try:
                    aroundPlayerArray[xPos][yPos] = world[startPositionInWorld[0] + xPos][startPositionInWorld[1] + yPos]
                except IndexError:
                    # we have an index error, which occurs if the player view is attempting to enter the right and bottom boundaries
                    # we make it out of bounds as there are no tiles there
                    aroundPlayerArray[xPos][yPos] = "X"

    aroundPlayerString = aroundPlayerArray.tostring()
    aroundPlayerString = aroundPlayerString.decode("utf-8")

    if(send):
        # sending to terminal
        # we firstly need to render tree logs and leaves cause that is important
        # leaves and logs are not strictly saved, only the base tree position is
        treePositions = np.where(aroundPlayerArray == "%")
        for yPos in treePositions[0]:
            # indexes of arrays with trees
            xPos = np.where(aroundPlayerArray[yPos] == "%")[0]

            for treeXPos in xPos:
                render_tree(aroundPlayerArray, (yPos, treeXPos))

        for index, row in enumerate(aroundPlayerArray):
            print(format_terrain_lines(index, world, row.tostring().decode("utf-8"), viewAroundPlayer))

        return aroundPlayerArray
    else:
        # returning for foliage most likely
        return aroundPlayerArray

def format_terrain_lines(index, world, terrain, viewLen):
    # given a "line" or "string" as terrain, we need to format it appropriately
    # we have a bunch of sub methods for each of the terrain elements
    player = Variables.playerPosition
    try:
        # biomes
        terrain = re.sub("(X)", "%s%sX ⠀%s" % (fg('red'), bg('red'), attr('reset')), terrain)
        terrain = re.sub("(W)", "%s%sW ⠀%s" % (fg('blue'), bg('blue'), attr('reset')), terrain)
        terrain = re.sub("(S)", "%s%sS ⠀%s" % (fg('yellow_2'), bg('yellow_2'), attr('reset')), terrain)
        terrain = re.sub("(Q)", "%s%sQ ⠀%s" % (fg('orange_4a'), bg('orange_4a'), attr('reset')), terrain)
        terrain = re.sub("(P)", "%s%sP ⠀%s" % (fg('light_green'), bg('light_green'), attr('reset')), terrain)
        terrain = re.sub("(F)", "%s%sF ⠀%s" % (fg('chartreuse_4'), bg('chartreuse_4'), attr('reset')), terrain)
        terrain = re.sub("(T)", "%s%sT ⠀%s" % (fg('orange_4b'), bg('orange_4b'), attr('reset')), terrain)
        terrain = re.sub("(H)", "%s%sH ⠀%s" % (fg('green_3b'), bg('green_3b'), attr('reset')), terrain)
        terrain = re.sub("(Y)", "%s%sY ⠀%s" % (fg('grey_82'), bg('grey_82'), attr('reset')), terrain)
        terrain = re.sub("(M)", "%s%sM ⠀%s" % (fg('grey_50'), bg('grey_50'), attr('reset')), terrain)
        terrain = re.sub("(A)", "%s%sA ⠀%s" % (fg('grey_93'), bg('grey_93'), attr('reset')), terrain)

        # render tree stuff
        terrain = re.sub("(C)", "%s%s^ ⠀%s" % (fg('dark_orange_3a'), bg('dark_orange_3a'), attr('reset')), terrain)
        terrain = re.sub("(&)", "%s%s& ⠀%s" % (fg('dark_green'), bg('dark_green'), attr('reset')), terrain)  
        
        # then change color for player in the center of the view
        # we know that the player must be in the middle, so we use the viewLen to place them
        # however, the terrain is strings so we must use the supplied index to determine where we are
        terrain = terrain.split()

        if((index + 1) % viewLen == 0 and not index == ((viewLen)* 2 - 1)):
            # "torso" of player
            # loop through characters until we get to the viewLen'th character
            terrain[viewLen] = '⠀\x1b[0m\x00\x00\x00\x1b[38;5;33m\x1b[48;5;33m#'
        elif ((index) % viewLen == 0 and not index == 0 and not index == viewLen * 2):
            terrain[viewLen] = '⠀\x1b[0m\x00\x00\x00\x1b[38;5;3m\x1b[48;5;3m#'
            #print([terrain])
        # then add on corrds and biome stuff
        terrain = ''.join(terrain)

        inventoryArray = []
        jsonInv = json.loads(json.dumps(Variables.inventory))

        if(index == 4):
            # tell biome
            terrain = terrain + "          Biome : %s" % (eval_tile(world[player.x][player.y]))
        elif(index == 5):
            # tell coords
            terrain = terrain + "          X, Z : %s, %s" % (player.x, player.y)
        elif(index == 7):
            # start of inventory
            terrain = terrain + "          Inventory : "
        elif(index >= 8 and index <= 15):
            try:      
                for key in jsonInv:
                    inventoryArray.append("%s %s" % (str(jsonInv[key]), str(key)))

                terrain = terrain + "              %s" % inventoryArray[index - 8]
            except:
                pass
        else:
            terrain = terrain

        return terrain
    except re.error:
        return terrain

def eval_tile(tile):

    # eval biomes
    if(tile == "X"):
        # out of bounds
        return "OOB"
    elif(tile == "W"):
        # water tile
        return "ocean"
    elif(tile == "S"):
        # sand tile
        return "beach"
    elif(tile == "P"):
        # plains tile
        return "plains"
    elif(tile == "Q"):
        # swamp tile
        return "swamp"
    elif(tile == "F"):
        # forest tile
        return "forest"
    elif(tile == "T"):
        # taiga tile
        return "taiga"
    elif(tile == "H"):
        # hills tile
        return "hills"
    elif(tile == "Y"):
        # snowy plains tile
        return "snowy_plains"
    elif(tile == "M"):
        # mountains tile
        return "mountains"
    elif(tile == "A"):
        # snowy mountains tile
        return "snowy_mountains"

    # eval other tiles
    if(tile == "%"):
        return "tree"

def spawn_player(world):
    randomPosX = random.randrange(0, len(world[0]))
    randomPosY = random.randrange(0, len(world))

    tileInWorld = world[randomPosX][randomPosY]
    if(tileInWorld == "W"):
        # player has spawn in water, redo to get on land
        return spawn_player(world)

    player = Player((randomPosX, randomPosY))
    return(player)


def get_choice(message):
    choice = input(message)
    if(choice == "y" or choice == "yes"):
        return True
    elif(choice == "n" or choice == "no"):
        return False

def clear_above(lines):
    for _ in range(0, lines):
        print("\033[A                             \033[A")

def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def ongoing(message, rate):
    for x in range(0, rate):
        print("\033[A                             \033[A")
        print(message + '.'*x)
        time.sleep(1)
