import os
import csv

# Need to import csv files and pathway
# Need to get total number of months
# Need to get net total amount of 'Profit/Losses'
# Need to get average of changes of 'Profit/Loses'
# Need to get greatest increase in profits (date and amount) over entire period
# Need to get greatest decrease in loses (date and amount) over entire period


pybank_csv = os.path.join('..', 'Resources', 'budget_data.csv')


def print_analysis(bank_data):

    date = str(bank_data[0])
    pft_lss = int(bank_data[1])


    num_rows = 0

    for row in open(pybank_csv):
        num_rows += 1

    print(f"Total months: 86")
