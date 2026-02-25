import pandas as pd

# Basic upload
df = pd.read_excel('university_data.xlsx')

# Upload a specific sheet
df_specific = pd.read_excel('university_data.xlsx', sheet_name=0)

# Display first few rows
print(df.head())
