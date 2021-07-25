from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas import DataFrame
import numpy as np

def table(table):
    html_text = requests.get(table).text
    soup = BeautifulSoup(html_text, 'lxml')

    # Grabs the first table for table1 and last table for table2 (only 2 tables)
    table1 = soup.find('table')
    table2 = soup.find_all('table')[-1]
    df = DataFrame()

    # Grabs the elemnts in the first row/columns for df
    column = []
    column_soup = table1.thead.tr.find_all('th')
    for items in column_soup:
        column.append(items.text)

    # Saves the first vertical column to index for df
    index = []
    index_soup = table1.tbody.find_all('th') + table2.tbody.find_all('th')
    for items in index_soup:
        index.append(items.text)

    df = DataFrame( columns=[column], index=[index])

    # Save all the values in the table that arent an index or row
    values = []
    values_soup = table1.tbody.find_all('td') + table2.tbody.find_all('td')
    for items in values_soup:
        values.append(items.text)
    # Reshapes list from (684, 1) to (76, 9)
    values = np.reshape(values, [76, 9])

    return DataFrame(values, columns=[column], index=[index])