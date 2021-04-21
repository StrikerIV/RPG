import time
import utils
from convert import convert
from create_noise_map import create_noise_map


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
        # if no error, show description of culture

        if(choice == 1):
            print("\nThe Svec\n\nRuthless Vikings descendants of adventurers from Norway. Known for their ruthless\nstyle of war, they prefer bloodshed over diplomacy for peace.\n\n+20% Strength\n")
            time.sleep(5)
            choice = utils.get_choice("Do you want to chose this culture? (y,n) ")
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
            choice = utils.get_choice("Do you want to chose this culture? (y,n) ")
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
            choice = utils.get_choice("Do you want to chose this culture? (y,n) ")
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
            choice = utils.get_choice("Do you want to chose this culture? (y,n) ")
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
            choice = utils.get_choice("Do you want to chose this culture? (y,n) ")
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
            choice = utils.get_choice("Do you want to chose this culture? (y,n)")
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


def game_terminal(world, player):
    terrainAP = utils.get_terrain_around_player(world, player)
    print(terrainAP)

world = convert()
player = utils.Player((95, 80))
utils.get_terrain_around_player(world, player)
#main()