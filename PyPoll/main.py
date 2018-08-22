import os
import csv

election_data = os.path.join("election_data.csv")

# Method 1 --> Automated (and dynamic)
total_votes = 0
candidates = []
votes = []
voting_dict = {}

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvreader)
    
    for row in csvreader:
        candidates.append(row[2])

    #List of unique values (in case candidates change)
    candidates = list(set(candidates))
    #Creating a dictionary
    for candidate in candidates:
        voting_dict[candidate] = [0,0.0]

    #Adds up number of votes for each candidate, then adds to dictionary
    for row in csvreader:
        for votes in voting_dict:
            if votes == row[2]:
                voting_dict[votes][0] += 1

    print(voting_dict)

    
'''
#Method 2 --> Dictionaries
total_votes = 0
voting_dict = {"Khan":[0,0.0], "Correy":[0,0.0], "Li": [0,0.0], "O-Tooley":[0,0.0]}

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvreader)
    
    for row in csvreader:
        total_votes += 1
        if row[2] == "Khan":
            voting_dict["Khan"][0] += 1
        elif row[2] == "Correy":
            voting_dict["Correy"][0] += 1
        elif row[2] == "Li":
            voting_dict["Li"][0] += 1
        else:
            voting_dict["O-Tooley"][0] += 1

voting_dict["Khan"][1] = voting_dict["Khan"][0]/total_votes
voting_dict["Correy"][1] = voting_dict["Correy"][0]/total_votes
voting_dict["Li"][1] = voting_dict["Li"][0]/total_votes
voting_dict["O-Tooley"][1] = voting_dict["O-Tooley"][0]/total_votes

print(voting_dict)
'''

'''
Things To Do:
1. Should the names of the candidates (keys of the dictionary) be extracted 
automatically?
2. Print & format output properly 
3. Export as .txt
4. "Verify" it works for other file (with a 0 output)
'''


'''
#Method 2 --> Manual calculations 

total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
percent_khan = 0.0
percent_correy = 0.0
percent_li = 0.0
percent_otooley = 0.0


with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvreader)
    for row in csvreader:
        total_votes += 1
        if row[2] == "Khan":
            khan_votes += 1
        elif row[2] == "Correy":
            correy_votes += 1
        elif row[2] == "Li":
            li_votes += 1
        else:
            otooley_votes += 1
    percent_khan = float(khan_votes/total_votes)
    percent_correy = float(correy_votes/total_votes)
    percent_li = float(li_votes/total_votes)
    percent_otooley = float(otooley_votes/total_votes)

print(total_votes)
print(khan_votes)
print(percent_khan)
'''
