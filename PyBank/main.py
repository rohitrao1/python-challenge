#Importing the necessary modules/libraries
import os
import csv

#Creating an object out of the CSV file
budget_data = os.path.join("budget_data.csv")

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
        #Average change in "Profit/Losses between months over entire period"
        #Greatest increase in profits 
        #Greatest decrease in profits 
        

