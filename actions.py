import utils

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
        updatedPlayer = utils.Player((playerX - 1, playerY))
        utils.Variables.playerPosition = updatedPlayer
        #print(utils.Variables.playerPosition.x, utils.Variables.playerPosition.x)
        return True
    elif(args[1] == "back" or args[1] == "down"):
        # input was to move "back" / "down"
        updatedPlayer = utils.Player((playerX + 1, playerY))
        utils.Variables.playerPosition = updatedPlayer
        return True
    elif(args[1] == "left"):
        # input was to move "left"
        updatedPlayer = utils.Player((playerX, playerY - 1))
        utils.Variables.playerPosition = updatedPlayer
        return True
    elif(args[1] == "right"):
        # input was to move "right"
        updatedPlayer = utils.Player((playerX, playerY + 1))
        utils.Variables.playerPosition = updatedPlayer
        return True

def chop(world):
    # chop down tree
    player = utils.Variables.playerPosition

    tile = utils.eval_tile(world[player.x][player.y])
    if(tile == "tree"):
        # this is a tree therefor we can chop
        print('tree')

    return True