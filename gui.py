from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from logic import *

# Main Window
root = Tk()
root.title("Rock, Paper, Scissors")
root.geometry("750x500")
root.resizable(False, False)
root.configure(bg="lightgray")

game_logic = Logic()

# Function to handle choice
def handle_choice(player_choice):
    computer_choice = game_logic.get_computer_choice()
    match_result = game_logic.decide_winner(player_choice, computer_choice)  # Capture match result
    user_choice_label.config(text=f'Your Choice: {player_choice}')
    computer_choice_label.config(text=f"Computer Choice: {computer_choice}")
    results_label.config(text=match_result)  # Update match result label
    player_score, computer_score = game_logic.get_scores()
    user_score_label.config(text=f"Your Score: {player_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

# Title
title_label = Label(root, text="ROCK, PAPER, SCISSORS", font=("Times New Roman", 20, "bold"), bg="lightgray")
title_label.pack(pady=10)

# Choice Section
choice_frame = Frame(root, bg="lightgray")
choice_frame.pack(pady=10)

pick_label = Label(choice_frame, text="PICK ONE:", font=("Times New Roman", 14), bg="lightgray")
pick_label.pack(side=LEFT, padx=10)

# Rock Button
rock_image_path = "C:/Users/elain/Documents/Project2/images/new_rock.png"
image = Image.open(rock_image_path)
image.thumbnail((150, 150))
rock_image_tk = ImageTk.PhotoImage(image)
rock_button = ttk.Button(choice_frame, image=rock_image_tk, compound="center", command=lambda: handle_choice("Rock"))
rock_button.pack(side=LEFT, padx=10)

# Scissors Button
scissors_image_path = "C:/Users/elain/Documents/Project2/images/new_scissors.png"
image = Image.open(scissors_image_path)
image.thumbnail((150, 150))
scissors_image_tk = ImageTk.PhotoImage(image)
scissors_button = ttk.Button(choice_frame, image=scissors_image_tk, compound="center", command=lambda: handle_choice("Scissors"))
scissors_button.pack(side=LEFT, padx=10)

# Paper Button
paper_image_path = "C:/Users/elain/Documents/Project2/images/new_paper.png"
image = Image.open(paper_image_path)
image.thumbnail((150, 150))
paper_image_tk = ImageTk.PhotoImage(image)
paper_button = ttk.Button(choice_frame, image=paper_image_tk, compound="center", command=lambda: handle_choice("Paper"))
paper_button.pack(side=LEFT, padx=10)

# Match Result Label
results_label = Label(root, text="", font=("Times New Roman", 16, "bold"), bg="lightgray", fg="blue")
results_label.pack(pady=20)

# Choices Display Section
display_frame = Frame(root, bg="lightgray")
display_frame.pack(pady=10)

# User and Computer Choices
user_choice_label = Label(display_frame, text="Your Choice:", font=("Times New Roman", 15), bg="lightgray")
user_choice_label.pack(side=LEFT, padx=40)

computer_choice_label = Label(display_frame, text="Computer’s Choice:", font=("Times New Roman", 15), bg="lightgray")
computer_choice_label.pack(side=RIGHT, padx=40)

# Scores Display Section
score_frame = Frame(root, bg="lightgray")
score_frame.pack(pady=10)

# User and Computer Scores
user_score_label = Label(score_frame, text="Your Score: 0", font=("Times New Roman", 15), bg="lightgray")
user_score_label.pack(side=LEFT, padx=40)

computer_score_label = Label(score_frame, text="Computer’s Score: 0", font=("Times New Roman", 15), bg="lightgray")
computer_score_label.pack(side=RIGHT, padx=40)

exit_button = Button(root, text="Exit", font=("Times New Roman", 14), command=root.destroy).pack(side=BOTTOM, pady=20)

root.mainloop()
