import time
import random
import string
import enum

options = ("yes", "no", "fight", "run")
response = ("1", "2")


class Color(enum.Enum):
    red = '\033[91m'
    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    black = '\033[0m'
    bold = '\033[1m'

    @classmethod
    def get_color(cls):
        return random.choice([color.value for color in cls])


def typewriter_simulator(message):
    for char in message:

        print(char, end='')
        if char in string.punctuation:
            time.sleep(.5)
        time.sleep(.03)
    print('')


def print_pause(message, delay=+1):
    typewriter_simulator(message)
    print(Color.get_color())
    time.sleep(delay)


def valid_input(message, options):
    while True:
        response = input(message).lower().strip()
        if response in options:
            return response
        else:
            print_pause("Sorry, invalid option")


def intro():
    print_pause("You find yourself standing deep under the sea!")
    print_pause("Whoever gets here doesn't live to tell the tale.")
    print_pause("In front of you there a poisonous plant Lily-Of-The-Valley")
    print_pause("To your left there's a pathway filled with sharks.")
    print_pause("In your hand you have time machine.")


intro()


def pathway_adventure1():
    user_input = valid_input("Would you like to play: yes/no?", options)
    random.choice(options)
    if 'yes' in user_input:
        print_pause("Congratulations, you are ready to begin.")
    elif 'no' in user_input:
        print_pause("Thank you for playing")
    else:
        print_pause("Sorry,I don't understand")


pathway_adventure1()


def pathway_adventure(response):
    answer = valid_input("""
    Enter 1 to peer into the pathway/n
    Enter 2 to for the Lily_of_the_Valley./n
    What would you like to do?:/
                         """, response)
    if "1" in answer:
        print_pause("You peer cautiously into the pathway")
        print_pause("Luckily for you, the sharks are taking a nap")
        print_pause("Your eye catches a glimpse of the door.")
        print_pause("You can slowly walk out, don't wake them .")
        print_pause("You discard your time machine and go back home.")
        exit()
    elif "2" in answer:
        print_pause("You approach the Lily of the Valley, get ready to attack")
        print_pause("You about to escape and a huge force pushes you away.")
        print_pause("Eep! This is the most dangerous part of the game.")
        print_pause("Find a way to escape.")
    else:
        print_pause("I'm sorry, would you like to try again?")


pathway_adventure(response)


def lily_of_the_valley(options):
    print_pause("You are in front of the most dangerous plant in the game.")
    choice = valid_input("Would you like to fight or run away?: ", options)
    if "fight" in choice:
        print_pause("Great time to use your time machine, it will help.")
        print_pause("Game Over, you have lost")
        exit()
    elif "run" in choice:
        print_pause("Congratulations, you have won the game!")

    else:
        print_pause("You have lost, sorry Game Over.")


lily_of_the_valley(options)


def play_again(options):
    while True:
        response = valid_input("""
Would you like to play again:
Please say yes or no\n
Yes/No
""", options).lower().strip()
        if response == "yes":
            print_pause("Get ready for an adventure")
            play_game()  # call the play_game function to start the game again
        elif response == "no":
            print_pause("Thank you for playing")
            break  # exit the loop and end the game
        else:
            print_pause("Sorry, selection invalid")


play_again(options)


def play_game():
    options = ("yes", "no", "fight", "run")
    response = ("1", "2")
    intro()
    valid_input(response, options)
    play_again(options)


play_game()

