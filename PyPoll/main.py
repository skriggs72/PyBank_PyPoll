# import modules
import os
import csv

# set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# set the output of the text  file
text_path = ('Analysis/election_analysis.txt')

# set variables
total_votes = 0
candidates = []
candidate_votes = []
winning_candidate = ""
winning_count = 0

# open the csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
# Count the number of votes in the dataset
        total_votes += 1
# Read name of candidate from column 3 of csv
        candidate_in = (row[2])
# If candidate already in list then locate the candidate by index # and increment the vote count by 1
        if candidate_in in candidates:
            candidate_index = candidates.index(candidate_in)
            candidate_votes[candidate_index] = candidate_votes[candidate_index] + 1
        else:
# If candidate was not found in candidates list then append to list and add 1 to vote count
            candidates.append(candidate_in)
            candidate_votes.append(1)

        
pct = []
max_votes = candidate_votes[0]
max_index = 0

for x in range(len(candidates)):
    vote_pct = round(candidate_votes[x]/total_votes*100, 2)
    pct.append(vote_pct)

    if candidate_votes[x] > max_votes:
        max_votes = candidate_votes[x]
        max_index = x
election_winner = candidates[max_index]


print('Election Results')
print('----------------------------')
print(f'Total Votes:  {total_votes}')
print('----------------------------')
for x in range(len(candidates)):
    print(f'{candidates[x]} : {pct[x]}% ({candidate_votes[x]})')
print('----------------------------')
print(f'Election Winner: {election_winner}')
print('----------------------------')

with open(text_path, 'w') as file:
    file.write('Election Results\n')
    file.write('-----------------------\n')
    file.write(f'Total Votes: {total_votes}\n')
    file.write('------------------------\n')
    for x in range(len(candidates)):
        file.write(f'{candidates[x]} : {pct[x]}% ({candidate_votes[x]})\n')
    file.write('-----------------------\n')
    file.write(f'Election Winner: {election_winner}\n')
    file.write('-----------------------\n')