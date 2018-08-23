import os
import csv

election_data = os.path.join("election_data.csv")

# A list to capture the names of candidates
candidates = []

# A list to capture the number of votes each candidate receives
num_votes = []

# A list to capture the percentage of total votes each candidate garners 
percent_votes = []

# A counter for the total number of votes 
total_votes = 0

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        # Add to our vote-counter 
        total_votes += 1 

        '''
        If the candidate is not on our list, add his/her name to our list, along with 
        a vote in his/her name.
        If he/she is already on our list, we will simply add a vote in his/her
        name 
        '''
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
    
    # Add to percent_votes list 
    percent_votes = num_votes
    percent_votes = [(num_votes[i]/total_votes * 100) for i in num_votes]

    print(candidates)
    print(num_votes)
    print(percent_votes)

    '''
    
    # List of "unique" candidates 
    candidates = list(set(candidates))
    print(candidates)

    #List to keep track of votes
    num_votes = [0 for vote in candidates]
    print(num_votes)

    # If a new candidate is added to CSV file 
    for row in csvreader:
        if row[2] in candidates:
            index = candidates.index(row[2])
            num_votes[index] += 1
        else:
            candidates.append(row[2])
            num_votes.append(0)
            index = candidates.index(row[2])
            num_votes[index] += 1

'''
    
        
    '''
    #Dictionary of candidates, their respective number of votes, and % votes 
    for candidate in candidates:
        voting_dict[candidate] = [0,0.0] 
        
    print(voting_dict)

    for row in csvreader:
        for votes in voting_dict:
            if voting_dict[votes] == row[2]:
                voting_dict[votes][0] += 1
    '''
    
                


    # print(voting_dict) 


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
#Method 3 --> Manual calculations 

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
