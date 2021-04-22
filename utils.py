from colored import fg, bg, attr
from os import system, name
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
    world = []

def get_terrain_around_player(world, player):

    pX = player.x
    pY = player.y

    viewAroundPlayer = 7
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
                    # basically we use a counter now to determine how far to go
                    aroundPlayerArray[xPos][yPos] = "X"

    aroundPlayerString = aroundPlayerArray.tostring()
    aroundPlayerString = aroundPlayerString.decode("utf-8")
    aroundPlayerArray[viewAroundPlayer][viewAroundPlayer] = "#"

    for index, row in enumerate(aroundPlayerArray):
        print(format_terrain_lines(index, world, row.tostring().decode("utf-8")))
    
    return aroundPlayerArray

def format_terrain_lines(index, world, terrain):
    # given a "line" or "string" as terrain, we need to format it appropriately
    # we have a bunch of sub methods for each of the terrain elements
    player = Variables.playerPosition
    try:
        terrain = re.sub("(X)", "%s%sX ⠀%s " % (fg('red'), bg('red'), attr('reset')), terrain)
        terrain = re.sub("(W)", "%s%sW ⠀%s " % (fg('blue'), bg('blue'), attr('reset')), terrain)
        terrain = re.sub("(S)", "%s%sS ⠀%s " % (fg('yellow_2'), bg('yellow_2'), attr('reset')), terrain)
        terrain = re.sub("(Q)", "%s%sQ ⠀%s " % (fg('dark_green'), bg('dark_green'), attr('reset')), terrain)
        terrain = re.sub("(P)", "%s%sP ⠀%s " % (fg('light_green'), bg('light_green'), attr('reset')), terrain)
        terrain = re.sub("(F)", "%s%sF ⠀%s " % (fg('chartreuse_4'), bg('chartreuse_4'), attr('reset')), terrain)
        terrain = re.sub("(T)", "%s%sT ⠀%s " % (fg('orange_4b'), bg('orange_4b'), attr('reset')), terrain)
        terrain = re.sub("(H)", "%s%sH ⠀%s " % (fg('green_3b'), bg('green_3b'), attr('reset')), terrain)
        terrain = re.sub("(Y)", "%s%sY ⠀%s " % (fg('grey_82'), bg('grey_82'), attr('reset')), terrain)
        terrain = re.sub("(M)", "%s%sM ⠀%s " % (fg('grey_50'), bg('grey_50'), attr('reset')), terrain)
        terrain = re.sub("(A)", "%s%sA ⠀%s " % (fg('grey_93'), bg('grey_93'), attr('reset')), terrain)

        #then change color for player
        terrain = re.sub("(#)", "%s%s# ⠀%s " % (fg('red'), bg('red'), attr('reset')), terrain)
        
        #then add new line afterward
        if(index == 4):
            terrain = terrain + "          Biome : %s\n" % (eval_tile(world[player.x][player.y]))
        else:
            terrain = terrain + "\n"

        return terrain
    except re.error:
        return terrain

def eval_tile(tile):
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

def spawn_player(world):
    randomPosX = random.randrange(0, len(world[0]))
    randomPosY = random.randrange(0, len(world))

    tileInWorld = world[randomPosX][randomPosY]
    if(tileInWorld == "."):
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
