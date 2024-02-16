import os

import csv

csvpath = os.path.join('C:/Users/danie/Documents/Module3 Python/Module-3-Python/PyBank/Resources/budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f'CSV Header:{csv_header}')

    total = 0
    row_no = 0

    for row in csvreader:
        print(row)

        total = total + int(row[1])
        row_no = row_no +1

print("Financial Analysis")
print("-------------------------------------------------")
print(f'Total Months: {row_no}')
print(f'Total: ${total}')   
    
