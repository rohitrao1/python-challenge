#Importing the necessary modules/libraries
import os
import csv

#Creating an object out of the CSV file
budget_data = os.path.join("budget_data.csv")

total_months = 0
total_pl = 0
changes = [0]
avg_change = 0
greatest_increase = 0
greatest_decrease = 0

#Opening and reading the CSV file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Reading the header row
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
    
    #Going through each row of data after the header
    for row in csvreader:
        
        #Total number of months
        #Total net amount of "Profit/Losses over entire period"
        total_pl = total_pl + int(row[1])

        #Average change in "Profit/Losses between months over entire period"
        
        #Greatest increase in profits 
        #Greatest decrease in profits 

#Displaying information
print("Financial Analysis")
print("---------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_pl))
print("Average Change: $" + str(avg_change))
print("Greatest Increase in Profits: ")
print("Greatest Decrease in Profits: ")

        

