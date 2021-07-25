from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
from pandas import DataFrame
import numpy as np
from tkinter import ttk, filedialog
import dfTable

root = Tk()
root.title('')
root.iconbitmap('')
root.geometry('800x600')
df = dfTable.table('https://www.benefits.va.gov/compensation/rates-index.asp')

# Create Frame
new_frame = Frame(root)
new_frame.pack(pady=20)

# Creates a treeview
my_tree = ttk.Treeview(new_frame)
my_tree["column"] = list(df.columns)
my_tree["show"] = list(df.index)

for column in my_tree['column']:
    my_tree.heading(column, text=column)

for index in my_tree['show']:
    my_tree.index(index, text=index)

df_rows = df.to_numpy().tolist()
for row in df_rows:
    my_tree.inser("", "end", values=row)

my_tree.pack()

root.mainloop()