#PyPoll:
#In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
#You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:

#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#As an example, your analysis should look similar to the one below:
#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------


# Basics: import modules, set the variables
import os
import csv

total_votes = 0
vote_count_for_khan = 0
vote_count_for_correy = 0
vote_count_for_li = 0
vote_count_for_otooley = 0
list_of_candidates = []

# Path to collect data from the CSV file
election_data = os.path.join('election_data.csv')
with open(election_data) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row (to see column headers)
    # I will delete this line from the code later as it isn't required for the final result.
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        
        # *** The total number of votes cast ***
        total_votes += 1

        # *** A complete list of candidates who received votes ***
        if row[2] not in list_of_candidates:
            list_of_candidates.append(row[2])

        # *** The total number of votes each candidate won ***
        if row[2] == "Khan":
            vote_count_for_khan += 1
        elif row[2] == "Correy":
             vote_count_for_correy += 1
        elif row[2] == "Li":
            vote_count_for_li += 1
        elif row[2] == "O'Tooley":
            vote_count_for_otooley += 1

    # I will delete these lines from the code later as it isn't required for the final result.
    print(list_of_candidates)
    print(total_votes) 
    print(f"Khan: {vote_count_for_khan}")
    print(f"Correy: {vote_count_for_correy}")
    print(f"Li: {vote_count_for_li}")
    print(f"O Tooley: {vote_count_for_otooley}")         

# *** The winner of the election based on popular vote. ***
# which candidate had the highest vote count
# should i make vote_count_for_khan, correy, li & otooley a list, 
# then draw out the max value in that list?

# Khan: 2218231
# Correy: 704200
# Li: 492940
# O Tooley: 105630


# *** In addition, your final script should both: ***
# 1) print the analysis to the terminal.
# 2) export a text file with the results.

    # 1) terminal
print('__________________________________')
print('                                  ')
print('Election Results')
print('- - - - - - - - - - - - - - - - - ')
print(f'Total Votes: {total_votes}')
print('- - - - - - - - - - - - - - - - - ')
print(f'Khan: (100/{total_votes}*{vote_count_for_khan})% {({vote_count_for_khan})}')
print(f'Correy: (100/{total_votes}*{vote_count_for_khan})% {({vote_count_for_khan})}')
print(f'Li: (100/{total_votes}*{vote_count_for_khan})% {({vote_count_for_khan})}')
print(f'O Tooley: (100/{total_votes}*{vote_count_for_khan})% {({vote_count_for_khan})}')
print('- - - - - - - - - - - - - - - - - ')
#print(f'Winner: {STILL FIGURING THIS BIT OUT}')
print('- - - - - - - - - - - - - - - - - ')

    # 2) export a text file
election_data_output_csv = os.path.join('election_data_output.csv')
with open(election_data_output_csv, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
        
    csvwriter.writerow('Election Results')
    csvwriter.writerow('- - - - - - - - - - - - - - - - - ')
    csvwriter.writerow(f'Total Votes: {total_votes}')
    csvwriter.writerow('- - - - - - - - - - - - - - - - - ')
    csvwriter.writerow(f'Khan: (100/{total_votes}*{vote_count_for_khan})% {({vote_count_for_khan})}')
    csvwriter.writerow(f'Correy: (100/{total_votes}*{vote_count_for_khan})% {({vote_count_for_khan})}')
    csvwriter.writerow(f'Li: (100/{total_votes}*{vote_count_for_khan})% {({vote_count_for_khan})}')
    csvwriter.writerow(f'O Tooley: (100/{total_votes}*{vote_count_for_khan})% {({vote_count_for_khan})}')
    csvwriter.writerow('- - - - - - - - - - - - - - - - - ')
    #csvwriter.writerow(f'Winner: {STILL FIGURING THIS BIT OUT}')

# LITERALY SO CLOSE I JUST NEED TO GET THESE DARN COMMAS OUT OF MY CSV FILE
# THEN VERIFY THE QUICK MAFTHS TO GET VOTE PERCENTAGE, 
# THEN GET A FORMULA TO DISPLAY THE CANDIDATE WIKTH THE HIGHEST VOTE COUNT

#-----------------------------------------------------------------------------------------------------------
# References:

# 1 *** A complete list of candidates who received votes ***
# 1 identify all unique values in the election_data[2] position as I want to get a list of all the names
# 1 refferenced: https://www.pythonpool.com/python-count-unique-values-in-list/