#Importing the necessary modules/libraries
import os
import csv

#Creating an object out of the CSV file
budget_data = os.path.join("budget_data.csv")

total_months = 0
total_pl = 0
value = 0
change = 0
profits = []

#Opening and reading the CSV file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Reading the header row
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
    
    #Going through each row of data after the header
    for row in csvreader:
        '''To Do: 
        1. Create a list to capture all changes
        2. Find the max increase & max decrease 
        3. Return values based on the indexes of 
        '''
        # Calculate the change, then add it to list of changes
        change = row[1]-value
        profits.append(change)
        value = row[1]
        
        #Total number of months
        total_months += 1

        #Total net amount of "Profit/Losses over entire period"
        total_pl = total_pl + int(row[1])

    #Greatest increase in profits
    greatest_increase = max(profits)

    #Greatest decrease (lowest increase) in profits 
    greatest_decrease = min(profits)

    #Average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits)/len(profits)

#Displaying information
print("Financial Analysis")
print("---------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_pl))
print("Average Change: $" + str(avg_change))
print("Greatest Increase in Profits: ")
print("Greatest Decrease in Profits: ")

        

