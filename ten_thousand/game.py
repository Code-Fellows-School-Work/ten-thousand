# play and start_game functions are JB starter code
import sys

from game_logic.game_logic import GameLogic

def play(roller=None):
    "Allows player to choose if they want to play game or quit game"

    roll_dice = roller or GameLogic.roll_dice
    calculate_score = GameLogic.calculate_score

    print("Welcome to Ten Thousand")

    choice = input("(y)es to play or (n)o to decline\n> ")
    if choice.lower() == "n":
        no_play()

    else:
        start_game(roll_dice, calculate_score)

def quit_game(total_score):
    "When player quits game, prints total score and resets game score to 0"
    print(f"Thanks for playing. You earned {total_score} points")
    total_score = 0
        
def no_play():
    "When player quits after first starting up game, then prints this message"
    print('OK. Maybe another time')

def keep_dice(calculate_score, remaining_dice):
    print(f"You have {calculate_score} unbanked points and {remaining_dice} dice remaining")

def start_game(roll_dice, calculate_score):

    round_number = 1
    total_score = 0
    total_dice = 6

    print(f"Starting round {round_number}")
    print("Rolling 6 dice...")

    dice = roll_dice(6)

    print(f"*** {' '.join(map(str, dice))} ***")
    choice = input("Enter dice to keep, or (q)uit:\n> ")
    if choice.lower() == "q":
        quit_game(total_score)
    elif choice:
        # print("Player choice: ", choice)
        # print("Data type: ", type(choice))
        # print("before replace", len(choice))\
        # find the space in this string and remove it
        remove_spaces = choice.replace(" ", "")
        # print("after replace", len(remove_spaces))
        score = calculate_score(dice)
        remaining_dice = total_dice - len(remove_spaces)
        keep_dice(score, remaining_dice)
        while False:
            print("while loop example")


                    

if __name__ == "__main__":
    play()


