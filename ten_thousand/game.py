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

def bank_points(unbanked_points, round_number, total_score):
    print(f"You banked {unbanked_points} points in round {round_number}")
    print(f"Total score is {total_score} points")

def start_game(roll_dice, calculate_score):

    round_number = 1
    total_score = 0
    total_dice = 6

    while True:
        print(f"Starting round {round_number}")
        print("Rolling 6 dice...")

        dice = roll_dice(6)

        print(f"*** {' '.join(map(str, dice))} ***")
        choice = input("Enter dice to keep, or (q)uit:\n> ")
        if choice.lower() == "q":
            quit_game(total_score)
            return
        elif choice:
            # print("Player choice: ", choice)
            # print("Data type: ", type(choice))
            # print("before replace", len(choice))\
            # find the space in this string and remove it
            remove_spaces = choice.replace(" ", "")
            # print("after replace", len(remove_spaces))
            unbanked_points = calculate_score(dice)
            # print("Unbanked points:", unbanked_points)
            remaining_dice = total_dice - len(remove_spaces)
            keep_dice(unbanked_points, remaining_dice)
            player_decision = input("(r)oll again, (b)ank your points or (q)uit:\n> ")
            # if player_decision.lower == "r":
            #     roll_again function
            if player_decision.lower() == "b":
                total_score = total_score + unbanked_points
                bank_points(unbanked_points, round_number, total_score)
                round_number = round_number + 1
            # else:
            #     quit_game(total_score)
            #     return
                    

if __name__ == "__main__":
    play()


