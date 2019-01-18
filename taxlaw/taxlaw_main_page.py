#! python3

# Crappy GUI, NEEDS WORK!
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, Menu
from taxlaw import Configuration

# Todo Rondell K. -> Redesign interface, Possibly use Javascript (Research React or Angular)
class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Tax Scraper")
        self.entered_county = ""

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.add_button = Button(master, text="+", command=lambda: self.update("add"))

        # LAYOUT
        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)
        self.reset_button.grid(row=2, column=2, sticky=W+E)

    def validate(self, new_text):
        if not new_text:  # the field is being cleared
            self.entered_county = ""
            return True

        try:
            url = Configuration.loaded_sites[self.entered_county.lower()]
        except KeyError:
            self.entered_county = "County not found"
            return False

    def get_data(self):
        print('Scraping {]'.fo)
root = Tk()
my_gui = Calculator(root)
root.mainloop()
