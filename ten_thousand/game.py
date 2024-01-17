# play and start_game functions are JB starter code

from game_logic import GameLogic

def get_dice_to_set_aside(current_roll):
    """
    Ask the user which dice to set aside. Ensure that '0' is not entered.

    :param current_roll: tuple - the current roll of dice
    :return: list - the dice that the user wants to set aside
    """
    while True:
        print(f"Current roll: {current_roll}")
        dice_to_set_aside = input("Enter the dice you want to set aside (e.g., '1 5 5'), no zeroes allowed: ")
        try:
            selected_dice = [int(die) for die in dice_to_set_aside.split()]
            if 0 in selected_dice:
                print("Entering '0' is not allowed. Please enter valid dice values.")
                continue
            return selected_dice
        except ValueError:
            print("Invalid input. Please enter the dice using numbers separated by spaces.")

def play_game():
    total_score = 0
    num_dice = 6  # Starting with 6 dice
    current_round = 1

    while True:
        print(f"Round {current_round}")
        round_score = 0
        round_in_progress = True

        while round_in_progress:
            current_roll = GameLogic.roll_dice(num_dice)
            print(f"Rolled: {current_roll}")

            dice_set_aside = get_dice_to_set_aside(current_roll)
            # Calculate the score for the set-aside dice
            round_score += GameLogic.calculate_score(tuple(dice_set_aside))

            num_dice -= len(dice_set_aside)
            if num_dice == 0:
                num_dice = 6  # Reset the number of dice

            print(f"Round Score: {round_score}")
            player_choice = input("Do you want to 'bank' your score or 'roll' again? (bank/roll): ").strip().lower()

            if player_choice == 'bank':
                total_score += round_score
                print(f"You banked your score! Total Score: {total_score}")
                round_in_progress = False  # End of the round
            elif player_choice == 'roll':
                if num_dice == 0:
                    print("All dice are set aside. Rolling all 6 dice again.")
                    num_dice = 6
                continue  # Roll the remaining dice
            else:
                print("Invalid input. Please type 'bank' or 'roll'.")


if __name__ == "__main__":
    play_game() 
