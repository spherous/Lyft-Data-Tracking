from tkinter import *
from Expense import *

ENTRYBOXWIDTH = 12
BACKGROUND_COLOR = "#171717"
FOREGROUND_COLOR = "#E6E6E6"

root = Tk()

root.title("Lyft Recordkeeper")

mainframe = Frame(root)
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))

mainframe["bg"] = BACKGROUND_COLOR

root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

#----------DATE----------#
date = StringVar()
#Label
dateLabel = Label(mainframe, text="Date", bg = BACKGROUND_COLOR, fg = FOREGROUND_COLOR)
dateLabel.grid(column = 1, row = 1)
#Entry Box
dateEntryBox = Entry(mainframe, width = ENTRYBOXWIDTH, textvariable = date)
dateEntryBox.grid(column = 1, row = 2)

#----------AMOUNT----------#
amount = StringVar()
#Label
amountLabel = Label(mainframe, text="Amount", bg = BACKGROUND_COLOR, fg = FOREGROUND_COLOR)
amountLabel.grid(column = 2, row = 1)
#Entry Box
amountEntryBox = Entry(mainframe, width = ENTRYBOXWIDTH, textvariable = amount)
amountEntryBox.grid(column = 2, row = 2)

#----------PERGALLON----------#
perGallon = StringVar()
#Label
perGallonLabel = Label(mainframe, text="Per Gallon", bg = BACKGROUND_COLOR, fg = FOREGROUND_COLOR)
perGallonLabel.grid(column = 3, row = 1)
#Entry Box
perGallonEntryBox = Entry(mainframe, width = ENTRYBOXWIDTH, textvariable = perGallon)
perGallonEntryBox.grid(column = 3, row = 2)

#----------LOCATION----------#
location = StringVar()
#Label
locationLabel = Label(mainframe, text="Location", bg = BACKGROUND_COLOR, fg = FOREGROUND_COLOR)
locationLabel.grid(column = 4, row = 1)
#Entry Box
locationEntryBox = Entry(mainframe, width = ENTRYBOXWIDTH, textvariable = location)
locationEntryBox.grid(column = 4, row = 2)

#----------DETAILS----------#
details = StringVar()
#Label
detailsLabel = Label(mainframe, text="Details", bg = BACKGROUND_COLOR, fg = FOREGROUND_COLOR)
detailsLabel.grid(column = 1, row = 3)
#Entry Box
detailsEntryBox = Entry(mainframe, bd = 2, textvariable = details)
detailsEntryBox.grid(column = 2, row = 3, sticky = (W, E), columnspan = 3)

#----------RECORDBUTTON----------#
recordButton = Button(mainframe, text = "Record", command = "record")
recordButton.grid(column = 4, row = 4, sticky = (W, E))

#Add padding to all children of mainframe
for child in mainframe.winfo_children():
    child.grid_configure(padx = 3, pady = 3)

#Set focus on date entry box
dateEntryBox.focus()

root.mainloop()

def record(self):
    self.expense = Expense(date, amount, perGallon, location, details)
