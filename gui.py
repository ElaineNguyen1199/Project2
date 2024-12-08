from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from logic import *
import csv

class RockPaperScissors:
    """
    A GUI class for the Rock, Paper, Scissors game. Handles the interaction between the player and computer,
    and updates the display based on the game results.
    """
    def __init__(self, root: Tk) -> None:
        """
        Initializes the RockPaperScissors Gui application.
        :param root: The Tkinter root window
        """
        self.root = root
        self.game_logic = Logic()
        self.create_widgets()

    def handle_choice(self, player_choice: str) -> None:
        """
        Handles the player's choice, determines the game's outcome, and updates the gui display
        :param player_choice: The player's choices ("Rock", "Paper", "Scissors").
        """
        computer_choice = self.game_logic.get_computer_choice()
        match_results = self.game_logic.decide_winner(player_choice, computer_choice)
        self.user_choice_label.config(text=f'Your Choice: {player_choice}')
        self.computer_choice_label.config(text=f"Computer Choice: {computer_choice}")
        self.results_label.config(text=match_results)
        player_score, computer_score = self.game_logic.get_scores()

        self.user_score_label.config(text=f"Your Score: {player_score}")
        self.computer_score_label.config(text=f"Computer Score: {computer_score}")

        self.write_to_csv(player_choice, computer_choice, match_results, player_score, computer_score)

    def write_to_csv(self, player_choice: str, computer_choice: str, match_results: str, player_score: int, computer_score: int) -> None:
        """
        Writes the game details to a CSV file.
        :param player_choice: Player's choices ("Rock", "Paper", "Scissors").
        :param computer_choice: Computer's choices ("Rock", "Paper", "Scissors").
        :param match_results: The results of the match ("It's a Tie!", "You win!", "Computer wins!")
        :param player_score: The player's current score.
        :param computer_score: The computer's current score.
        """
        file_path = "game_results.csv"  # Specify the CSV file path
        try:
            with open(file_path, mode='a', newline='') as file:
                writer = csv.writer(file)

                # Write a header row if the file is empty
                if file.tell() == 0:
                    writer.writerow(["Player Choice", "Computer Choice", "Result", "Player Score", "Computer Score"])
                writer.writerow([player_choice, computer_choice, match_results, player_score, computer_score])
        except IOError as e:
            print(f"Error writing to CSV file: {e}")

    def create_widgets(self) -> None:
        """
        Creates and arranges the widgets for the RockPaperScissors Gui.
        """
        # Title
        title_label = Label(self.root, text="ROCK, PAPER, SCISSORS", font=("Times New Roman", 20, "bold"), bg="lightgray")
        title_label.pack(pady=10)

        # Choice Section
        choice_frame = Frame(self.root, bg="lightgray")
        choice_frame.pack(pady=10)

        pick_label = Label(choice_frame, text="PICK ONE:", font=("Times New Roman", 14), bg="lightgray")
        pick_label.pack(side=LEFT, padx=10)

        # Add Buttons
        self.create_choice_buttons(choice_frame)

        # Match Result Label
        self.results_label = Label(self.root, text="", font=("Times New Roman", 16, "bold"), bg="lightgray")
        self.results_label.pack(pady=20)

        # Choices Display Section
        display_frame = Frame(self.root, bg="lightgray")
        display_frame.pack(pady=10)

        # User and Computer Choices
        self.user_choice_label = Label(display_frame, text="Your Choice:", font=("Times New Roman", 15), bg="lightgray")
        self.user_choice_label.pack(side=LEFT, padx=40)

        self.computer_choice_label = Label(display_frame, text="Computer’s Choice:", font=("Times New Roman", 15), bg="lightgray")
        self.computer_choice_label.pack(side=RIGHT, padx=40)

        # Scores Display Section
        score_frame = Frame(self.root, bg="lightgray")
        score_frame.pack(pady=10)

        # User and Computer Scores
        self.user_score_label = Label(score_frame, text="Your Score: 0", font=("Times New Roman", 15), bg="lightgray")
        self.user_score_label.pack(side=LEFT, padx=40)

        self.computer_score_label = Label(score_frame, text="Computer’s Score: 0", font=("Times New Roman", 15), bg="lightgray")
        self.computer_score_label.pack(side=RIGHT, padx=40)

        # Exit Button
        exit_button = Button(self.root, text="Exit", font=("Times New Roman", 14), command=self.root.destroy)
        exit_button.pack(side=BOTTOM, pady=20)

    def create_choice_buttons(self, parent: Frame) -> None:
        """
        Creates buttons for player's choices using associated images (Rock, Paper, Scissors).
        :param parent: The parent frame to hold the buttons.
        """
        # Rock Button
        rock_image_path = "C:/Users/elain/Documents/Project2/images/new_rock.png"
        image = Image.open(rock_image_path)
        image.thumbnail((150, 150))
        rock_image_tk = ImageTk.PhotoImage(image)
        rock_button = ttk.Button(parent, image=rock_image_tk, compound="center", command=lambda: self.handle_choice("Rock"))
        rock_button.image = rock_image_tk
        rock_button.pack(side=LEFT, padx=10)

        # Scissors Button
        scissors_image_path = "C:/Users/elain/Documents/Project2/images/new_scissors.png"
        image = Image.open(scissors_image_path)
        image.thumbnail((150, 150))
        scissors_image_tk = ImageTk.PhotoImage(image)
        scissors_button = ttk.Button(parent, image=scissors_image_tk, compound="center", command=lambda: self.handle_choice("Scissors"))
        scissors_button.image = scissors_image_tk
        scissors_button.pack(side=LEFT, padx=10)

        # Paper Button
        paper_image_path = "C:/Users/elain/Documents/Project2/images/new_paper.png"
        image = Image.open(paper_image_path)
        image.thumbnail((150, 150))
        paper_image_tk = ImageTk.PhotoImage(image)
        paper_button = ttk.Button(parent, image=paper_image_tk, compound="center", command=lambda: self.handle_choice("Paper"))
        paper_button.image = paper_image_tk
        paper_button.pack(side=LEFT, padx=10)