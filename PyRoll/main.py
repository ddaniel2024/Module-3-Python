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

    for candidate in candidates:
        candidate_votes = votes[candidates.index(candidate)]
        pc_votes = round(candidate_votes / total_votes *100,3)
        print(f'{candidate}: {pc_votes}% ({candidate_votes})')
    print("-------------------------------------------------")