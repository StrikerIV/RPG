import time
import json
import utils
import numpy as np
from pathlib import Path

def chop(world):
    # chop down tree
    player = utils.Variables.playerPosition

    pX = player.x
    pY = player.y

    # use the same method to get a 1x1 around player
    viewAroundPlayer = 1
    aroundPlayerGridHeight = (viewAroundPlayer * 2) + 1
    aroundPlayerGridWidth = (viewAroundPlayer * 2) + 1
    aroundPlayerArray = np.tile("X", (aroundPlayerGridHeight, aroundPlayerGridWidth))
    
    startPositionInWorld = (pX - viewAroundPlayer, pY - viewAroundPlayer)
    for xPos, rowOfTiles in enumerate(aroundPlayerArray):
        for yPos, _ in enumerate(rowOfTiles):
            if((startPositionInWorld[0] + xPos) < 0 or (startPositionInWorld[1] + yPos) < 0):
                aroundPlayerArray[xPos][yPos] = "X"
            else:
                try:
                    aroundPlayerArray[xPos][yPos] = world[startPositionInWorld[0] + xPos][startPositionInWorld[1] + yPos]
                except IndexError:
                    aroundPlayerArray[xPos][yPos] = "X"

    # check to see if tree in "view"
    if(not np.where(aroundPlayerArray == "%")[0][0]):
        # no tree in range of player, return
        return

    # remove tree from world, then add 3 logs to their inventory
    inventory = json.loads(utils.Variables.inventory)
    inventory['logCount'] += 3

    
    return True

def move(args, world):
    # this is the function that actually moves the character around
    # it's quite simple, depending on where they move we edit the x / y values 
    # negative or positive. to move forward, increase "x" by one, ect
    
    # we know args[0] is the command, so we initially start with [1]
    player = utils.Variables.playerPosition

    playerX = player.x
    playerY = player.y

    if(args[1] == ""):
        # nothing was supplied
        return False
    elif(args[1] == "forward" or args[1] == "up"):
        # input was to move "up" / "forward"
        if(playerX - 1 < 0):
            # out of bounds
            return True
        updatedPlayer = utils.Player((playerX - 1, playerY))
        utils.Variables.playerPosition = updatedPlayer
        #print(utils.Variables.playerPosition.x, utils.Variables.playerPosition.x)
        return True
    elif(args[1] == "back" or args[1] == "down"):
        # input was to move "back" / "down"
        if(playerX + 1 == 500):
            # out of bounds
            return True
        updatedPlayer = utils.Player((playerX + 1, playerY))
        utils.Variables.playerPosition = updatedPlayer
        return True
    elif(args[1] == "left"):
        # input was to move "left"
        if(playerY - 1 < 0):
            # out of bounds
            return True
        updatedPlayer = utils.Player((playerX, playerY - 1))
        utils.Variables.playerPosition = updatedPlayer
        return True
    elif(args[1] == "right"):
        # input was to move "right"
        print(playerY)
        if(playerY + 1 == 500):
            # out of bounds
            return True
        updatedPlayer = utils.Player((playerX, playerY + 1))
        utils.Variables.playerPosition = updatedPlayer
        return True

def save(world):
    # save the game
    playerName = utils.Variables.playerName

    # create path
    p = Path('saves/%s' % playerName)
    p.mkdir(exist_ok=True)

    path = 'saves/%s' % playerName

    # save world first
    np.savetxt("%s/world.txt" % path, world, fmt='%s', delimiter=' ', newline='\n')

    # save variables
    with open('%s/variables.json' % path, 'w') as variablesFile:

        pPos = utils.Variables.playerPosition
        playerPosition = "%s, %s" %(pPos.x, pPos.y)
        currentlyTyping = utils.Variables.currentlyTyping
        inventory = utils.Variables.inventory

        data = {
            'playerPosition': playerPosition, 
            "currentlyTyping": currentlyTyping, 
            "inventory": inventory
        }

        variablesFile.write(json.dumps(data))
    
    return True