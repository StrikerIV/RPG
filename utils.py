from os import system, name
import time


class Attribute:
    def __init__(self, culture, attribute, percent):
        self.culture = culture
        self.attribute = attribute
        self.percent = percent


def get_choice():
    choice = input()
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
