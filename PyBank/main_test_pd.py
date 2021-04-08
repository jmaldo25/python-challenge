# Make sure to use print() to have python print dataframe

import pandas as pd

csv_path = "Resources/budget_data.csv"

bank_df = pd.read_csv(csv_path)

print(bank_df.head())

# bank_df["Date"].count()

# bank_df["Profit/Losses"].sum()

# bank_df["Profit/Losses"].mean()