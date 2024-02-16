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
        candidates.append(row[2])

    for i in range(len(candidates)):
        if candidates[i] != candidates[i+1]:
            print(candidates[i])

    print(f'Total Votes: {row_count}')