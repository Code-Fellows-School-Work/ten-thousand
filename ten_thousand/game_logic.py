import random
from collections import Counter

class GameLogic:
    @staticmethod
    def roll_dice(num_dice):
        """
        Roll the specified number of dice and return the results.

        :param num_dice: int representing the number of dice to roll
        :return: tuple containing the results of each die roll
        """
        return tuple(random.randint(1, 6) for _ in range(num_dice))
    
    @staticmethod
    def calculate_score(dice_roll):
        """
        Calculate the score for a given dice roll.

        :param dice_roll: tuple of integers representing the dice roll
        :return: int representing the score
        """
        score = 0
        counter = Counter(dice_roll)

        # Check for a straight
        if set(dice_roll) == {1, 2, 3, 4, 5, 6}:
            return 1500

        # Check for three pairs
        if len(counter) == 3 and all(count == 2 for count in counter.values()):
            return 1500

        for num, count in counter.items():
            if count >= 3:
                if num == 1:
                    score += 1000
                else:
                    score += num * 100

                # Increment score for additional dice beyond three
                if count > 3:
                    increment = 100 * (num if num != 1 else 10)
                    score += increment * (count - 3)
            else:
                if num == 1:
                    score += count * 100
                elif num == 5:
                    score += count * 50

        return score

