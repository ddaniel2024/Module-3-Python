#import os and csv modules
import os
import csv

#define csv path; absolute location was used instead of relative
csvpath = os.path.join('C:/Users/danie/Documents/Module-3-Python/Module-3-Python/PyBank/Resources/budget_data.csv')

#open csv file, state csv header
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #set total and row number to 0, establish blank "prices" and "months" list (to calculate min and max values later)
    total = 0
    row_no = 0
    prices=[]
    months=[]

    ##calculate total months and total price
    #iterate through all the rows
    for row in csvreader:

        #cumulate all the prices to get a total value, and keep track of the row number to find total months
        total = total + int(row[1])
        row_no = row_no +1

        #while iterating, append prices to the "prices" list, and append months to the "months" list 
        prices.append(row[1])
        months.append(row[0])

##calculate greatest increase and decrease
#set max and min increases to 0, set max and min months to 0, establish blank "changes" list (to use later to calculate average change)
max_inc = 0
max_inc_month = 0
max_dec = 0  
max_dec_month = 0
changes=[]

#iterate through newly created "prices" list (starting at the second value to avoid index error)
for i in range(1,len(prices)):

    #calculate change between price value and the price value before it. Append it to the blank "changes" list
    change = int(prices[i]) - int(prices[i-1])
    changes.append(change)

    #conditional to calculate min/max values. index value of price values in "prices" list is used to determine min/max months from "months" list
    #if the change is greater than the previous change, previous change is overwritten, and new change is stored
    price_index = prices.index(prices[i])
    if  change > max_inc:
        max_inc = change
        max_inc_month = months[int(price_index)]
    #if the change is lower than the previous change, previous change is overwritten, and new change is stored
    if change < max_dec:
        max_dec = change
        max_dec_month = months[int(price_index)]

##calculate average change
#set sum of changes to 0
sum_of_changes = 0

#iterate through "changes" list and sum all the change values
for i in range(0,len(changes)):
    sum_of_changes = sum_of_changes + changes[i]

#calculate average change by dividing sum of change values by number of values. Round the result to 2 decimal places
average_change = round(sum_of_changes / len(changes),2)

#print results to terminal
print("Financial Analysis")
print("-------------------------------------------------")
print(f'Total Months: {row_no}')
print(f'Total: ${total}')  
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in in Profits: {max_inc_month} (${max_inc})')
print(f'Greatest Decrease in Profits: {max_dec_month} (${max_dec})')
print("-------------------------------------------------")

##export results to textfile in "analysis" folder
#define location for text file
text_filepath = os.path.join('C:/Users/danie/Documents/Module-3-Python/Module-3-Python/PyBank/analysis/pybank_analysis.txt')

#if there is no text file at the location, one is created. If there is already a text file, it is re-written
with open(text_filepath, "w") as file:
    
    file.write("Financial Analysis\n")
    file.write("-------------------------------------------------\n")
    file.write(f'Total Months: {row_no}\n')
    file.write(f'Total: ${total}\n')  
    file.write(f'Average Change: ${average_change}\n')
    file.write(f'Greatest Increase in Profits: {max_inc_month} (${max_inc})\n')
    file.write(f'Greatest Decrease in Profits: {max_dec_month} (${max_dec})\n')
    file.write("-------------------------------------------------\n")