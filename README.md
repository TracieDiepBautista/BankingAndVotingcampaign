# Python_my_challenge
Py_Poll works:
import os
import csv

# Set path for file
csvpath = os.path.join("Resources","election_data.csv")

# Open the CSV
with open(csvpath) as calculation:
    Voting= csv.reader(calculation, delimiter=",")
    header=next(Voting)
    #Assign the variables
    Vote_count = []
    for x in Voting:
        Voter_ID= x[0]
        county = x[1]
        Candidates = x[2]
        Vote_count.append(Voter_ID)
    number_of_votes = len(Vote_count)
    print(f"There are totally {number_of_votes} votes counted.")
    
  
