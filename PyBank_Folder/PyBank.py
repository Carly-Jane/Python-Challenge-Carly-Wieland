#PyBank Task Instructions can be found in the read me file.

# alright alright alright

import os
import csv

#lists for variables to be counted in.

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


    # *** The total number of months included in the dataset ***

    for row in csvreader:

        # append first column (date) to months list
        total_months.append(row[0])

        # append second column (profit/loss) to total list
        total_profit_or_loss.append(int(row[1]))

        # append third column (profit/loss) to largest_increase list
        largest_increase.append(int(row[1]))

        # append third column (profit/loss) to largest_decrease list
        largest_decrease.append(int(row[1]))

    # Test code point - no need to print, just a sanity check: #print(total_months) #print(total_profit_or_loss) #print(largest_increase) #print(largest_decrease)


    # Create a list containing the change in values from month to month. Then assign to variable. Use zip - "zip takes in a series of lists as it's parameters and joins them together into a stack"
    average_change_list = [x-y for y, x in zip(total_profit_or_loss[:-1], total_profit_or_loss[1:])]
    
    # Test code point - no need to print, just a sanity check: # print(average_change_list)


    # Find which month had the largest increase/decrease in profits - using letters i , j , k , l , m , n for the loops
    # Reference 1: https://www.geeksforgeeks.org/enumerate-in-python/

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

    # Test code point - no need to print, just a sanity check: #print(months_maximum_index)#print(largest_increase_month)#print(months_minimum_index)#print(largest_decrease_month)
    
    # *** Final script should both: 1) print the analysis to the terminal. 2) export a text file with the results. ***

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
    print('                                  ')
    print('__________________________________')

    # 2) export a text file
    bank_data_output_csv = os.path.join('bank_data_output.csv')
    with open(bank_data_output_csv, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        
        csvwriter.writerow(['Financial Analysis'])
        csvwriter.writerow(['- - - - - - - - - - - - - - - - - '])
        csvwriter.writerow([(f'Total Months: {len(total_months)}')])
        csvwriter.writerow([(f'Total: ${sum(total_profit_or_loss)}')])
        csvwriter.writerow([(f'Average Change: ${round(sum(average_change_list) / len(average_change_list),2)}')])
        csvwriter.writerow([(f'Greatest Increase in Profits: {largest_increase_month} ${max(largest_increase)})')])
        csvwriter.writerow([(f'Greatest Decrease in Profits: {largest_decrease_month} ${min(largest_increase)})')])


# Reference List:
# Reference 1: https://www.geeksforgeeks.org/enumerate-in-python/
# "built-in function enumerate() - Often, when dealing with iterators, we also get a need to keep a count of iterations."
# "Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object. "
# "This enumerated object can then be used directly for loops or converted into a list of tuples using the list() method."