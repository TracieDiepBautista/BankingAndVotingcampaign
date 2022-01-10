#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import csv


# In[5]:


# Set path for file
csvpath = os.path.join("Resources","budget_data.csv")

# Open the CSV
with open(csvpath) as cal:
    Profit_Loss= csv.reader(cal, delimiter=",")
    header=next(Profit_Loss)
    #Assign the variables
    months =[]
    
#call the variables available in the data file's row
    for row in Profit_Loss:
        the_month=row[0]
        months.append(the_month)
    count_of_month = len(months)
    print(f" the total months is {count_of_month}")


# In[6]:


csvpath = os.path.join("Resources","budget_data.csv")
# Read the csv and convert it into a list of dictionaries
total_months=0
total_net=0
net_change_list=[]
month_of_change=[]
# Open the CSV
with open(csvpath) as cal:
    profit_loss= csv.reader(cal, delimiter=",")

    # Read the header row
    header = next(profit_loss)

    # Extract first row to avoid appending to net_change_list
    first_row = next(profit_loss)
    total_months += 1 #to ask the computer to add the current row when calculate the next row
    total_net += int(first_row[1]) #adds the current net to the total net, whether positive or negative
    prev_net = int(first_row[1]) #tells python to go and read the previous row 

    for row in profit_loss:

        # Track the total
        total_months += 1
        #print(total_months)
        total_net = total_net + int(row[1]) #find the total during entire period
        #print(total_net)

        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]
print(f"The net total amount of profit | loss over the entire period is: ${total_net}")


# In[7]:


#find the greatest increase in profits over the entire period
increase = max(net_change_list)
print(increase)


# In[8]:


#find the greatest decrease in profits over the entire period
decrease = min(net_change_list)
print(decrease)


# In[9]:


def Average(net_change_list):
    return sum(net_change_list) / len(net_change_list)
average = str(round(Average(net_change_list),2))
print("the average of net change is: " + average)


# In[10]:


#print the outcomes as format
Financial_Analysis = print(f"Finacial Analysis:\n"
                           f"--------------------\n"
    f"Total Months: {total_months}\n"
    f"Total change: {total_net}\n"
    f"Average change: ${average}\n"
    f"Greatest increase in Profit: ${increase}\n"
    f"Greatest decrease in Profit|Loss: ${decrease}\n")


# In[26]:


# write to csv file
output_path = os.path.join("output", "analysis.csv")
with open(output_path, 'w', newline='') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=' ')

    # Write the first row (column headers)
    csvwriter.writerow("text:")

    # Write the second row
    csvwriter.writerow(["Financial Analysis"])
    
    #next rows
    csvwriter.writerow(["-------------------"])
    csvwriter.writerow(["Total Months:" , [total_months]])
    csvwriter.writerow(["Total change: ", [total_net]])
    csvwriter.writerow(["Average change: ", [average]])
    csvwriter.writerow(["Greatest increase in Profit: " "$",[increase]])
    csvwriter.writerow(["Greatest decrease in Profit|Loss: " "$",[decrease]])

