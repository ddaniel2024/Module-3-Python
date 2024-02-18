#import os and csv modules
import os
import csv

#define csv path; relative location was not working so absolute location had to be used
csvpath =  os.path.join('c:/Users/danie/Documents/Module3 Python/Module-3-Python/PyRoll/Resources/election_data.csv')

#open csv file, state csv header
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #set total to 0, establish blank "candidates" and "total candidate votes" list (to calculate min and max values later)
    total_votes = 0
    candidates=[]
    total_candidate_votes=[]

    ##calculate total votes

    #iterate through all the rows
    for row in csvreader:
                
        #cumulate all the votes to get a total value
        total_votes = total_votes + 1
        
        #conditional to find unique candidates and add to "candidates" list
        if row[2] not in candidates:
            candidates.append(row[2])
            #for each unique candidate, a "0" is appended in the "total candidate votes" list (to calculate each candidates' votes later)
            total_candidate_votes.append(0)
        
        #each unique candidates' total votes is summed into the "total candidate votes" list
        candidate_index = int(candidates.index(row[2]))
        total_candidate_votes[candidate_index] +=1

#establish "max votes" list to hold the total votes of each candidate, and set max vote to 0
max_votes = []
max_vote = 0
#establish "results" list to hold results for printing later
results = []

#iterate through all candidates in "candidates" list and find their total votes by matching their index to the total votes in the "total candidate votes" list
for candidate in candidates:

    #calculate percentage of votes by dividing the candidate's total vote by the overall total votes. Set to 3 decimal places
    candidate_votes = total_candidate_votes[candidates.index(candidate)]
    pc_votes = round(candidate_votes / total_votes *100,3)

    #while iterating, append results to "results" list
    results.append(f'{candidate}: {pc_votes}% ({candidate_votes})')
    
    #while iterating, each candidate's total vote is appended to the "max votes" list. 
    max_votes.append(candidate_votes)
    #the maximum vote value is found and held using this conditional
    if candidate_votes > max_vote:
        max_vote = candidate_votes

#max vote is found by using the index of the max vote in the "max votes" list and applying it to the "candidates" list
max_votes_index = int(max_votes.index(max_vote))

#print results to terminal
print("Election Results")
print("-------------------------------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------------------------------")
for row in results:
    print(row)
print("-------------------------------------------------")
print(f'Winner: {candidates[max_votes_index]}')
print("-------------------------------------------------")

##export results to textfile in "analysis" folder

#define location for text file
text_filepath = os.path.join('C:/Users/danie/Documents/Module3 Python/Module-3-Python/PyRoll/analysis/analysis.txt')

#if there is no text file at the location, one is created. If there is already a text file, it is re-written
with open(text_filepath, "w") as file:
    
    file.write("Election Results\n")
    file.write("-------------------------------------------------\n")
    file.write(f'Total Votes: {total_votes}\n')
    file.write("-------------------------------------------------\n")
    for row in results:
        file.write(f'{row}\n')
    file.write("-------------------------------------------------\n")
    file.write(f'Winner: {candidates[max_votes_index]}\n')
    file.write("-------------------------------------------------\n")