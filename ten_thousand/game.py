# play and start_game functions are JB starter code
import sys

from ten_thousand.game_logic import GameLogic

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

def unbank_points_and_dice_remaining_str(calculate_score, remaining_dice):
    print(f"You have {calculate_score} unbanked points and {remaining_dice} dice remaining")

def bank_points(unbanked_points, round_number, total_score):
    print(f"You banked {unbanked_points} points in round {round_number}")
    print(f"Total score is {total_score} points")

def invalid_keepers():
    print("Cheater!!! Or possibly made a typo...")

def start_game(roll_dice, calculate_score):

    round_number = 1
    total_score = 0
    total_dice = 6
    unbanked_points = 0
    validate_keepers = GameLogic.validate_keepers

    while True:
        print(f"Starting round {round_number}")
        # print(f"score before:", total_score)
        while True:
            dice = roll_dice(total_dice)
            print(f"Rolling {total_dice} dice...")
            print(f"*** {' '.join(map(str, dice))} ***")
            choice = input("Enter dice to keep, or (q)uit:\n> ")
            # print("score after:", total_score)
            if choice.lower() == "q":
                quit_game(total_score)
                return
            # if validate_keepers(dice, choice) == False:
            #     invalid_keepers()
            #     print(f"*** {' '.join(map(str, dice))} ***")
            #     choice = input("Enter dice to keep, or (q)uit:\n> ")
            elif choice:
                # find the space in this string and remove it
                remove_spaces = choice.replace(" ", "")
                kept_dice = tuple(int(num) for num in choice)
                unbanked_points = unbanked_points + calculate_score(kept_dice)
                remaining_dice_int = total_dice - len(remove_spaces)
                # if player keeps all dice or no dice remain, then hot dice
                if len(kept_dice) == 6 or total_dice == 0:
                    remaining_dice_int = 6
                unbank_points_and_dice_remaining_str(unbanked_points, remaining_dice_int)
                player_decision = input("(r)oll again, (b)ank your points or (q)uit:\n> ")
                if player_decision.lower() == "r":
                    total_dice = remaining_dice_int
                if player_decision.lower() == "b":
                    total_score = total_score + unbanked_points
                    bank_points(unbanked_points, round_number, total_score)
                    round_number = round_number + 1
                    total_dice = 6
                    unbanked_points = 0
                    break
                if player_decision.lower() == "q":
                    quit_game(total_score)
                    return
                

if __name__ == "__main__":
    play()


