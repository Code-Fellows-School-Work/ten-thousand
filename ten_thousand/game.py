# play and start_game functions are JB starter code

from game_logic.game_logic import GameLogic

def play(roller=None):
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    print("> n")
    print("OK. Maybe another time")

def one_and_done():
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    print("> y")
    print("Starting round 1")
    print("Rolling 6 dice...")
    print("*** 4 4 5 2 3 1 ***")
    print("Enter dice to keep, or (q)uit:")
    print("> q")
    print("Thanks for playing. You earned 0 points")


# if __name__ == "__main__":
play() 
one_and_done()