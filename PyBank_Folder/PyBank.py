#PyBank:

#In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

#Your task is to create a Python script that analyzes the records to calculate each of the following:

#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

#As an example, your analysis should look similar to the one below:

#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.


# let's go baby

import os
import csv

#Empty lists for variables to be counted in. Quick mafths.

total_months = []
total_profit_or_loss = []
largest_increase = []
largest_decrease = []

# Connect CSV file 
bank_data_csv = os.path.join('budget_data.csv')


with open (bank_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip header row
    csv_header = next(csvreader, None)

    # alright alright alright
    # *** The total number of months included in the dataset ***
    # Loop through each row and append data to variables
    # DRAFT

    for row in csvreader:

        # append first column (date) to months list
        total_months.append(row[0])

        # append second column (profit/loss) to total list
        total_profit_or_loss.append(int(row[1]))

        # append third column (profit/loss) to largest_increase list
        largest_increase.append(int(row[1]))

        # append third column (profit/loss) to largest_decrease list
        largest_decrease.append(int(row[1]))

    #print not required
    #print(total_months)
    #print(total_profit_or_loss)
    #print(largest_increase)
    #print(largest_decrease)

    # Create a list containing the change in values from month to month. Then assign to variable.
    average_change_list = [x-y for y, x in zip(total_profit_or_loss[:-1], total_profit_or_loss[1:])]
    
    # no need to print
    # print(average_change_list)

    # find which month had the largest increase/decrease in profits
    # using letters i , j , k , l , m , n for the loops

    # find index number of the largest increase and store in ‘months_maximum_index’ variable
    for i, j in enumerate (largest_increase):
        if j == max(largest_increase):
            months_maximum_index = (i)

    # store the month with the largest increase in ‘lge_increase_month’ variable
    for k in [total_months[months_maximum_index]]:
        largest_increase_month = k

    # find index number of the largest decrease and store in ‘months_minimum_index’ variable
    for l, m in enumerate (largest_decrease):
        if m == min(largest_decrease):
            months_minimum_index = (l)

    # store the month with the largest decrease in ‘lge_decrease_month’ variable
    for n in [total_months[months_minimum_index]]:
        largest_decrease_month = n

    # test code
    # heck yeah looks like she's runnin'
    # no need to print, just a sanity check
    #print(months_maximum_index)
    #print(largest_increase_month)
    #print(months_minimum_index)
    #print(largest_decrease_month)

    
    # In addition, your final script should both: 
    # 1) print the analysis to the terminal.
    # 2) export a text file with the results.

    # 1) terminal
    print('__________________________________')
    print('                                  ')
    print('Financial Analysis')
    print('- - - - - - - - - - - - - - - - - ')
    print(f'Total Months: {len(total_months)}')
    print(f'Total: ${sum(total_profit_or_loss)}')
    print(f'Average Change: ${round(sum(average_change_list) / len(average_change_list),2)}')
    print(f'Greatest Increase in Profits: {largest_increase_month} ${max(largest_increase)})')
    print(f'Greatest Decrease in Profits: {largest_decrease_month} ${min(largest_increase)})')

    # 2) export a text file
    bank_data_output_csv = os.path.join('bank_data_output.csv')
    with open(bank_data_output_csv, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')

        # Write the first row - Financial Analysis
        
        csvwriter.writerow('Financial Analysis')
        csvwriter.writerow('- - - - - - - - - - - - - - - - - ')
        csvwriter.writerow(f'Total Months: {len(total_months)}')
        csvwriter.writerow(f'Total: ${sum(total_profit_or_loss)}')
        csvwriter.writerow(f'Average Change: ${round(sum(average_change_list) / len(average_change_list),2)}')
        csvwriter.writerow(f'Greatest Increase in Profits: {largest_increase_month} ${max(largest_increase)})')
        csvwriter.writerow(f'Greatest Decrease in Profits: {largest_decrease_month} ${min(largest_increase)})')

        # LITERALY SO CLOSE I JUST NEED TO GET THESE DARN COMMAS OUT OF MY CSV FILE