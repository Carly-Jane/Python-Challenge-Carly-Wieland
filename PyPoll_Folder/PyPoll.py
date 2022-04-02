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
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# *** SECOND TASK: A complete list of candidates who received votes ***
# okay so here I want to get a list of all the names
# identify all unique values in the election_data[2] position
# refferenced: https://www.pythonpool.com/python-count-unique-values-in-list/

    list_of_candidates = []

    count = 0

    for row in csvreader:

        if row[2] not in list_of_candidates:

            count = count + 1

            list_of_candidates.append(row[2])

print(list_of_candidates)

    # I may delete this line from the code later as it isn't required for the final result and it might make the results look messy.
    # I miss Pandas already

# Define the columns as per headers in the CSV file
VoterID = str(election_data[0])
County = str(election_data[1])
Candidate = str(election_data[2])


# *** FIRST TASK: The total number of votes cast ***
# Total Votes will be the variable name (as the instructions example indicates)
# FYI the answer is 3521002, andf i verified that by checking the data. It doesnt include the header as python starts as 0.

Total_Votes = 0

for row in open(election_data):

    Total_Votes += 1

print(Total_Votes)



# get candidate names, and hard code them

#




# then when I have those names, i want to make each name a variable and start a count on it.

# *********************************************************************************************************************************
# Below is code from class activities that I will use to create the final code for my homework

#udemy_csv = os.path.join("..", "Resources", "web_starter.csv")

# Lists to store data
#title = []
#price = []
#subscribers = []
#reviews = []
#review_percent = []
#length = []

# Use encoding for Windows
# with open(udemy_csv, newline='', encoding='utf-8') as csvfile:
#with open(udemy_csv, newline='') as csvfile:
    #csvreader = csv.reader(csvfile, delimiter=",")
    #for row in csvreader:
        # Add title
        #title.append(row[1])

        # Add price
        #price.append(row[4])

        # Add number of subscribers
        #subscribers.append(row[5])

        # Add amount of reviews
        #reviews.append(row[6])

        # Determine percent of review left to 2 decimal places
        #percent = round(int(row[6]) / int(row[5]), 2)
        #review_percent.append(percent)

        # Get length of the course to just a number
        #new_length = row[9].split(" ")
        #length.append(float(new_length[0]))

# Zip lists together
#cleaned_csv = zip(title, price, subscribers, reviews, review_percent, length)

# Set variable for output file
#output_file = os.path.join("web_final.csv")

#  Open the output file
#with open(output_file, "w", newline="") as datafile:
    #writer = csv.writer(datafile)

    # Write the header row
    #writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     #"Percent of Reviews", "Length of Course"])

    # Write in zipped rows
    #writer.writerows(cleaned_csv)


# Define the function and have it accept the 'wrestler_data' as its sole parameter
#def print_percentages(wrestler_data):
    # For readability, it can help to assign your values to variables with descriptive names
    #name = str(wrestler_data[0])
    #wins = int(wrestler_data[1])
    #losses = int(wrestler_data[2])
    #draws = int(wrestler_data[3])

    # Total matches can be found by adding wins, losses, and draws together
    #total_matches = wins + losses + draws

    # Win percent can be found by dividing the the total wins by the total matches and multiplying by 100
    #win_percent = (wins / total_matches) * 100

    # Loss percent can be found by dividing the total losses by the total matches and multiplying by 100
    #loss_percent = (losses / total_matches) * 100

    # Draw percent can be found by dividing the total draws by the total matches and multiplying by 100
    #draw_percent = (draws / total_matches) * 100

    # If the loss percentage is over 50, type_of_wrestler is "Jobber". Otherwise it is "Superstar".
    #if loss_percent > 50:
       # type_of_wrestler = "Jobber"
    #else:
        #type_of_wrestler = "Superstar"

    # Print out the wrestler's name and their percentage stats
    #print(f"Stats for {name}")
    #print(f"WIN PERCENT: {win_percent}")
    #print(f"LOSS PERCENT: {loss_percent}")
    #print(f"DRAW PERCENT: {draw_percent}")
    #print(f"{name} is a {type_of_wrestler}")


# Read in the CSV file
#with open(wrestling_csv, 'r') as csvfile:

    # Split the data on commas
    #csvreader = csv.reader(csvfile, delimiter=',')

    #header = next(csvreader)

    # Prompt the user for what wrestler they would like to search for
    #name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    #for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        #if name_to_check == row[0]:
            #print_percentages(row)