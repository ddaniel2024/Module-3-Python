import os

import csv

csvpath =  os.path.join('c:/Users/danie/Documents/Module3 Python/Module-3-Python/PyRoll/Resources/election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    row_count = 0
    candidates=[]

    for row in csvreader:
        row_count = row_count + 1
        
        if row[2] not in candidates:
            candidates.append(row[2])
        
    print(f'Total Votes: {row_count}')

    print(candidates)

    for candidate in candidates:
        votes = 0
        for row in csvreader:
            if row[2] == candidate:
                votes = votes + 1
        print(votes)