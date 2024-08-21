import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('/Users/justin/Documents/git/NHL/asssets/all_teams.csv')

# Group by column B
grouped = df.groupby('B')

# Print the column titles
print("Column Titles: ", df.columns)

# Iterate over the groups and print the first row for each unique value in column B
for name, group in grouped:
    print(f"First row for unique value in column B ({name}):")
    print(group.iloc[0])
    print("\n")