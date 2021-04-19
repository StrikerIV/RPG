import time
import utils


def main():
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
    except ValueError as e:
        print("\nPlease supply a valid choice.")

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
    print("Chose your culture by typing it. You can view information on a culute by choosing the appropriate number option.\n")
    print("+-------------+")
    print("| 1. Svec     |")
    print("| 2. Baeskens |")
    print("| 3. Thurber  |")
    print("| 4. Dueck    |")
    print("| 5. Obeng    |")
    print("| 6. Bostian  |")
    print("+-------------+\n")

    choice = input()

    try:
        choice = int(choice)
    except ValueError as e:
        print("Please supply a valid choice.\n")

        time.sleep(2)
        utils.clear_screen()
        return create_character()

    if(choice == 1):
        print("    The Svec's\nRuthless Vikings descendants of adventures from Norway. Known for their ruthless\nstyle of war, they prefer blood over peace.")


def start_game():
    time.sleep(2)
    utils.clear_screen()
    print("Welcome to Elderflame, a world of endless possibilities.\n")
    time.sleep(2)
    print("I'm the narrator; you won't hear much from me from this little conversation.")
    time.sleep(2)
    message = "Before we get started, you need to create a character. Let's do that now."
    print(message)
    utils.ongoing(message, 3)
    time.sleep(2)
    create_character()


main()
