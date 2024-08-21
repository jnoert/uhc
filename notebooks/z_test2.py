##import pandas as pd

## Read the CSV file
#df = pd.read_csv('asssets/all_teams.csv')

## Print the first 10 rows
#print(df.head(10))


import pandas as pd

# Read the CSV file
df = pd.read_csv('asssets/all_teams.csv')

# Find the first row for each unique value in column B
first_occurrences = df.drop_duplicates(subset='team', keep='first')

# Print those rows
print(first_occurrences)

# Write the result to a new CSV file
first_occurrences.to_csv('unique_teams.csv', index=False)