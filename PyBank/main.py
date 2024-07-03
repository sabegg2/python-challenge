"""
Module 3 Challenge - PyBank 

Due: Jul 15, 2024 by 11:59pm

@author: Steph Abegg
"""

# modules
import csv
import os

# path to csv file
budget_data_csv = os.path.join("Resources", "budget_data.csv")

# lists to store data
date = []
profit_loss = []
changes = []

# open csv file
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # grab column headers
    header = []
    header = next(csvreader) # Date, Profit/Losses
    
    # read rows into lists
    for row in csvreader:
        # add date
        date.append(row[0])
        # add profit/loss
        profit_loss.append(int(row[1]))

# find monthly change, max increase, max decrease     
num_rows = len(date)
max_increase = 0
max_decrease = 0
max_increase_month = ""
max_decrease_month = ""
for i in range(1, num_rows):
    change = profit_loss[i]-profit_loss[i-1]
    changes.append(change)
    if change > max_increase:
        max_increase = change
        max_increase_month = date[i]
    if change < max_decrease:
        max_decrease = change
        max_decrease_month = date[i]

# compute desired output
month_count = len(set(date))
total_profit = sum(profit_loss)
avg_change = sum(changes)/(num_rows-1) 

# create list of output strings
L = [
     "Financial Analysis",
     "----------------------------", 
     f"Total Months: {month_count}",
     f"Total: ${total_profit:,}",
     f"Average Change: ${avg_change:,.2f}",
     f"Greatest Increase in Profits: {max_increase_month} (${max_increase:,})",
     f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease:,})"
     ]

# ouput to file
output_file = open("analysis/output_PyBank.txt","w")
output_file.writelines(line + '\n' for line in L)
output_file.close()

# print output as well
for row in L:
    print(row)