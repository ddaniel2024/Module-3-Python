import os

import csv

csvpath =  os.path.join('c:/Users/danie/Documents/Module3 Python/Module-3-Python/PyRoll/Resources/election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    total_votes = 0
    candidates=[]
    votes=[]

    for row in csvreader:
        total_votes = total_votes + 1
        
        if row[2] not in candidates:
            candidates.append(row[2])
            votes.append(0)
        
        candidate_index = int(candidates.index(row[2]))
        votes[candidate_index] +=1

print("Election Results")
print("-------------------------------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------------------------------")

max_votes = []
max_vote = 0

for candidate in candidates:

    candidate_votes = votes[candidates.index(candidate)]
    pc_votes = round(candidate_votes / total_votes *100,3)

    print(f'{candidate}: {pc_votes}% ({candidate_votes})')

    max_votes.append(candidate_votes)
    if candidate_votes > max_vote:
        max_vote = candidate_votes

print("-------------------------------------------------")

max_votes_index = int(max_votes.index(max_vote))

print(f'Winner: {candidates[max_votes_index]}')

print("-------------------------------------------------")