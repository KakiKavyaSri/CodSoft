from tkinter import *

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title("To Do List")
        
        # Set the background color of the main window
        self.root.configure(bg='#dcc4a8')
        
        # Make the main window resizable
        self.root.geometry("1000x1000")
        self.root.resizable(True, True)

        # Create a frame with the same background color
        self.page = Frame(self.root, bg='#dcc4a8')
        self.page.pack(fill=BOTH, expand=True)

        # Make the label fill the entire width of the page
        self.todotitle = Label(self.page, text=' TO - DO LIST APPLICATION', bg='#dcc4a8', fg='#873e23', font=('Showcard Gothic',35 , 'bold'), height=2)
        # Make the label fill horizontally with padding
        self.todotitle.pack(fill=X, padx=20, pady=20)

        # Label for entering task
        self.title1 = Label(self.page, text='Enter the Task : ', bg='#dcc4a8', fg='black', font=('Arial Rounded MT Bold', 25, 'bold'), height=1)
        self.title1.place(x=100, y=180)

        # Entry widget for entering task
        self.title1_entry = Entry(self.page, width=30, font=('Roboto', 25, 'bold'))
        self.title1_entry.place(x=450, y=180)

        # Smaller buttons for tasks
        self.button_add = Button(self.page, text='ADD TASK', font=('Roboto', 20, 'bold'), bg='#05ca51', fg='white', padx=10, pady=5, command=self.add)
        self.button_add.place(x=120, y=270)

        self.button_remove = Button(self.page, text='REMOVE TASK', font=('Roboto', 20, 'bold'), bg='#f6b830', fg='white', padx=10, pady=5, command=self.delete)
        self.button_remove.place(x=330, y=270)

        self.button_mark = Button(self.page, text='MARK TASK', font=('Roboto', 20, 'bold'), bg='#af67c5', fg='white', padx=10, pady=5, command=self.mark)
        self.button_mark.place(x=590, y=270)

        self.button_delete = Button(self.page, text='DELETE ALL', font=('Roboto', 20, 'bold'), bg='#f5334b', fg='white', padx=10, pady=5, command=self.delete_all)
        self.button_delete.place(x=820, y=270)

          # Listbox widget to display tasks
        self.main_text = Listbox(self.root,width = 30,height = 9,bd = 5,font=('Roboto', 20, 'bold'))
        self.main_text.place(x=420,y=380)

        # Exit button to destroy the window
        self.exit_button = Button(self.page, text='Exit', font=('Roboto', 20, 'bold'), bg='#4287f5', fg='white', padx=10, pady=5, command=self.root.destroy)
        self.exit_button.place(x=900, y=700)

        # Load tasks from file
        self.load_tasks()

    def load_tasks(self):
        try:
            with open('data.txt', 'r') as file:
                read = file.readlines()
                for i in read:
                    ready = i.split()
                    if ready:  # Check if ready list is not empty
                        self.main_text.insert(END, ready[0])
                file.close()
        except FileNotFoundError:
            pass

    # Function to add task
    def add(self):
        content = self.title1_entry.get()
        self.main_text.insert(END, content)
        with open('data.txt', 'a') as file:
            file.write(content + '\n')
        self.title1_entry.delete(0, END)  # Clear the entry box

    # Function to delete task
    def delete(self):
        delete_ = self.main_text.curselection()
        look = self.main_text.get(delete_)
        with open('data.txt', 'r+') as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
                item = str(look)
                if item not in line:
                    f.write(line)
            f.truncate()
        self.main_text.delete(delete_)

    # Function to delete all tasks
    def delete_all(self):
        self.main_text.delete(0, END)  # Delete all items in the Listbox
        self.title1_entry.delete(0, END)  # Clear the entry box

    def mark(self):
        selected_indices = self.main_text.curselection()
        for index in selected_indices:
            self.main_text.itemconfig(index, {'bg': '#ffff00', 'fg': '#000000'})  # Change background and foreground color

     # Function to save tasks and exit
    def save_and_exit(self):
        with open('data.txt', 'w') as file:
            for i in range(self.main_text.size()):
                file.write(self.main_text.get(i) + '\n')
        self.root.destroy()

def main():
    root = Tk()
    ui = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
