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
        Beginning with a score of 0, calculate the score for a given dice roll

        :param dice_roll: tuple of integers representing the dice roll
        :return: int representing the score
        """
        score = 0
        counter = Counter(dice_roll)

        "If the dice roll is a straight, then add to score 1500"
        if set(dice_roll) == {1, 2, 3, 4, 5, 6}:
            return 1500

        "If there are three pairs of any values, then add to score 1500"
        if len(counter) == 3 and all(count == 2 for count in counter.values()):
            return 1500

        "Iterate over each dice count and score the following:"
        for num, count in counter.items():
            """If the count of a dice appears 3 or more times, do the following:
            If there are three 1s, add to score 1000
            Else there are three-of-a-kind of any other count, add to score count * 100 
            If there are more than three-of-a-kind, then add additional points to score
            Else if the count of a dice appears less than 3 times and is 1 or a 5:
            Add to score count * 100 for each 1 and add to score count * 50 for each 5"""
            if count >= 3:
                if num == 1:
                    score += 1000
                else:
                    score += num * 100
                if count > 3:
                    increment = 100 * (num if num != 1 else 10)
                    score += increment * (count - 3)
            else:
                if num == 1:
                    score += count * 100
                elif num == 5:
                    score += count * 50

        return score

    @staticmethod
    def validate_keepers(roll, keepers):
        """
        Validate that the keepers are a valid subset of the roll.

        :param roll: tuple of integers representing the original dice roll
        :param keepers: tuple of integers representing the dice the user wants to keep
        :return: bool indicating whether the keepers are a valid subset of the roll
        """
        roll_counter = Counter(roll)
        keepers_counter = Counter(keepers)
        for die in keepers_counter:
            if keepers_counter[die] > roll_counter[die]:
                return False
        return True
        
