import random
from tkinter import *

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        
        # Set the background color of the main window
        self.root.configure(bg='#dcc4a8')
        
        # Maximize the main window
        self.root.state('zoomed')

        # Variables to keep track of scores
        self.user_score = 0
        self.computer_score = 0

        # Title label
        self.title_label = Label(self.root, text='Rock-Paper-Scissors', bg='#dcc4a8', fg='#873e23', font=('Showcard Gothic', 35, 'bold'))
        self.title_label.pack(pady=20)

        # Frame for buttons
        self.button_frame = Frame(self.root, bg='#dcc4a8')
        self.button_frame.pack(pady=10)

        # Rock button
        self.rock_button = Button(self.button_frame, text='Rock', font=('Roboto', 20, 'bold'), bg='#05ca51', fg='white', padx=20, pady=10, command=lambda: self.play('Rock'))
        self.rock_button.grid(row=0, column=0, padx=20, pady=20)

        # Paper button
        self.paper_button = Button(self.button_frame, text='Paper', font=('Roboto', 20, 'bold'), bg='#f6b830', fg='white', padx=20, pady=10, command=lambda: self.play('Paper'))
        self.paper_button.grid(row=0, column=1, padx=20, pady=20)

        # Scissors button
        self.scissors_button = Button(self.button_frame, text='Scissors', font=('Roboto', 20, 'bold'), bg='#af67c5', fg='white', padx=20, pady=10, command=lambda: self.play('Scissors'))
        self.scissors_button.grid(row=0, column=2, padx=20, pady=20)

        # Labels to display choices and result
        self.user_choice_label = Label(self.root, text='', bg='#dcc4a8', fg='black', font=('Arial Rounded MT Bold', 20, 'bold'))
        self.user_choice_label.pack(pady=10)

        self.computer_choice_label = Label(self.root, text='', bg='#dcc4a8', fg='black', font=('Arial Rounded MT Bold', 20, 'bold'))
        self.computer_choice_label.pack(pady=10)

        self.result_label = Label(self.root, text='', bg='#dcc4a8', fg='black', font=('Arial Rounded MT Bold', 25, 'bold'))
        self.result_label.pack(pady=20)

        # Score label
        self.score_label = Label(self.root, text=f'User: {self.user_score}  Computer: {self.computer_score}', bg='#dcc4a8', fg='black', font=('Arial Rounded MT Bold', 20, 'bold'))
        self.score_label.pack(pady=20)

        # Play Again button
        self.play_again_button = Button(self.root, text='Play Again', font=('Roboto', 20, 'bold'), bg='#4287f5', fg='white', padx=20, pady=10, command=self.reset_game)
        self.play_again_button.pack(pady=50)

        # Exit button
        self.exit_button = Button(self.root, text='Exit', font=('Roboto', 20, 'bold'), bg='#d63230', fg='white', padx=20, pady=10, command=self.root.destroy)
        self.exit_button.pack(pady=20)

    def play(self, user_choice):
        """Handle the user's choice and determine the game's outcome."""
        choices = ['Rock', 'Paper', 'Scissors']
        computer_choice = random.choice(choices)
        
        self.user_choice_label.config(text=f'You chose: {user_choice}')
        self.computer_choice_label.config(text=f'Computer chose: {computer_choice}')

        if user_choice == computer_choice:
            self.result_label.config(text="It's a Tie!", fg='blue')
        elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
             (user_choice == 'Scissors' and computer_choice == 'Paper') or \
             (user_choice == 'Paper' and computer_choice == 'Rock'):
            self.result_label.config(text='You Win!', fg='green')
            self.user_score += 1
        else:
            self.result_label.config(text='You Lose!', fg='red')
            self.computer_score += 1

        self.update_score()

    def update_score(self):
        """Update the score label with the current scores."""
        self.score_label.config(text=f'User: {self.user_score}  Computer: {self.computer_score}')

    def reset_game(self):
        """Reset the game to allow another round."""
        self.user_choice_label.config(text='')
        self.computer_choice_label.config(text='')
        self.result_label.config(text='')

def main():
    root = Tk()
    ui = RockPaperScissors(root)
    root.mainloop()

if __name__ == "__main__":
    main()
