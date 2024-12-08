from gui import *

def main() -> None:
    """
    Creates the main Tkinter window
    """
    root = Tk()
    root.title("Rock, Paper, Scissors")
    root.geometry("750x500")
    root.resizable(False, False)
    root.configure(bg="lightgray")
    RockPaperScissors(root)
    root.mainloop()

if __name__ == '__main__':
    main()