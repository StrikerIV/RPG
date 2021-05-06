import time
import json
import utils
import numpy as np
from pathlib import Path

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