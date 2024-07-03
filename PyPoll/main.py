"""
Module 3 Challenge - PyPoll 

Due: Jul 15, 2024 by 11:59pm

@author: Steph Abegg
"""

# modules
import csv
import os

# path to csv file
election_data_csv = os.path.join("Resources", "election_data.csv")

# list to store candidate votes
votes = []

# open csv file
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # grab column headers
    header = []
    header = next(csvreader) # Ballot ID, County, Candidate
    
    # read rows into lists
    # just need Candidate column - don't need Ballot ID or County in this analysis
    for row in csvreader:
        # add vote (i.e. candidate name)
        votes.append(row[2])

# compute total votes
total_votes = len(votes)

# get list of candidates
candidates = set(votes)

# get output summary for each candidate
num_candidates = len(candidates)
winner_votes = 0
winner = []
# create list of output strings
L = ["Election Results",
     "----------------------------", 
     f"Total Votes: {total_votes:,}",
     "----------------------------"] 
for candidate in candidates:
    # get number of votes for candidate
    num_candidate_votes = votes.count(candidate)
    # find winner
    if winner_votes < num_candidate_votes:
        winner_votes = num_candidate_votes
        winner = candidate
    # add candidate to list
    L = L + [f"{candidate}: {100*num_candidate_votes/total_votes:.3f}% ({num_candidate_votes:,})"]

# add winner to list
L = L + ["----------------------------", f"Winner: {winner}", "----------------------------"]

# ouput to file
output_file = open("analysis/output_PyPoll.txt","w")
output_file.writelines(line + '\n' for line in L)
output_file.close()

# print output as well
for row in L:
    print(row)