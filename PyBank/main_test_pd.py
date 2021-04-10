# Make sure to use print() to have python print dataframe

import pandas as pd

csv_path = "Resources/budget_data.csv"

bank_df = pd.read_csv(csv_path, encoding="utf-8")

# Test to ensure pandas pathway was correct
# bank_df.head()

# Calculation for total months
print(f"Total Months: ", bank_df["Date"].count())

# Calculation for sum of Profit/Losses
print(f"Total: $", bank_df["Profit/Losses"].sum())

# Setting bank average with calculation for average
bank_avg = bank_df["Profit/Losses"].mean()
print(bank_avg)

# Setting bank max number with max calculation
bank_max = bank_df["Profit/Losses"].max()
print(bank_max)

# Setting bank min number with min calculation
bank_min = bank_df["Profit/Losses"].min()
print(bank_min)

# Creating f function statement for print out