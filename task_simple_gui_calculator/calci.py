import tkinter as tk
from tkinter import messagebox
from tkinter import BOTH, Frame, Label, X, Canvas

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # Set the background color of the main window
        self.root.configure(bg='#dcc4a8')
        
        # Make the main window resizable
        self.root.geometry("1000x1000")
        self.root.resizable(True, True)

        # Create a frame with the same background color
        self.page = Frame(self.root, bg='#dcc4a8')
        self.page.pack(fill=BOTH, expand=True)

        # Add a heading frame to hold the title and exit button
        self.heading_frame = tk.Frame(self.page, bg='#dcc4a8')
        self.heading_frame.pack(fill=X, padx=20, pady=20)

        # Add a label for the heading
        self.calcititle = Label(self.heading_frame, text='# SIMPLE PyCALCI #', bg='#dcc4a8', fg='#873e23', font=('Showcard Gothic', 40, 'bold'), height=2)
        self.calcititle.pack(side=tk.LEFT, fill=X, expand=True)

        # Add the round exit button
        self.exit_canvas = Canvas(self.heading_frame, width=70, height=70, bg='#dcc4a8', highlightthickness=0)
        self.exit_canvas.pack(side=tk.RIGHT, padx=10)
        self.create_round_button()

        self.expression = ""
        self.input_text = tk.StringVar()

        # Creating the input field
        self.input_frame = tk.Frame(self.page, bg='#dcc4a8')
        self.input_frame.place(relx=0.05, y=150, relwidth=0.9)  # Adjust the y for positioning below the heading

        self.input_field = tk.Entry(self.input_frame, textvariable=self.input_text, font=('arial', 25, 'bold'), bd=10, insertwidth=10, width=35, borderwidth=2)
        self.input_field.pack(fill=BOTH, ipady=20, padx=10, pady=10)  # internal padding for better appearance

        # Creating the buttons
        self.button_frame = tk.Frame(self.page, bg='#dcc4a8')
        self.button_frame.place(relx=0.05, y=300, relwidth=0.9, relheight=0.6)  # Adjust the y for positioning below the input frame

        # Buttons layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

    def create_button(self, value, row, column):
        button = tk.Button(self.button_frame, text=value, font=('arial', 18, 'bold'), command=lambda: self.on_button_click(value), height=2, width=7)
        button.grid(row=row, column=column, padx=5, pady=5, sticky='nsew')

        # Configure grid to expand
        self.button_frame.grid_rowconfigure(row, weight=1)
        self.button_frame.grid_columnconfigure(column, weight=1)

    def on_button_click(self, value):
        if value == "C":
            self.clear()
        elif value == "=":
            self.calculate()
        elif value in '+-*/':
            self.add_operator(value)
        else:
            self.add_to_expression(value)

    def clear(self):
        self.expression = ""
        self.input_text.set(self.expression)

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except:
            messagebox.showerror("Error", "Invalid Input")
            self.expression = ""
            self.input_text.set("")

    def add_operator(self, operator):
        self.expression += operator
        self.input_text.set(self.expression)

    def add_to_expression(self, value):
        self.expression += str(value)
        self.input_text.set(self.expression)

    def create_round_button(self):
        # Draw a larger circle on the canvas
        self.exit_canvas.create_oval(5, 5, 65, 65, fill="#b9393d", outline="#4287f5")

        # Add text in the center of the circle
        self.exit_canvas.create_text(35, 35, text='Exit', fill='white', font=('Roboto', 15, 'bold'))

        # Bind click event to the canvas to destroy the root window
        self.exit_canvas.bind("<Button-1>", lambda event: self.root.destroy())


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
