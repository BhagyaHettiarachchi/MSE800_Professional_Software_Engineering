import pandas as pd

# Load the Parquet file
df = pd.read_parquet('Week4/Sample_data_2.parquet')

# Print the number of rows in the DataFrame
print(len(df))
