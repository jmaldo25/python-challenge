import os
import csv
# print(os.getcwd()) 'test for pathway'

# Need to import csv files and pathway
# Need to get total number of months
# Need to get net total amount of 'Profit/Losses'
# Need to get average of changes of 'Profit/Loses'
# Need to get greatest increase in profits (date and amount) over entire period
# Need to get greatest decrease in loses (date and amount) over entire period


# Defined the pathway
pybank_csv = os.path.join('Resources', 'budget_data.csv')

# Defining the function for 'bank_data'
def print_totals(bank_data):
    months = str(bank_data[0])
    pft_ls = int(bank_data[1])

# Defining the calculations
    total_months = months

    net = sum(pft_ls)

    avg = sum(pft_ls) / len(pft_ls)

    max_pft = max(pft_ls)

    min_pft = min(pft_ls)

    avg_chg = (max_pft - min_pft) / avg
    



# Read in the pathway
with open(pybank_csv, "r") as file:
    reader = csv.reader(file)
    total_months_total = len(list(reader))
    
    
