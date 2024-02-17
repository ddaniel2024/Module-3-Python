import os

import csv

csvpath =  os.path.join('c:/Users/danie/Documents/Module3 Python/Module-3-Python/PyRoll/Resources/election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    row_count = 0
    candidates=[]
    votes=[]

    for row in csvreader:
        row_count = row_count + 1
        
        if row[2] not in candidates:
            candidates.append(row[2])
            votes.append(0)
        
        candidate_index = candidates.index(row[2])
        votes[int(candidate_index)] +=1

    print(f'Total Votes: {row_count}')

    print(candidates)
       
    print(votes)