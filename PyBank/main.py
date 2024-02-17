import os

import csv

csvpath = os.path.join('C:/Users/danie/Documents/Module3 Python/Module-3-Python/PyBank/Resources/budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    total = 0
    row_no = 0
    prices=[]
    dates=[]

    for row in csvreader:

        total = total + int(row[1])
        row_no = row_no +1

        prices.append(row[1])
        dates.append(row[0])

max_inc = 0
max_inc_month = 0
max_dec = 0  
max_dec_month = 0
changes=[]

for i in range(1,len(prices)):

    change = int(prices[i]) - int(prices[i-1])
    price_index = prices.index(prices[i])
    changes.append(change)

    if  change > max_inc:
        max_inc = change
        max_inc_month = dates[int(price_index)]
    if change < max_dec:
        max_dec = change
        max_dec_month = dates[int(price_index)]

total_changes = 0

for i in range(0,len(changes)):
    total_changes = total_changes + changes[i]

average_change = round(total_changes / len(changes),2)

print("Financial Analysis")
print("-------------------------------------------------")
print(f'Total Months: {row_no}')
print(f'Total: ${total}')  
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in in Profits: {max_inc_month} (${max_inc})')
print(f'Greatest Decrease in Profits: {max_dec_month} (${max_dec})')
print("-------------------------------------------------")

file = 'C:/Users/danie/Documents/Module3 Python/Module-3-Python/PyBank/output.txt'

with open("analysis.txt", "w") as file:
    
    file.write("Financial Analysis")
    file.write("-------------------------------------------------")
    file.write(f'Total Months: {row_no}')
    file.write(f'Total: ${total}')  
    file.write(f'Average Change: ${average_change}')
    file.write(f'Greatest Increase in in Profits: {max_inc_month} (${max_inc})')
    file.write(f'Greatest Decrease in Profits: {max_dec_month} (${max_dec})')
    file.write("-------------------------------------------------")