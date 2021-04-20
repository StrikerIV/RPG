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
            print("\nThe Svec\n\nRuthless Vikings descendants of adventurers from Norway. Known for their ruthless\nstyle of war, they prefer bloodshed over diplomacy for peace.\n\n+20% Strength")
            time.sleep(7)
        elif(choice == 2):
            print("\nThe Baesken\n\nPeaceful fisherman from the rivers of the Northwest. Prideful of their vast\ndelicacies, they strive to be better than everyone else at cooking.\n\n+20% Cooking")
            time.sleep(7)
        elif(choice == 3):
            print("\nThe Thurber\n\nHardened blacksmiths from the mountains, they are strong and persevere.\nBe sure to know they won't back down without a fight, as they will always be ready.\n\n+20% Strength")
            time.sleep(7)
        elif(choice == 4):
            print("\nThe Dueck\n\nFarmers from the hills of Italy, they are stadefast towards their religion.\nThey will fight to protect their faith, by any means, at any cost.\n\n+20% Charisma")
            time.sleep(6)
        elif(choice == 5):
            print("\nThe Obeng\n\nMasters of building, they come from the valleys of China. Skilled craftsman, they\nconstruct the most engineered buildings to date.\n\n+20% Intelligence")
            time.sleep(7)
        elif(choice == 6):
            print("\nThe Boastian\n\nComing from the foothills of Spain, these folk love dancing and well, showing off.\nBut when the time is right, they'll be as strong as giants.\n\n+20% Tactics")
            time.sleep(7)
        else:
            print("\nPlease supply a valid choice.")
            time.sleep(3)

        utils.clear_screen()
        create_character()
    except ValueError:
        # chose a culture
        choice = choice.lower()

        if(choice == "svec"):
            octave2 += 1
            octave1 += 2
            attribute = utils.Attribute("Svec", "strength", 20)
        elif(choice == "baeskens"):
            octave2 += 2
            octave1 += 3
            attribute = utils.Attribute("Baeskens", "cooking", 20)
        elif(choice == "thurber"):
            octave2 += 3
            octave1 += 4
            attribute = utils.Attribute("Thurber", "strength", 20)
        elif(choice == "dueck"):
            octave2 += 4
            octave1 += 5
            attribute = utils.Attribute("Dueck", "charisma", 20)
        elif(choice == "obeng"):
            octave2 += 5
            octave1 += 6
            attribute = utils.Attribute("Obeng", "intelligence", 20)
        elif(choice == "bostian"):
            octave2 += 6
            octave1 += 7
            attribute = utils.Attribute("Bostian", "tactics", 20)
        else:
            print("\nPlease supply a valid choice.")
            time.sleep(2)
            utils.clear_screen()
            create_character()

    return ((octave1, octave2), attribute)


def begin_game(data):
    # to begin, we create the map based on octaves and frequency
    utils.clear_screen()
    print("Welcome to the world of Elderflame.")
    time.sleep(2)
    print("Give us a moment to set up your world.\n")
    create_noise_map(data[0])
    print("Noise map generated. Starting conversion.")
    convert()
    message = "Converted. Starting game."
    print(message)
    utils.ongoing(message, 3)
    # time.sleep(3)
    print(data)


def start_game():
    time.sleep(2)
    utils.clear_screen()
    print("Welcome to Elderflame, a world of endless possibilities.\n")
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
    time.sleep(2)
    begin_game(data)

main()
