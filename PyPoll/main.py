#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os
import csv


# In[8]:


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
    


# In[9]:


#find the complete candidate_names who received votes
    #to find the full list of names in the file first, then find out the complete_candidates without duplicating

# Open the CSV
with open(csvpath) as calculation:
    Voting= csv.reader(calculation, delimiter=",")
    header=next(Voting)
    
    #Assign the variables    
    
    candidate_name = []
    candidate_list = []
    
    #do loop to find list of candidate_name first
    for x in Voting:
        candidate = x[-1]
        candidate_list.append(candidate)
        if candidate not in candidate_name:
            candidate_name.append(candidate)
            print(candidate_name)


# In[10]:


number_of_candidate = len(candidate_name)
print(number_of_candidate)


# In[11]:


#find out how many votes each can. received by count the "candidate" column to see how many time repeated in name:

max = 0
winner = ""
for name in candidate_name:
    #print(name)
    Vote = candidate_list.count(name)
    #print(Vote)
    
    if Vote > max:
        max = Vote
        winner = name

    result = print(f"{name}: {round(Vote/number_of_votes*100)}%, ({Vote} votes)")      
print("-----------------")


# In[12]:


# Find the winner by max function
print(max,winner)


# In[19]:


# write to csv file
csv_path = os.path.join("Resources","election_data.csv")
with open(csv_path, 'w', newline='') as csvfile:
    
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow("Election Results:")

    # Write the second row
    csvwriter.writerow(["-----------------"])
    
    #next rows
    csvwriter.writerow(f"{name}: {round(Vote/number_of_votes*100)}%, ({Vote} votes)")
    csvwriter.writerow(["Winner: ", "Khan", "63%", max])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




