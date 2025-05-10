import pandas as pd

# Read the text file with tab delimiter
df = pd.read_csv('Week4/sample_text.txt', delimiter='\t')

# Print the first record
print("First record:")
print(df.head(1))

# Print the last record
print("\nLast record:")
print(df.tail(1))
