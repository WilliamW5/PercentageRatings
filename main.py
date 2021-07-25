from tkinter import *
from PIL import ImageTk, Image
from numpy.core.fromnumeric import resize
import pandas as pd
from pandas import DataFrame
import numpy as np
from tkinter import ttk, filedialog
from pandastable import Table, TableModel
import dfTable

def get_rating():
    # Turns text_field into list
    values = text_field.get().split(',')

    # Logic: get first split from textfield.
    # Go to index location, then column name
    # New x
    # Go to new index location, then column name
    print(df[values[0]][values[1]])
    print(values)
    return

root = Tk()
root.title('')
root.iconbitmap('')
root.geometry('800x600')
# Incase the link breaks, I have attached a file in webpage, that the same 2 tables exist
# with open('webpage/table.html', 'r') as html_file: # Then send to dfTable, just the html_file
df = dfTable.table('https://www.benefits.va.gov/compensation/rates-index.asp')

# Create Frame
new_frame = Frame(root)
new_frame.pack(fill='both', expand=True)

# Create a table from df
table = Table(new_frame, dataframe=df, showstatusbar=True, showtoolbar=True)
table.showIndex()
table.show()

# Creates the label, entry, and button
label = Label(root, text="Enter your ratings, seperated by a comma")
label.pack()
text_field = Entry(root, width=75, bg="#ffffff", fg="#000000", borderwidth=3)
text_field.pack()
button = Button(root, text="submit", command=get_rating)
button.pack()

root.mainloop()
