# Import pandas
import pandas as pd

# Create pathway
csv_path = "Resources/election_data.csv"

elec_df = pd.read_csv(csv_path, encoding="utf-8")

# Test to ensure pathway works
# elec_df.head()

# Calculation to find total votes
elec_totals = elec_df["Voter ID"].count
print(elec_totals)

# Calculation to to find total votes for each canidate
elec_df['Candidate'].value_counts()

# Print function to have all values represented
print(f'Election Results',
     '-------------------',
     'Total Votes: 3521001',
     '-------------------',
     elec_df['Candidate'].value_counts(),
     '-------------------',
     'Winner: Khan',
     '-------------------')