from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Main Window
root = Tk()
root.title("Rock, Paper, Scissors")
root.geometry("500x400")
root.resizable(False, False)
root.configure(bg="lightgray")

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
image.thumbnail((100, 100))
# rock_image = rock_image.resize((50, 50), Image.Resampling.LANCZOS)
rock_image_tk = ImageTk.PhotoImage(image)
rock_button = ttk.Button(choice_frame, image=rock_image_tk, compound="top")
rock_button.pack(side=LEFT, padx=10)

# Scissors Button
scissors_image_path = "C:/Users/elain/Documents/Project2/images/new_scissors.png"
image = Image.open(scissors_image_path)
image.thumbnail((100, 100))
# scissors_image = scissors_image.resize((50, 50), Image.Resampling.LANCZOS)
scissors_image_tk = ImageTk.PhotoImage(image)
scissors_button = ttk.Button(choice_frame, image=scissors_image_tk, compound="top")
scissors_button.pack(side=LEFT, padx=10)

# Paper Button
paper_image_path = "C:/Users/elain/Documents/Project2/images/new_paper.png"
image = Image.open(paper_image_path)
image.thumbnail((100, 100))
# paper_image = paper_image.resize((50, 50), Image.Resampling.LANCZOS)
paper_image_tk = ImageTk.PhotoImage(image)
paper_button = ttk.Button(choice_frame, image=paper_image_tk, compound="top")
paper_button.pack(side=LEFT, padx=10)

# Separator
separator = Label(root, text="ENTER", font=("Times New Roman", 14), bg="lightgray")
separator.pack(pady=10)

# Choices Display Section
display_frame = Frame(root, bg="lightgray")
display_frame.pack(pady=10)

# User and Computer Choices
user_choice_label = Label(display_frame, text="Your Choice:", font=("Times New Roman", 12), bg="lightgray")
user_choice_label.pack(side=LEFT, padx=40)

computer_choice_label = Label(display_frame, text="Computer’s Choice:", font=("Times New Roman", 12), bg="lightgray")
computer_choice_label.pack(side=RIGHT, padx=40)

# Scores Display Section
score_frame = Frame(root, bg="lightgray")
score_frame.pack(pady=10)

# User and Computer Scores
user_score_label = Label(score_frame, text="Your Score:", font=("Times New Roman", 12), bg="lightgray")
user_score_label.pack(side=LEFT, padx=40)

computer_score_label = Label(score_frame, text="Computer’s Score:", font=("Times New Roman", 12), bg="lightgray")
computer_score_label.pack(side=RIGHT, padx=40)

root.mainloop()
