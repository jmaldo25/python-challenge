import pandas as pd

csv_path = "Resources/budget_data.csv"

bank_df = pd.read_csv(csv_path)

# bank_df.head()

bank_df["Date"].count()

bank_df["Profit/Losses"].sum()