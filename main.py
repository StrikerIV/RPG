import os
from random import randint
import sys
import time
import json
import utils
import actions
import numpy as np
import generate_foliage as gf
from convert import convert
from colored import fg, attr, bg
from pynput.keyboard import Listener
from create_noise_map import create_noise_map
from inspect import signature as s, isfunction as f


def main():
    utils.clear_screen()
    print("+-------------------+")
    print("|     Welcome.      |")
    print("+-------------------+")
    print("| 1. Start Game     |")
    print("| 2. Load Game      |")
    print("| 3. Help           |")
    print("| 4. Credits        |")
    print("| 5. Other projects |")
    print("+-------------------+\n")

    choice = input()

    try:
        choice = int(choice)
    except ValueError:
        print("Please supply a valid choice.")

        time.sleep(2)
        utils.clear_screen()
        return main()

    if(choice == 1):
        start_game()
    elif(choice == 2):
        load_game()
    elif(choice == 3):
        print("\nget gud")
    elif(choice == 4):
        print("\n+------------------------------+")
        print("|           Credits            |")
        print("|      Made by StrikerIV       |")
        print("| https://github.com/StrikerIV |")
        print("+------------------------------+")
    elif(choice == 5):
        print("\n+--------------------------------+")
        print("| See my other projects on Github! |")
        print("|   https://github.com/StrikerIV   |")
        print("+----------------------------------+")

    time.sleep(5)
    utils.clear_screen()
    return main()


def get_name():
    time.sleep(1)
    utils.clear_screen()
    time.sleep(1)
    name = str(input("Who shall you be named? "))

    if(os.path.isdir("saves/%s" % name)):
        # there is already a saved game with this name, we ask them to use a different name
        time.sleep(1)
        print("\nThere is already a saved game by this name. Please chose a\ndifferent name, or restart the game and load from a save.")
        time.sleep(5)
        utils.clear_screen()

    return name


def create_character():
    utils.clear_screen()
    print("Chose your culture by typing it. You can view information on a culture by choosing the appropriate number option.\n")
    print("+-------------+")
    print("| 1. Svec     |")
    print("| 2. Baeskens |")
    print("| 3. Thurber  |")
    print("| 4. Dueck    |")
    print("| 5. Obeng    |")
    print("| 6. Bostian  |")
    print("+-------------+\n")

    choice = input()
    attribute = ""
    octave2 = 0
    octave1 = 2

    try:
        choice = int(choice)
        # if no error, show description of culture and ask if they want to chose

        if(choice == 1):
            print("\nThe Svec\n\nRuthless Vikings descendants of adventurers from Norway. Known for their ruthless\nstyle of war, they prefer bloodshed over diplomacy for peace.\n\n+20% Strength\n")
            time.sleep(2.5)
            choice = utils.get_choice(
                "Do you want to chose this culture? (y,n) ")
            if(choice):
                octave2 += 1
                octave1 += 3
                attribute = utils.Attribute("Svec", "strength", 20)
            else:
                utils.clear_screen()
                return create_character()
        elif(choice == 2):
            print("\nThe Baesken\n\nPeaceful fisherman from the rivers of the Northwest. Prideful of their vast\ndelicacies, they strive to be better than everyone else at cooking.\n\n+20% Cooking\n")
            time.sleep(2.5)
            choice = utils.get_choice(
                "Do you want to chose this culture? (y,n) ")
            if(choice):
                octave2 += 2
                octave1 += 1
                attribute = utils.Attribute("Baeskens", "cooking", 20)
            else:
                utils.clear_screen()
                return create_character()
        elif(choice == 3):
            print("\nThe Thurber\n\nHardened blacksmiths from the mountains, they are strong and persevere.\nBe sure to know they won't back down without a fight, as they will always be ready.\n\n+20% Strength\n")
            time.sleep(2.5)
            choice = utils.get_choice(
                "Do you want to chose this culture? (y,n) ")
            if(choice):
                octave2 += 3
                octave1 += 1
                attribute = utils.Attribute("Thurber", "strength", 20)
            else:
                utils.clear_screen()
                return create_character()
        elif(choice == 4):
            print("\nThe Dueck\n\nFarmers from the hills of Italy, they are steadfast towards their religion.\nThey will fight to protect their faith, by any means, at any cost.\n\n+20% Charisma\n")
            time.sleep(2.5)
            choice = utils.get_choice(
                "Do you want to chose this culture? (y,n) ")
            if(choice):
                octave2 += 2
                octave1 += 2
                attribute = utils.Attribute("Dueck", "charisma", 20)
            else:
                utils.clear_screen()
                return create_character()
        elif(choice == 5):
            print("\nThe Obeng\n\nMasters of building, they come from the valleys of China. Skilled craftsman, they\nconstruct the most engineered buildings to date.\n\n+20% Intelligence\n")
            time.sleep(2.5)
            choice = utils.get_choice(
                "Do you want to chose this culture? (y,n) ")
            if(choice):
                octave2 += 1
                octave1 += 4
                attribute = utils.Attribute("Obeng", "intelligence", 20)
            else:
                utils.clear_screen()
                return create_character()
        elif(choice == 6):
            print("\nThe Boastian\n\nComing from the foothills of Spain, these folk love dancing and well, showing off.\nBut when the time is right, they'll be as strong as giants.\n\n+20% Tactics\n")
            time.sleep(2.5)
            choice = utils.get_choice(
                "Do you want to chose this culture? (y,n) ")
            if(choice):
                octave2 += 5
                octave1 += 3
                attribute = utils.Attribute("Boastian", "tactics", 20)
            else:
                utils.clear_screen()
                return create_character()
        else:
            print("\nPlease supply a valid choice.")
            time.sleep(3)
            utils.clear_screen()
            return create_character()

        return ((octave1, octave2), attribute)
    except ValueError:
        print("\nPlease supply a valid choice.")
        time.sleep(2)
        utils.clear_screen()
        return create_character()

    # culture has been chosen, now we ask for character name used in save file


def begin_game(data):
    # to begin, we create the map based on octaves and frequency
    utils.clear_screen()
    print("Welcome to Elderflame, %s." % utils.Variables.playerName)
    time.sleep(2)
    print("Give us a moment to set up your world.\n")
    create_noise_map(data[0])
    print("Noise map generated. Starting conversion.")
    world = convert()
    utils.Variables.world = world
    utils.Variables.ogWorld = world
    message = "Converted. Starting game."
    print(message)
    utils.ongoing(message, 3)
    gf.generate_foliage(world)
    player = utils.spawn_player(world)
    game_terminal(world, player)
    time.sleep(3)


def start_game():
    time.sleep(2)
    utils.clear_screen()
    print("Welcome to Elderflame.\n")
    time.sleep(3)
    print("I'm the narrator; you won't hear much from me but from this little conversation.")
    time.sleep(3)
    message = "Before we get started, you need to create a character. Let's do that now."
    print(message)
    utils.ongoing(message, 3)
    time.sleep(2)
    data = create_character()
    print("\nThe path of the %s is always a good choice.\n" % data[1].culture)
    time.sleep(2)
    name = get_name()
    utils.Variables.playerName = name
    time.sleep(2)
    utils.clear_screen()
    time.sleep(1)
    begin_game(data)


def load_game():
    saves = os.listdir("saves/")

    utils.clear_screen()
    if(not saves):
        # there are no saves, so we go back to main screen
        print("There are currently no saved games.")
    else:
        print("Load a save by name - \n")

        for index, save in enumerate(saves):
            print("    %s. %s" % (index + 1, save))

        saveChoice = str(input("\n\n"))

        if(not saveChoice in saves):
            # specified save is not a valid save, go back to load game
            return load_game()
        else:
            # now we load the variables from the save and head to the game terminal
            path = 'saves/%s' % saveChoice

            utils.Variables.world = np.genfromtxt("%s/world.txt" % path, delimiter=" ", dtype=str)
            
            with open("%s/variables.json" % path) as variablesFile:
                variables = json.loads(variablesFile.read())
                pPosTuple = tuple(map(int, variables["playerPosition"].split(", ")))

                utils.Variables.playerPosition = utils.Player((pPosTuple[0], pPosTuple[1]))
                utils.Variables.currentlyTyping = variables['currentlyTyping']
                utils.Variables.playerName = saveChoice
                utils.Variables.inventory = variables['inventory']


                time.sleep(2)
                game_terminal(utils.Variables.world, utils.Variables.playerPosition)

i = 0
currentlyTyping = False

def on_press(key):
    # this is the input function of the program
    # we give them the "pointer" and concat what they are typing onto it
    pointer = ("%s>%s" % (fg('white'), attr('reset')))
    world = utils.Variables.world

    global currentlyTyping

    try:
        key = "{0}".format(key.char)
        if(key == "T" or key =="t" or currentlyTyping):
            if(currentlyTyping):
                # after pressing chat key it starts adding characters
                utils.Variables.currentlyTyping += key
            currentlyTyping = True
            print("\033[A                             \033[A")
            print(pointer + " {0}".format(utils.Variables.currentlyTyping))
        elif(key == "Q" or key == "q"):
            action = actions.destroy()
            return False
        elif(key == "E" or key == "e"):
            action = actions.place()
            return False
        elif(key == "W" or key == "w"):
            command = ["move", "forward"]
            actions.move(command, world)
            return False
        elif(key == "S" or key == "s"):
            command = ["move", "down"]
            actions.move(command, world)
            return False
        elif(key == "A" or key == "a"):
            command = ["move", "left"]
            actions.move(command, world)
            return False
        elif(key == "D" or key == "d"):
            command = ["move", "right"]
            actions.move(command, world)
            return False

    except AttributeError:
        # key pressed was nonalphanumeric, check for movement.
        key = "{0}".format(key)
        if(key == "Key.ctrl_l" or key == "key.ctrl_r"):
            # control key, exit program
            sys.exit()
        if(key == "Key.enter"):
            # execute whatever command is in terminal currently
            currentlyTyping = False
            command = utils.Variables.currentlyTyping.split(" ")
            utils.Variables.currentlyTyping = ""
            if(command[0] == "move"):
                # inputted command is move
                # it default updates the player in the variables so no reassign needed.
                worked = actions.move(command, world)
                if(not worked):
                    print("\nEror executing command %s." % command[0])
                    time.sleep(3)
                    print("\033[A                             \033[A")
                    print("\033[A                             \033[A")
                    return True
                else:
                    return False
            elif(command[0] == "chop"):
                worked = actions.chop(world)
                if(not worked):
                    print("\nEror executing command %s." % command[0])
                    time.sleep(3)
                    print("\033[A                             \033[A")
                    print("\033[A                             \033[A")
                    return True
                else:
                    return False     
            elif(command[0] == "save"):
                worked = actions.save(world)
                if(not worked):
                    print("\nEror executing command %s." % command[0])
                    time.sleep(3)
                    print("\033[A                             \033[A")
                    print("\033[A                             \033[A")
                    return True
                else:
                    return False          
            elif(command[0] == "exit" or command[0] == "quit"):
                actions.save(world)  
                os._exit(1)
        elif(key == "Key.space"):
            utils.Variables.currentlyTyping += ' '
        elif(key == "Key.backspace"):
            utils.Variables.currentlyTyping = utils.Variables.currentlyTyping[:-1]
            print("\033[A                             \033[A")
            print(pointer + " {0}".format(utils.Variables.currentlyTyping))
        elif(key == "Key.up"):
            if(utils.Variables.currentlyUsing == 0): return
            utils.Variables.currentlyUsing -= 1
            return False
        elif(key == "Key.down"):
            if(utils.Variables.currentlyUsing == 5): return
            utils.Variables.currentlyUsing += 1
            return False


def on_release(key):
    pass


def game_terminal(world, player):
    # the terminal will be constantly refreshed if anything is done in the game, therefor we
    # put it in a while loop. firstly define the "pointer" then we print all we need to the console before the terminal
    utils.Variables.playerPosition = player

    while True:
        utils.clear_screen()  # clear screen cause we don't want uglyness
        player = utils.Variables.playerPosition
        world = utils.Variables.world
        utils.get_terrain_around_player(True, world, player)  # print terrain
        print("\n\n\n\n%s>%s" % (fg('white'), attr('reset')))  # move down a few lines for the console input

        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()



main()
