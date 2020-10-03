# -*- coding: UTF-8 -*-

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('')
sales_filepath = Path('')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list
# Set the file path
csvpath = Path('menu_data.csv')

with open(csvpath, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    menu_header = next(csvreader)
    
    for row in csvreader:
        menu.append(row)

# @TODO: Read in the sales data into the sales list
csvpath = Path('sales_data.csv')

with open(csvpath, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    sales_header = next(csvreader)

    for row in csvreader:
        sales.append(row)

# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object
for sale in sales:

    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
    quantity = int(sale[3])
    sale_item = str(sale[4])

    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    if not(sale_item in report):
        report[sale_item] = {'01-count': 0,
                             '02-revenue': 0,
                             '03-cogs': 0,
                             '04-profit': 0}

    # @TODO: For every row in our sales data, loop over the menu records to determine a match
    for record in menu:

        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables
        menu_item = str(record[0])
        price = float(record[3])
        cost = float(record[4])
        # @TODO: Calculate profit of each item in the menu data
        profit = price - cost

        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        if menu_item == sale_item:

            # @TODO: Print out matching menu data
            # No printinng within nested for loops: too much output

            # @TODO: Cumulatively add up the metrics for each item key
            report[sale_item]["01-count"] += quantity
            report[sale_item]["02-revenue"] += price * quantity
            report[sale_item]["03-cogs"] += cost * quantity
            report[sale_item]["04-profit"] += profit * quantity

        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match
        '''
        else:
            print(f"{sale_item} does not equal {menu_item}! NO MATCH!")

        '''
    # @TODO: Increment the row counter by 1
    row_count += 1

# @TODO: Print total number of records in sales data
print(f"Amount of sales: {row_count}")

# @TODO: Write out report to a text file (won't appear on the command line output)
output_path = 'output.txt'

with open(output_path, 'w') as file:
        # Write daily_average to the output file, convert to string
        file.write(f"{report}")