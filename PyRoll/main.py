#import os and csv modules
import os
import csv

#define csv path; absolute location was used
csvpath = os.path.join('c:/Users/danie/Documents/Module-3-Python/Module-3-Python/PyRoll/Resources/election_data.csv')

#open csv file, state csv header
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #set total to 0, establish blank dictionary
    total_votes = 0
    dict = {"Name" : [],
        "Votes" : [],
        "pc_vote" : []}

    #iterate through all the rows
    for row in csvreader:
                
        #cumulate all the votes to get a total value
        total_votes = total_votes + 1
        
        #conditional to find unique candidates and append to dictionary
        #for each unique candidate, a "0" is appended in the "votes" and "percentage votes" lists
        if row[2] not in dict["Name"]:
            dict["Name"].append(row[2])
            dict["Votes"].append(0)
            dict["pc_vote"].append(0)

        # for each unqiue candidate, add their votes as you iterate through the rows and add to the dictionary
        for candidate in dict["Name"]:

            candidate_index = dict["Name"].index(candidate)
            
            if row[2] == candidate:
                dict["Votes"][candidate_index] +=1
            
            #as you iterate through the rows, caluclate the percentage vote for each candidate and add to the dictionary
            #percentage vote is calculated by dividing the candidate's vote, dividing by the total number of votes, multiplying by 100, then rounding to 3 dp.
            pc_vote = round(dict["Votes"][candidate_index] / total_votes * 100, 3)
            dict["pc_vote"][candidate_index] = pc_vote
    
#winning candidate is found by using the index of the maximum vote in the "votes" list and applying it to the "name" list in the dictionary
max_vote = 0 
for i in range(len(dict["Votes"])):
    if dict["Votes"][i] > max_vote:
        max_vote = dict["Votes"][i]

max_vote_index = dict["Votes"].index(max_vote)
winner = dict["Name"][max_vote_index]

#print results to terminal
print("Election Results")
print("-------------------------------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------------------------------")
for i in range(len(dict)):
    print(f'{dict["Name"][i]}: {dict["pc_vote"][i]}% ({dict["Votes"][i]})')
print("-------------------------------------------------")
print(f'Winner: {winner}')

##export results to textfile in "analysis" folder
#define location for text file
text_filepath = os.path.join('C:/Users/danie/Documents/Module-3-Python/Module-3-Python/PyRoll/analysis/pyroll_analysis.txt')

#if there is no text file at the location, one is created. If there is already a text file, it is re-written
with open(text_filepath, "w") as file:

    file.write("Election Results\n")
    file.write("-------------------------------------------------\n")
    file.write(f'Total Votes: {total_votes}\n')
    file.write("-------------------------------------------------\n")
    for i in range(len(dict)):
        file.write(f'{dict["Name"][i]}: {dict["pc_vote"][i]}% ({dict["Votes"][i]})\n')
    file.write("-------------------------------------------------\n")
    file.write(f'Winner: {winner}\n')