# Write your code here
import random


class RockPaperScissors:
    default_opt = {"rock": "paper",
                   "paper": "scissors",
                   "scissors": "rock"}

    def __init__(self):
        self.name = None
        self.ratings = {}
        self.options = {}

    def main(self):
        self.game_config()
        print("Okay, let's start")
        while True:
            human = input()
            if self.valid_input(human):
                computer = random.choice(list(self.options.keys()))
                self.game_result(human, computer)

    def game_config(self):
        self.saved_ratings()
        self.username()
        self.ratings.setdefault(self.name, 0)
        self.def_options()

    def saved_ratings(self):
        with open('rating.txt', 'r') as rating_file:
            for rating in rating_file:
                player_name, score = rating.split(sep=" ", maxsplit=1)
                self.ratings[player_name] = int(score)

    def username(self):
        self.name = input("Enter your name: ")
        print(f"Hello, {self.name}")

    def def_options(self):
        options = input()
        if not options:
            self.options = RockPaperScissors.default_opt
        else:
            options = options.split(',')
            for option in options:
                option_index = options.index(option)
                tmp_option = options[option_index + 1:] + options[:option_index]
                self.options[option] = tmp_option[:len(tmp_option) // 2]

    def valid_input(self, human):
        if human == "!exit":
            exit('Bye!')
        elif human == "!rating":
            print(self.ratings.get(self.name))
            return False
        elif not self.options.get(human):
            print("Invalid input")
            return False
        return True

    def game_result(self, human, computer):
        if human == computer:
            print(f'There is a draw ({computer})')
            self.ratings[self.name] += 50
        elif computer not in self.options.get(human):
            print(f'Well done. The computer chose {computer} and failed')
            self.ratings[self.name] += 100
        elif computer in self.options.get(human):
            print(f'Sorry, but the computer chose {computer}')


play_game = RockPaperScissors()
play_game.main()