#PyPoll:

#In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

#You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:

#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

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

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Basics: connect with the data and look at the headers
import os
import csv

# Path to collect data from the CSV file
election_data = os.path.join('election_data.csv')
with open(election_data) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row (to get an idea of where the data is located)
    # I will delete this line from the code later as it isn't required for the final result.
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# *** A complete list of candidates who received votes ***
# identify all unique values in the election_data[2] position as I want to get a list of all the names
# refferenced: https://www.pythonpool.com/python-count-unique-values-in-list/

    list_of_candidates = []
    count = 0
    for row in csvreader:
        if row[2] not in list_of_candidates:
            count = count + 1
            list_of_candidates.append(row[2])
    
    # I will delete this line from the code later as it isn't required for the final result.
    print(list_of_candidates)

    # *** The total number of votes each candidate won ***
    # ["Khan", "Correy", "Li", "O'Tooley"] I want to make each name a variable and start a count on it.
    # FIXED THE indent issue, my issue NOW is the vote count is coming back as 0.
    #CSV Header: ['Voter ID', 'County', 'Candidate']
    #['Khan', 'Correy', 'Li', "O'Tooley"]
    #Khan: 0    
    #Correy: 0  
    #Li: 0      
    #O Tooley: 0
    #3521002

    vote_count_for_khan = [0]
    vote_count_for_correy = [0]
    vote_count_for_li = [0]
    vote_count_for_otooley = [0]

    for row in csvreader:

        if row[2] == "Khan":
            vote_count_for_khan += 1
        elif row[2] == "Correy":
            vote_count_for_correy += 1
        elif row[2] == "Li":
            vote_count_for_li += 1
        elif row[2] == "O'Tooley":
            vote_count_for_otooley += 1

        # Should I format this like the pybank task?
        # append first column (date) to months list
        #total_months.append(row[0])

    print(f"Khan: {vote_count_for_khan}")
    print(f"Correy: {vote_count_for_correy}")
    print(f"Li: {vote_count_for_li}")
    print(f"O Tooley: {vote_count_for_otooley}")               

# *** The total number of votes cast ***
# FYI the answer is 3521002, and I verified that by checking the data. It doesnt include the header as python starts as 0.

Total_Votes = 0

for row in open(election_data):

        Total_Votes += 1

print(Total_Votes)

#NOW I NEED TO: figure out which cxandidate had the highest vote count
#vote_count_for_khan = [0]
#vote_count_for_correy = [0]
#vote_count_for_li = [0]
#vote_count_for_otooley = [0]

#do i need this?
# Define the columns as per headers in the CSV file
VoterID = str(election_data[0])
County = str(election_data[1])
Candidate = str(election_data[2])

    # In addition, your final script should both: 
    # 1) print the analysis to the terminal.
    # 2) export a text file with the results.

    # 1) terminal
    print('__________________________________')
    print('                                  ')
    print('Election Results')
    print('- - - - - - - - - - - - - - - - - ')
    print(f'Total Votes: {Total_Votes}')
    print('- - - - - - - - - - - - - - - - - ')
    print(f'Khan: (100/{Total_Votes}*{vote_count_for_khan})% {({vote_count_for_khan})}')
    print(f'Correy: (100/{Total_Votes}*{vote_count_for_khan})% {({vote_count_for_khan})}')
    print(f'Li: (100/{Total_Votes}*{vote_count_for_khan})% {({vote_count_for_khan})}')
    print(f'O Tooley: (100/{Total_Votes}*{vote_count_for_khan})% {({vote_count_for_khan})}')
    print('- - - - - - - - - - - - - - - - - ')
    print(f'Winner: {STILL FIGURING THIS BIT OUT}')
    print('- - - - - - - - - - - - - - - - - ')

    # 2) export a text file
    election_data_output_csv = os.path.join('election_data_output.csv')
    with open(election_data_output_csv, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        
        csvwriter.writerow('Election Results')
        csvwriter.writerow('- - - - - - - - - - - - - - - - - ')
        csvwriter.writerow(f'Total Votes: {Total_Votes}')
        csvwriter.writerow('- - - - - - - - - - - - - - - - - ')
        csvwriter.writerow(f'Khan: (100/{Total_Votes}*{vote_count_for_khan})% {({vote_count_for_khan})}')
        csvwriter.writerow(f'Correy: (100/{Total_Votes}*{vote_count_for_khan})% {({vote_count_for_khan})}')
        csvwriter.writerow(f'Li: (100/{Total_Votes}*{vote_count_for_khan})% {({vote_count_for_khan})}')
        csvwriter.writerow(f'O Tooley: (100/{Total_Votes}*{vote_count_for_khan})% {({vote_count_for_khan})}')
        csvwriter.writerow('- - - - - - - - - - - - - - - - - ')
        csvwriter.writerow(f'Winner: {STILL FIGURING THIS BIT OUT}')

# LITERALY SO CLOSE I JUST NEED TO GET THESE DARN COMMAS OUT OF MY CSV FILE
# AND I ALSO NEED TO GET THE COUNT GOING PROPERLY, 
# THEN VERIFY THE QUICK MAFTHS TO GET VOTE PERCENTAGE, 
# THEN GET A FORMULA TO DISPLAY THE CANDIDATE WIKTH THE HIGHEST VOTE COUNT