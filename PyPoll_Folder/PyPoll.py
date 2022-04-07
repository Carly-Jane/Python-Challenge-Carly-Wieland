#PyPoll Task Instructions can be found in the read me file.

# let's go girls.

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
    
    # Test code point - no need to print, just a sanity check: 
    # Read the header row (to see column headers)
    # csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

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
                
    # Test code point - no need to print, just a sanity check: 
    # print(list_of_candidates)
    # print(total_votes) 
    # print(f"Khan: {vote_count_for_khan}")
    # print(f"Correy: {vote_count_for_correy}")
    # print(f"Li: {vote_count_for_li}")
    # print(f"O Tooley: {vote_count_for_otooley}")
            
# *** The winner of the election based on popular vote. ***
dictionary_of_vote_summary = {"Khan": vote_count_for_khan, "Correy": vote_count_for_correy, "Li": vote_count_for_li, "O'Tooley": vote_count_for_otooley}
election_winner = max(zip(dictionary_of_vote_summary.values(), dictionary_of_vote_summary.keys()))[1]

# *** The percentage of votes each candidate won ***
percentage_of_total_votes_khan = round((100/total_votes)*vote_count_for_khan,2)
percentage_of_total_votes_correy = round((100/total_votes)*vote_count_for_correy,2)
percentage_of_total_votes_li = round((100/total_votes)*vote_count_for_li,2)
percentage_of_total_votes_otooley = round((100/total_votes)*vote_count_for_otooley,2)

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
print(f'Khan: {percentage_of_total_votes_khan}% ({vote_count_for_khan})')
print(f'Correy: {percentage_of_total_votes_correy}% ({vote_count_for_correy})')
print(f'Li: {percentage_of_total_votes_li}% ({vote_count_for_li})')
print(f'O Tooley: {percentage_of_total_votes_otooley}% ({vote_count_for_otooley})')
print('- - - - - - - - - - - - - - - - - ')
print(f'Winner: {election_winner}')
print('- - - - - - - - - - - - - - - - - ')

    # 2) export a text file
election_data_output_csv = os.path.join('election_data_output.csv')
with open(election_data_output_csv, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
        
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['- - - - - - - - - - - - - - - - - '])
    csvwriter.writerow([(f'Total Votes: {total_votes}')])
    csvwriter.writerow(['- - - - - - - - - - - - - - - - - '])
    csvwriter.writerow([(f'Khan: {percentage_of_total_votes_khan}% ({vote_count_for_khan})')])
    csvwriter.writerow([(f'Correy: {percentage_of_total_votes_correy}% ({vote_count_for_correy})')])
    csvwriter.writerow([(f'Li: {percentage_of_total_votes_li}% ({vote_count_for_li})')])
    csvwriter.writerow([(f'O Tooley: {percentage_of_total_votes_otooley}% ({vote_count_for_otooley})')])
    csvwriter.writerow(['- - - - - - - - - - - - - - - - - '])
    csvwriter.writerow([f'Winner: {election_winner}'])
    csvwriter.writerow(['- - - - - - - - - - - - - - - - - '])


#-----------------------------------------------------------------------------------------------------------
# References:

# 1 *** A complete list of candidates who received votes ***
# 1 identify all unique values in the election_data[2] position as I want to get a list of all the names
# 1 refferenced: https://www.pythonpool.com/python-count-unique-values-in-list/