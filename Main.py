import tkinter as tk
from Expense import *

#----------GLOBAL VARRIABLES----------#
ENTRYBOXWIDTH = 12
BACKGROUND_COLOR = "#171717"
FOREGROUND_COLOR = "#E6E6E6"

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.frame.grid(column = 0, row = 0, sticky = "nsew")
        self.frame["bg"] = BACKGROUND_COLOR

        self.frame.columnconfigure(0, weight = 1)
        self.frame.rowconfigure(0, weight = 1)

        #----------DATE----------#
        self.date = tk.StringVar()
        #Label
        self.dateLabel = tk.Label(self.frame, text="Date", bg = BACKGROUND_COLOR, fg = FOREGROUND_COLOR)
        self.dateLabel.grid(column = 1, row = 1)
        #Entry Box
        self.dateEntryBox = tk.Entry(self.frame, width = ENTRYBOXWIDTH, textvariable = self.date)
        self.dateEntryBox.grid(column = 1, row = 2)

        #----------AMOUNT----------#
        self.amount = tk.StringVar()
        #Label
        self.amountLabel = tk.Label(self.frame, text="Amount", bg = BACKGROUND_COLOR, fg = FOREGROUND_COLOR)
        self.amountLabel.grid(column = 2, row = 1)
        #Entry Box
        self.amountEntryBox = tk.Entry(self.frame, width = ENTRYBOXWIDTH, textvariable = self.amount)
        self.amountEntryBox.grid(column = 2, row = 2)

        #----------PERGALLON----------#
        self.perGallon = tk.StringVar()
        #Label
        self.perGallonLabel = tk.Label(self.frame, text="Per Gallon", bg = BACKGROUND_COLOR, fg = FOREGROUND_COLOR)
        self.perGallonLabel.grid(column = 3, row = 1)
        #Entry Box
        self.perGallonEntryBox = tk.Entry(self.frame, width = ENTRYBOXWIDTH, textvariable = self.perGallon)
        self.perGallonEntryBox.grid(column = 3, row = 2)

        #----------LOCATION----------#
        self.location = tk.StringVar()
        #Label
        self.locationLabel = tk.Label(self.frame, text="Location", bg = BACKGROUND_COLOR, fg = FOREGROUND_COLOR)
        self.locationLabel.grid(column = 4, row = 1)
        #Entry Box
        self.locationEntryBox = tk.Entry(self.frame, width = ENTRYBOXWIDTH, textvariable = self.location)
        self.locationEntryBox.grid(column = 4, row = 2)

        #----------DETAILS----------#
        self.details = tk.StringVar()
        #Label
        self.detailsLabel = tk.Label(self.frame, text="Details", bg = BACKGROUND_COLOR, fg = FOREGROUND_COLOR)
        self.detailsLabel.grid(column = 1, row = 3)
        #Entry Box
        self.detailsEntryBox = tk.Entry(self.frame, bd = 2, textvariable = self.details)
        self.detailsEntryBox.grid(column = 2, row = 3, columnspan = 3, sticky = "ew")

        #----------RECORDBUTTON----------#
        self.recordButton = tk.Button(self.frame, text = "Record", command = "record")
        self.recordButton.grid(column = 4, row = 4, sticky = "ew")

        #Add padding to all children of mainframe
        for child in self.frame.winfo_children():
            child.grid_configure(padx = 3, pady = 3)

    def record(self):
        self.expense = Expense(self.date, self.amount, self.perGallon, self.location, self.details)

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    root.title("Lyft Recordkeeper")
    app = MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()