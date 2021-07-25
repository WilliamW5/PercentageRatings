from tkinter import *
from PIL import ImageTk, Image
from numpy.core.fromnumeric import resize
import pandas as pd
from pandas import DataFrame
import numpy as np
from tkinter import ttk, filedialog
from pandastable import Table, TableModel
import dfTable

# Logic: get first split from textfield.
# Go to index location, then column name
# New x
# Go to new index location, then column name
def get_rating():
    # Turns text_field into list
    rating_list = text_field.get().split(',')

    # Assigns the first value as the new_rating, then pop off list
    new_rating = rating_list[0]
    rating_list.pop(0)
    
    # For each addition rating after the initial, it will pull the new rating
    for rating in rating_list:
        new_rating = df.loc[new_rating, rating].values[0]
        print(new_rating)
    print(f"Your final rating is {int(new_rating)}")
    final_rating = int(new_rating)
    table.setSelectedRow(final_rating - 19)
    
    final_rating_string = str(f"Your new rating is {final_rating}%, which is rounded to {round(final_rating, -1)}%")
    final_rating_label = Label(item_frame, text=final_rating_string)
    final_rating_label.grid(row=2, column=0)
    

root = Tk()
root.title('')
root.iconbitmap('')
root.geometry('800x600')
# Incase the link breaks, I have attached a file in webpage, that the same 2 tables exist
# with open('webpage/table.html', 'r') as html_file:    # Then send html_file to dfTable.table
df = dfTable.table('https://www.benefits.va.gov/compensation/rates-index.asp')

# Create Frames
df_frame = Frame(root)
df_frame.pack(fill='both', expand=True)
item_frame = Frame(root)
item_frame.pack(fill='both', expand=True)

# Create a table from df
table = Table(df_frame, dataframe=df, showstatusbar=True, showtoolbar=True)
table.showIndex()
table.show()

# Creates the label, entry, and button
label = Label(item_frame, text="Enter your ratings, seperated by a comma")
label.grid(row=0, column=0)
text_field = Entry(item_frame, width=40, bg="#ffffff", fg="#000000", borderwidth=3)
text_field.grid(row=1, column=0)
button = Button(item_frame, text="submit", command=get_rating)
button.grid(row=1, column=2)

root.mainloop()
