import time
import utils
import actions
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
    print("| 2. Help           |")
    print("| 3. Credits        |")
    print("| 4. Other projects |")
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
        print("\nget gud")
    elif(choice == 3):
        print("\n+------------------------------+")
        print("|           Credits            |")
        print("|      Made by StrikerIV       |")
        print("| https://github.com/StrikerIV |")
        print("+------------------------------+")

    time.sleep(5)
    utils.clear_screen()
    return main()


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
            time.sleep(5)
            choice = utils.get_choice(
                "Do you want to chose this culture? (y,n) ")
            if(choice):
                octave2 += 1
                octave1 += 2
                attribute = utils.Attribute("Svec", "strength", 20)
                return ((octave1, octave2), attribute)
            else:
                utils.clear_screen()
                create_character()
        elif(choice == 2):
            print("\nThe Baesken\n\nPeaceful fisherman from the rivers of the Northwest. Prideful of their vast\ndelicacies, they strive to be better than everyone else at cooking.\n\n+20% Cooking\n")
            time.sleep(5)
            choice = utils.get_choice(
                "Do you want to chose this culture? (y,n) ")
            if(choice):
                octave2 += 2
                octave1 += 3
                attribute = utils.Attribute("Baeskens", "cooking", 20)
                return ((octave1, octave2), attribute)
            else:
                utils.clear_screen()
                create_character()
        elif(choice == 3):
            print("\nThe Thurber\n\nHardened blacksmiths from the mountains, they are strong and persevere.\nBe sure to know they won't back down without a fight, as they will always be ready.\n\n+20% Strength\n")
            time.sleep(5)
            choice = utils.get_choice(
                "Do you want to chose this culture? (y,n) ")
            if(choice):
                octave2 += 2
                octave1 += 3
                attribute = utils.Attribute("Thurber", "cooking", 20)
                return ((octave1, octave2), attribute)
            else:
                utils.clear_screen()
                create_character()
        elif(choice == 4):
            print("\nThe Dueck\n\nFarmers from the hills of Italy, they are steadfast towards their religion.\nThey will fight to protect their faith, by any means, at any cost.\n\n+20% Charisma\n")
            time.sleep(5)
            choice = utils.get_choice(
                "Do you want to chose this culture? (y,n) ")
            if(choice):
                octave2 += 2
                octave1 += 3
                attribute = utils.Attribute("Dueck", "cooking", 20)
                return ((octave1, octave2), attribute)
            else:
                utils.clear_screen()
                create_character()
        elif(choice == 5):
            print("\nThe Obeng\n\nMasters of building, they come from the valleys of China. Skilled craftsman, they\nconstruct the most engineered buildings to date.\n\n+20% Intelligence\n")
            time.sleep(5)
            choice = utils.get_choice(
                "Do you want to chose this culture? (y,n) ")
            if(choice):
                octave2 += 2
                octave1 += 3
                attribute = utils.Attribute("Obeng", "cooking", 20)
                return ((octave1, octave2), attribute)
            else:
                utils.clear_screen()
                create_character()
        elif(choice == 6):
            print("\nThe Boastian\n\nComing from the foothills of Spain, these folk love dancing and well, showing off.\nBut when the time is right, they'll be as strong as giants.\n\n+20% Tactics\n")
            time.sleep(5)
            choice = utils.get_choice(
                "Do you want to chose this culture? (y,n)")
            if(choice):
                octave2 += 2
                octave1 += 3
                attribute = utils.Attribute("Boastian", "cooking", 20)
                return ((octave1, octave2), attribute)
            else:
                utils.clear_screen()
                create_character()
        else:
            print("\nPlease supply a valid choice.")
            time.sleep(3)
            utils.clear_screen()
            return create_character()
    except ValueError:
        print("\nPlease supply a valid choice.")
        time.sleep(2)
        utils.clear_screen()
        return create_character()

    return ((octave1, octave2), attribute)


def begin_game(data):
    # to begin, we create the map based on octaves and frequency
    utils.clear_screen()
    print("Welcome.")
    time.sleep(2)
    print("Give us a moment to set up your world.\n")
    create_noise_map(data[0])
    print("Noise map generated. Starting conversion.")
    world = convert()
    message = "Converted. Starting game."
    print(message)
    utils.ongoing(message, 3)
    #generate_foilage(world)
    player = utils.spawn_player(world)
    print(player)
    game_terminal(world, player)
    # time.sleep(3)
    print(data)


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
    time.sleep(4)
    print("Are you ready to enter the world of Elderflame? Too bad. Here you go!")
    time.sleep(4)
    begin_game(data)


i = 0


def execute(c):
    exec('global i; i = %s' % c)
    global i
    return i


def on_press(key):
    # this is the input function of the program
    # we give them the "pointer" and concat what they are typing onto it
    pointer = ("%s>%s" % (fg('white'), attr('reset')))
    try:
        key = "{0}".format(key.char)
        utils.Variables.currentlyTyping += key
        print("\033[A                             \033[A")
        print(pointer + " {0}".format(utils.Variables.currentlyTyping))
    except AttributeError:
        # key pressed was nonalphanumeric, check for movement.
        key = "{0}".format(key)
        if(key == "Key.enter"):
            # execute whatever command is in terminal currently
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
            else:
                print("\nInvalid command.")
                time.sleep(3)
                print("\033[A                             \033[A")
                print("\033[A                             \033[A")
                utils.Variables.currentlyTyping = ""
                return False
        #     # it falls out and refreshes
        elif(key == "Key.space"):
            utils.Variables.currentlyTyping += ' '
        elif(key == "Key.backspace"):
            utils.Variables.currentlyTyping = utils.Variables.currentlyTyping[:-1]
            print("\033[A                             \033[A")
            print(pointer + " {0}".format(utils.Variables.currentlyTyping))
        elif(key == "Key.up"):
            command = ["move", "forward"]
            actions.move(command, world)
            return False
        elif(key == "Key.down"):
            command = ["move", "down"]
            actions.move(command, world)
            return False
        elif(key == "Key.left"):
            command = ["move", "left"]
            actions.move(command, world)
            return False
        elif(key == "Key.right"):
            command = ["move", "right"]
            actions.move(command, world)
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
        utils.get_terrain_around_player(world, player)  # print terrain
        print("\n\n\n\n%s>%s" % (fg('white'), attr('reset')))  # move down a few lines for the console input

        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

        # userInput = str(input(pointer + " "))  # actual input
        # command = userInput.split(" ")

        # if(command[0] == "move"):
        #     # inputted command is move
        #     # it default updates the player in the variables so no reassign needed.
        #     worked = actions.move(command, world, player)
        #     if(not worked):
        #         print("Eror executing command %s." % command[0])
        #         time.sleep(3)

        #     # it falls out and refreshes


world = convert()
player = utils.Player((95, 95))
#utils.get_terrain_around_player(world, player)
game_terminal(world, player)
# main()
