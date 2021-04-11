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

# Defining the functions for 'bank_data'
dates = []
pft_ls = []

# Read in the pathway and pull data
with open(pybank_csv, "r") as file:
    bank_reader = csv.reader(file)
    next(file)
    for row in bank_reader:
        dates.append(row[0])
        pft_ls.append(int(row[1]))

# Creating the variables to store calculated values
total_months = len(dates)
total_pft = sum(pft_ls)

# Creating variables to store starting data
rev_change = 0
pft_rev = (pft_ls[1]) - (pft_ls[0])
ls_rev = (pft_ls[1]) - (pft_ls[0])

# Creating loop for calculating average change as well as calculating changes
for i in range(0, total_months-1):
    difference = (pft_ls[i+1]) - (pft_ls[i])
    if difference >= pft_rev:
        pft_rev = difference
        date_pft = dates[i+1]
    elif difference <= ls_rev:
        ls_rev = difference
        date_ls = dates[i+1]
    rev_change += difference

# Calculate average revenue change
avg_rev = rev_change / total_months

# Print output

print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total Revenue: {total_pft}")
print(f"Average Revenue Change: {avg_rev}")
print(f"Greatest Increase in Profit: {date_pft} $ {pft_rev}" )
print(f"Greatest Decrease in Profit: {date_ls} $ {ls_rev}" )

# Creating text file for output
txt_output = os.path.join("Analysis", 'Financial_Analysis.txt')
with open (txt_output, 'w', newline='') as summary:
    write = csv.writer(summary)
    write.writerows([
["Financial Analysis"],
["-------------------------"],
["Total Months: " + str(total_months)],
["Total Revenue: " + str(total_pft)],
["Average Revenue Change: $" + str(avg_rev)],
["Greatest Increase in Profit: " + str(date_pft) + "$" + str(pft_rev) ],
["Greatest Decrease in Profit: " + str(date_ls) + "$" + str(ls_rev) ]
    ])
