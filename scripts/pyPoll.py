# Dependancies
import csv
import os
import collections

voterFileInput = input("What is the name of your file? (include extension) : ")

# Define file path
csvPath = os.path.join('raw_data', voterFileInput)
#csvPath = os.path.join('raw_data', 'election_data_2.csv')


# Open file
with open(csvPath, newline = '') as csvFile:

# Define reader
    csvReader = csv.reader(csvFile, delimiter = ',')
#Skip the header
    next(csvReader, None)

#Define variables
    totalVotes = 0
    winnerName = ""
    highVote = 0
    percentVote = 0.0

# create collector to aggregate data    
    cntVotes = collections.Counter()
    for votes in csvReader:
        cntVotes[votes[2]] += 1

# Get the totals votes and winner from the results
for name, number in cntVotes.items():
    if totalVotes == 0:
        winnerName = name
        highVote = number
    elif number > highVote:
        winnerName = name
        highVote = number
    totalVotes = totalVotes + number
    

# Print to Terminal
print(f"   ")
print(f"-----------------------------------------")
print(f"            Election Results             ")
print(f"-----------------------------------------")
print(f"Total Votes: {totalVotes}")
print(f"-----------------------------------------")
for name, number in cntVotes.items():
    percentVote = round((number/totalVotes),2)
    print(f"{name}:  {percentVote}%  -  {number}")
print(f"-----------------------------------------")
print(f"Winner: {winnerName}")
print(f"-----------------------------------------")
    

 
# Setup Output file name
parseFileName = voterFileInput.split(".")
voterFileOutput = parseFileName[0] + ".txt"

# Write to file
file = open(voterFileOutput,"w") 

file.write(f"\n   ")
file.write(f"\n-----------------------------------------")
file.write(f"\n            Election Results             ")
file.write(f"\n-----------------------------------------")
file.write(f"\nTotal Votes: {totalVotes}")
file.write(f"\n-----------------------------------------")
for name, number in cntVotes.items():
    percentVote = round((number/totalVotes),2)
    file.write(f"\n{name}:  {percentVote}%  -  {number}")
file.write(f"\n-----------------------------------------")
file.write(f"\nWinner: {winnerName}")
file.write(f"\n-----------------------------------------")

file.close() 