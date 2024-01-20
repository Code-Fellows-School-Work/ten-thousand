# play and start_game functions are JB starter code
import sys

from game_logic.game_logic import GameLogic

def play_game(roll_dice):

    round_number = 1
    total_score = 0

    print(f"Starting round {round_number}")
    print("Rolling 6 dice...")

    dice = roll_dice(6)

    print(f"*** {' '.join(map(str, dice))} ***")
    choice = input("Enter dice to keep, or (q)uit:\n> ")
    if choice == "q":
        quit_game(total_score)
    # elif choice == [1, 2, 3, 4, 5, 6]:
    #     keep_dice(calculate_score)
    else:
        print("4, 4") # continue from here
        
                    
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

def quit_game(total_score):
    print(f"Thanks for playing. You earned {total_score} points")
    # sys.exit()
    
def no_play():
    print('OK. Maybe another time')

def keep_dice(calculate_score):
    print(f"You have {calculate_score} unbanked points and 5 dice remaining")

if __name__ == "__main__":
    play()


