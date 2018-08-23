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
print("Average Change: $" + str(round(avg_change,2)))
print("Greatest Increase in Profits: " + greatest_date + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + worst_date + " ($" + str(greatest_decrease) + ")")

#Exporing to .txt file
output = open("output.txt", "w")
line1 = "Financial Analysis"
line2 = "---------------------"
line3 = "Total Months: " + str(total_months)
line4 = "Total: $" + str(total_pl)
line5 = "Average Change: $" + str(round(avg_change,2))
line6 = "Greatest Increase in Profits: " + greatest_date + " ($" + str(greatest_increase) + ")"
line7 = "Greatest Decrease in Profits: " + worst_date + " ($" + str(greatest_decrease) + ")"
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))