import os
import csv

# Need to import csv files and pathway (DONE)
# Need to get total number of months
# Need to get net total amount of 'Profit/Losses'
# Need to get average of changes of 'Profit/Loses'
# Need to get greatest increase in profits (date and amount) over entire period
# Need to get greatest decrease in loses (date and amount) over entire period

pybank_csv = os.path.join('..', 'Resources', 'budget_data.csv')

def print_analysis(bank_data):

    date = str(bank_data[0])
    pft_lss = int(bank_data[1])


    file = open("budget_data.csv")
    reader = csv.reader(file)
    total_months = len(list(reader))

    print(f"Total months: {total_months}")