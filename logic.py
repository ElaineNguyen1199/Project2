import random

class Logic:
    def __init__(self):
        self.computer_value = {
            "0": "Rock",
            "1": "Paper",
            "2": "Scissors"
        }
        self.player_score = 0
        self.computer_score = 0

    def get_computer_choice(self):
        return self.computer_value[str(random.randint(0, 2))]


    def decide_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            match_result = "Match Draw"
        elif (player_choice == "Rock" and computer_choice == "Scissor") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            self.player_score += 1
        else:
            self.computer_score += 1

    def get_scores(self):
        return self.player_score, self.computer_score


