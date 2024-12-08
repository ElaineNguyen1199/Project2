import random

class Logic:
    """
    A class that contains the rock, paper, scissors game logic.
    """
    def __init__(self) -> None:
        """
        Setting up the game logic with set choices for the computer and
        tracks the player's and computer's scores.
        """
        self.computer_value: dict[str, str] = {
            "0": "Rock",
            "1": "Paper",
            "2": "Scissors"
        }
        self.player_score = 0
        self.computer_score = 0

    def get_computer_choice(self) -> str:
        """
        Randomly selects the computer's choice
        :return: The computers choice as a string ("Rock", "Paper", "Scissors").
        """
        return self.computer_value[str(random.randint(0, 2))]


    def decide_winner(self, player_choice: str, computer_choice: str) -> str:
        """
        Determines the winner or looser based on what the player's and computer's chooses.
        :param player_choice: The player's choice ("Rock", "Paper", "Scissors").
        :param computer_choice: The computer's choice ("Rock", "Paper", "Scissors").
        :return: A message indicating the match results ("It's a Tie!", "You win!", or "Computer wins!").
        """
        if player_choice == computer_choice:
            match_result = "Its a Tie!"
        elif (player_choice == "Rock" and computer_choice == "Scissor") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            match_result = "You win!"
            self.player_score += 1
        else:
            match_result = "Computer wins!"
            self.computer_score += 1
        return match_result

    def get_scores(self) -> tuple[int, int]:
        """
        Retrieves the current scores of the player and the computer.
        :return: A tuple containing the player's score and computers score.
        """
        return self.player_score, self.computer_score