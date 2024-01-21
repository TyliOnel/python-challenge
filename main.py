# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

# Find csv file for the project
import os
import csv

# import as collection; method used for bigger list data
# use counter; unordered data with name and number that are connected
import collections
from collections import Counter

# Define variables in PyPoll csv - what are we solving for
candidates = []
votes_per_candidate = []

# Change directory to match the current python code
os.chdir(os.path.dirname(__file__))

# make sure CSV files have the correct path to the CSV file
election_data_csv = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(election_data_csv, newline="") as csvfile:

    #tell python that csv data is differentiated by a comma (delimiter)
    csv_reader = csv.reader(csvfile, delimiter=",")

     # tell python there is a header - read the header (Voter ID, Country, Candidate)
    csv_header = next(csvfile)

    # Read rows after the header
    for row in csv_reader:

        candidates.append(row[2])

    # Use sorted in order to arrange the data in assending order
    sorted_list = sorted(candidates)
    
    # find the most common outcomes by arranging list
    list_aranged = sorted_list

    # count all votes per candidate and arrange in most common outcome order - then add to the list
    candidate_count = Counter (list_aranged) 
    votes_per_candidate.append(candidate_count.most_common())

    # find three candidates with most votes and convert to percentage
    for item in votes_per_candidate:
       
        first = format((item[0][1])*100/(sum(candidate_count.values())),'.3f')
        second = format((item[1][1])*100/(sum(candidate_count.values())),'.3f')
        third = format((item[2][1])*100/(sum(candidate_count.values())),'.3f')
    
# show results of the challenge
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {sum(candidate_count.values())}")
print("-------------------------")
print(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})")
print(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})")
print(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})")
print("-------------------------")
print(f"Winner:  {votes_per_candidate[0][0][0]}")
print("-------------------------")

# create new .txt document with results
poll_file = os.path.join("Output", "election_data.txt")
with open("poll_file", "w") as text:

    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write(f"Total Votes:  {sum(candidate_count.values())}\n")
    text.write("-------------------------\n")
    text.write(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})\n")
    text.write(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})\n")
    text.write(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})\n")
    text.write("-------------------------\n")
    text.write(f"Winner:  {votes_per_candidate[0][0][0]}\n")
    text.write("-------------------------\n")    
   
