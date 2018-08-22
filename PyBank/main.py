#Importing the necessary modules/libraries
import os
import csv

#Creating an object out of the CSV file
budget_data = os.path.join("budget_data.csv")

total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

#Opening and reading the CSV file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Reading the header row
    csv_header = next(csvreader)
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])
    # print(f"Header: {csv_header}")
    
    #Going through each row of data after the header
    for row in csvreader:
        '''To Do: 
        1. Create a list to capture all changes
        2. Find the max increase & max decrease 
        3. Return values based on the indexes of 
        '''
        # Keeping track of the dates
        dates.append(row[0])
        
        # Calculate the change, then add it to list of changes
        change = int(row[1])-value
        print(change)
        profits.append(change)
        value = int(row[1])
        
        #Total number of months
        total_months += 1

        #Total net amount of "Profit/Losses over entire period"
        total_pl = total_pl + int(row[1])

    #Greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #Greatest decrease (lowest increase) in profits 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    #Average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits)/len(profits)

#Displaying information
print("Financial Analysis")
print("---------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_pl))
print("Average Change: $" + str(avg_change))
print("Greatest Increase in Profits: " + greatest_date + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + worst_date + " ($" + str(greatest_decrease) + ")")

'''What's Left: 
1. Fixing "Average Change"
2. Pulling/pushing to Github (Save this file to desktop + Pull + Copy-paste code + Push)
3. Exporting to txt file
'''

