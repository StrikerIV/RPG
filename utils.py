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

def insertChar(string, position, chartoinsert):
    lenS = len(string)
    string = string[:position] + chartoinsert + string[position:]
    return string

def get_terrain_around_player(world, player):

    pX = player.x
    pY = player.y

    print("here", (pX, pY))
    rangeAP = 5
    countLength = (rangeAP * 2) + 1
    aroundPA = np.tile("X", (countLength, countLength))

    # now we loop and get the tiles within a 5 x 5 of the player (turns into 11 x 11 because of center block)
    # we need to start in the upper left corner, and loop downwards

    startPosIW = (pX - rangeAP, pY - rangeAP)
    xCount = -1
    yCount = -1

    for x in range(startPosIW[0], startPosIW[0] + countLength):
        xCount += 1
        for y in range(startPosIW[0], startPosIW[0] + countLength):
            # every time "y" loops it needs to go down a row, because that is the bounding box
            # x and y values correspond to the world coordnents,
            # xCount and yCound values correspond to aroundPA coords

            yCount += 1

            if(x < 0 or y < 0):
                # out of bounds for world
                aroundPA[xCount][yCount] = "X"
            else:
                aroundPA[xCount][yCount] = world[x][y]

            if(yCount + 1 == 11):
                # reset counter for next row because the current row is finished
                yCount = -1

    # now we have the view of the player, convert to multiline string and change colors of tiles, add the player in, and return
    # the red dot represents the player
    aroundPS = aroundPA.tostring()
    aroundPS = aroundPS.decode("utf-8")
    aroundPA[rangeAP][rangeAP] = "U"

    print(format_terrain_lines(aroundPA[0].tostring().decode("utf-8")))
    print("")
    print(format_terrain_lines(aroundPA[1].tostring().decode("utf-8")))
    print("")
    print(format_terrain_lines(aroundPA[2].tostring().decode("utf-8")))
    print("")
    print(format_terrain_lines(aroundPA[3].tostring().decode("utf-8")))
    print("")
    print(format_terrain_lines(aroundPA[4].tostring().decode("utf-8")))
    print("")
    print(format_terrain_lines(aroundPA[5].tostring().decode("utf-8")))
    print("")
    print(format_terrain_lines(aroundPA[6].tostring().decode("utf-8")))
    print("")
    print(format_terrain_lines(aroundPA[7].tostring().decode("utf-8")))
    print("")
    print(format_terrain_lines(aroundPA[8].tostring().decode("utf-8")))
    print("")
    print(format_terrain_lines(aroundPA[9].tostring().decode("utf-8")))
    print("")
    print(format_terrain_lines(aroundPA[10].tostring().decode("utf-8")))
    print("")
    
    return aroundPA

def format_terrain_lines(terrain):
    # given a "line" or "string" as terrain, we need to format it appropriately
    # we have a bunch of sub methods for each of the terrain elements

    try:
        terrain = re.sub("(X)", "%s%sX ⠀%s " % (fg('red'), bg('red'), attr('reset')), terrain)
        terrain = re.sub("(W)", "%s%sW ⠀%s " % (fg('blue'), bg('blue'), attr('reset')), terrain)
        terrain = re.sub("(S)", "%s%sS ⠀%s " % (fg('yellow_2'), bg('yellow_2'), attr('reset')), terrain)
        terrain = re.sub("(Q)", "%s%sQ ⠀%s " % (fg('dark_green'), bg('dark_green'), attr('reset')), terrain)
        terrain = re.sub("(P)", "%s%sP ⠀%s " % (fg('light_green'), bg('light_green'), attr('reset')), terrain)
        terrain = re.sub("(F)", "%s%sF ⠀%s " % (fg('green_3b'), bg('green_3b'), attr('reset')), terrain)
        terrain = re.sub("(T)", "%s%sT ⠀%s " % (fg('orange_4b'), bg('orange_4b'), attr('reset')), terrain)
        terrain = re.sub("(H)", "%s%sH ⠀%s " % (fg('green_3b'), bg('green_3b'), attr('reset')), terrain)
        terrain = re.sub("(Y)", "%s%sY ⠀%s " % (fg('grey_82'), bg('grey_82'), attr('reset')), terrain)
        terrain = re.sub("(M)", "%s%sM ⠀%s " % (fg('grey_50'), bg('grey_50'), attr('reset')), terrain)
        terrain = re.sub("(A)", "%s%sA ⠀%s " % (fg('grey_93'), bg('grey_93'), attr('reset')), terrain)

        #then change color for player
        terrain = re.sub("(U)", "%s%sU ⠀%s " % (fg('red'), bg('red'), attr('reset')), terrain)

        return terrain
    except re.error:
        return terrain

def spawn_player(world):
    randomPosX = random.randrange(0, len(world[0]))
    randomPosY = random.randrange(0, len(world))

    print(randomPosX, randomPosY)
    tileInWorld = world[randomPosX][randomPosY]
    print(tileInWorld)
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
