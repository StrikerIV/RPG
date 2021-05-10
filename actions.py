import time
import json
import utils
import random
import numpy as np
from pathlib import Path

def destroy():
    # get currently "equipped" block
    player = utils.Variables.playerPosition
    world = utils.Variables.world

    inventoryArray = []
    jsonInv = json.loads(json.dumps(utils.Variables.inventory))

    for key in jsonInv:
        inventoryArray.append("%s %s" % (str(jsonInv[key]), str(key)))

    equipped = inventoryArray[utils.Variables.currentlyUsing]
    amount = int(equipped.split(" ")[0].strip())
    block = equipped.split(" ")[1].strip()

    if(amount <= 0): return
    
    # set tile to block
    if(block == "stone"):
        world[player.x][player.y] = "H"
    elif(block == "dirt"):
        world[player.x][player.y] = "P"
    elif(block == "podzol"):
        world[player.x][player.y] = "T"        
    elif(block == "snow"):
        world[player.x][player.y] = "Y"    
    elif(block == "sand"):
        world[player.x][player.y] = "S"
    elif(block == "logs"): 
        world[player.x][player.y] = "I"       

    # then remove item from inventory that was placed
    utils.Variables.inventory[block] -= 1

def place():
    # use key
    # evaluate tile beneath the player to know what to do
    player = utils.Variables.playerPosition
    world = utils.Variables.world
    tileBelowPlayer = utils.eval_tile(world[player.x][player.y])

    if(tileBelowPlayer == "tree"):
        # use key on tree, we chop 
        # add logs to inventory then remove tree
        utils.Variables.inventory['logs'] += random.randint(3, 4)

        # then reset tile as tree is gone
        world[player.x][player.y] = "F"
        utils.Variables.world = world
        return False
    elif(tileBelowPlayer == "sand"):
        # on sand tile, dig & give to player
        utils.Variables.inventory['sand'] += 1

        world[player.x][player.y] = "U"
        utils.Variables.world = world
        return False
    elif(tileBelowPlayer == "dirt"):
        # on sand tile, dig & give to player
        utils.Variables.inventory['dirt'] += 1

        world[player.x][player.y] = "U"
        utils.Variables.world = world
        return False
    elif(tileBelowPlayer == "podzol"):
        # on sand tile, dig & give to player
        utils.Variables.inventory['podzol'] += 1

        world[player.x][player.y] = "U"
        utils.Variables.world = world
        return False
    elif(tileBelowPlayer == "stone"):
        # on sand tile, dig & give to player
        utils.Variables.inventory['stone'] += 1

        world[player.x][player.y] = "U"
        utils.Variables.world = world
        return False
    elif(tileBelowPlayer == "snow"):
        # on sand tile, dig & give to player
        utils.Variables.inventory['snow'] += 1

        world[player.x][player.y] = "U"
        utils.Variables.world = world
        return False
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