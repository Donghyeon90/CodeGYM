from tkinter import Tk, Label, Entry, Button, Listbox, END

#lllll
class TodoList:
    def __init__(self, window):
        # Define RGB values
        red = 73
        green = 49
        blue = 232

        hex_color = f"#{red:02x}{green:02x}{blue:02x}"


        self.window = window
        self.window.geometry ("400x400")
        self.window.title("Lost Ark Daily Tasks")
        self.window.iconbitmap("lostarkicon.ico")
        self.window.configure(background=hex_color)

    
        self.task_label = Label(window, text="Daily Task:")
        self.task_label.configure(bg=hex_color)
        self.task_label.pack()

        self.task_entry = Entry(window)
        self.task_entry.pack()

        self.add_button = Button(window, text="Add Task", command=self.add_task)
        self.add_button.configure(bg="green")
        self.add_button.pack()

        self.remove_button = Button(window, text="Remove Task", command=self.remove_task)
        self.remove_button.configure(bg="red")
        self.remove_button.pack()

        self.task_listbox = Listbox(window)
        self.task_listbox.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(END, task)
            self.task_entry.delete(0, END)

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.delete(selected_index)

# Create the main window
window = Tk()

# Create an instance of TodoList
todo_list = TodoList(window)

# Start the Tkinter event loop
window.mainloop()