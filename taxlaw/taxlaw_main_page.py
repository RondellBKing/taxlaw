from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, Menu


class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Tax Scraper")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

        # LAYOUT
        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)
        self.reset_button.grid(row=2, column=2, sticky=W+E)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

root = Tk()
my_gui = Calculator(root)
root.mainloop()
