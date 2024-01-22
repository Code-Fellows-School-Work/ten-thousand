# play and start_game functions are JB starter code

from ten_thousand.game_logic import GameLogic

def play(roller=None, num_rounds=20):
    global dice_roller
    dice_roller = roller or GameLogic.roll_dice


def get_dice_to_set_aside(current_roll):
    """
    Ask the user which dice to set aside. Ensures that '0' is not entered.

    :param current_roll: tuple - the current roll of dice
    :return: list - the dice that the user wants to set aside
    """
    while True:
        "Prints dice roll and asks user to select dice"
        print(f"Current roll: {current_roll}")
        dice_to_set_aside = input("Enter the dice you want to set aside (e.g., '1 5 5'), no zeroes allowed: ")
        try:
            "Prevents player from selecting 0. If valid dice is selected, then return dice"
            selected_dice = [int(die) for die in dice_to_set_aside.split()]
            if 0 in selected_dice:
                print("Entering '0' is not allowed. Please enter valid dice values.")
                continue
            return selected_dice
        except ValueError:
            print("Invalid input. Please enter the dice using numbers separated by spaces.")

def bank_score(total_score, round_score):
    """Bank the current round's score to the total score."""
    total_score += round_score
    print(f"You banked your score! Total Score: {total_score}")
    return total_score

def track_total_score(total_score):
    """Display the total score."""
    print(f"Total Score: {total_score}")

def next_round(current_round):
    """Increment and display the current round number."""
    current_round += 1
    print(f"Round {current_round}")
    return current_round

def play_game():
    total_score = 0
    num_dice = 6
    current_round = 0

    while True:
        next_round(current_round)
        round_score = 0
        round_in_progress = True

        while round_in_progress:
            current_roll = GameLogic.roll_dice(num_dice)
            print(f"Rolled: {current_roll}")

            dice_set_aside = get_dice_to_set_aside(current_roll)
            round_score += GameLogic.calculate_score(tuple(dice_set_aside))

            num_dice -= len(dice_set_aside)
            if num_dice == 0:
                num_dice = 6

            print(f"Round Score: {round_score}")
            player_choice = input("Choose 'bank', 'roll' again, or 'quit': ").strip().lower()

            if player_choice == 'bank':
                total_score = bank_score(total_score, round_score)
                current_round = next_round(current_round)
                num_dice = 6
                round_in_progress = False
            elif player_choice == 'roll':
                if num_dice == 0:
                    print("All dice are set aside. Rolling all 6 dice again.")
                    num_dice = 6
                continue
            elif player_choice == 'quit':
                print(f"Quitting the game. Final Score: {total_score}")
                return
            else:
                print("Invalid input. Please type 'bank', 'roll', or 'quit'.")

        track_total_score(total_score)


if __name__ == "__main__":

    # rolls = [
    #     (3, 2, 5, 4, 3, 3),
    #     (5, 2, 3, 2, 1, 4)
    # ]
    # def mock_roller(num_dice):
    #     return rolls.pop(0)
    
    # play_game(roller=mock_roller) 

    play_game()
