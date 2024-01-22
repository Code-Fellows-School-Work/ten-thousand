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
    "When player selects dice to keep, displays unbanked point total and dice remaining"
    print(f"You have {calculate_score} unbanked points and {remaining_dice} dice remaining")

def bank_points(unbanked_points, round_number, total_score):
    "When player banks point, displays banked points in round and total score"
    print(f"You banked {unbanked_points} points in round {round_number}")
    print(f"Total score is {total_score} points")

def invalid_keepers():
    "When player selects invalid dice, displays cheater message"
    print("Cheater!!! Or possibly made a typo...")

def zilch():
    "When player rolls a non-scoring roll, displays zilch message"
    print("****************************************")
    print("**        Zilch!!! Round over         **")
    print("****************************************")

def start_game(roll_dice, calculate_score):
    """
    Plays the game Ten Thousand.

    :param 
        roll_dice: int representing the number of dice to roll
        calculate_score: beginning with a score of 0, calculate the score for a given dice roll
    :return: tuple containing the results of each die roll
    """

    round_number = 1
    total_score = 0
    total_dice = 6
    unbanked_points = 0
    validate_keepers = GameLogic.validate_keepers

    while True:
        print(f"Starting round {round_number}")
        while True:
            dice = roll_dice(total_dice)
            print(f"Rolling {total_dice} dice...")
            print(f"*** {' '.join(map(str, dice))} ***")
            # zilch functionality
            if calculate_score(dice) == 0:
                zilch()
                unbanked_points = 0
                bank_points(unbanked_points, round_number, total_score)
                round_number = round_number + 1
                total_dice = 6
                break
            while True:
                choice = input("Enter dice to keep, or (q)uit:\n> ")
                if choice.lower() == "q":
                    quit_game(total_score)
                    return
                # used ChatGPT to correct tuple conversion
                # validate keepers functionality
                choice_tuple = tuple(int(num) for num in choice if num.isdigit())
                if validate_keepers(dice, choice_tuple) == False:
                    invalid_keepers()
                    print(f"*** {' '.join(map(str, dice))} ***")
                else:
                    break
            if choice:
                remove_spaces = choice.replace(" ", "")
                # used ChatGPT to correct tuple conversion
                kept_dice = tuple(int(num) for num in choice if num.isdigit())
                unbanked_points = unbanked_points + calculate_score(kept_dice)
                remaining_dice_int = total_dice - len(remove_spaces)
                # hot dice functionality
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


