# play and start_game functions are JB starter code
import sys

from game_logic.game_logic import GameLogic

def play_game(roll_dice):

    print("Starting round 1")
    print("Rolling 6 dice...")

    dice = roll_dice(6)

    print(f"*** {' '.join(map(str, dice))} ***")
    choice = input("Enter dice to keep, or (q)uit:\n> ")
    if choice == "q":
        quit_game()
    else:
        # print("4, 4") # continue from here
        keep_dice()
                    
def play(roller=None):
    roll_dice = roller or GameLogic.roll_dice
    print("Welcome to Ten Thousand")

    choice = input("(y)es to play or (n)o to decline\n> ")
    if choice.lower() == "n":
        no_play()

    elif choice.lower() == "y":
        play_game(roll_dice)

    # elif choice.lower == "q":
    #     quit_game()

def quit_game():
    print("Thanks for playing. You earned 0 points")
    # sys.exit()
    
def no_play():
    print('OK. Maybe another time')

def keep_dice():


if __name__ == "__main__":
    play()
# play()

