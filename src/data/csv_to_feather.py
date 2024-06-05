import pandas as pd

# Read the CSV file
df = pd.read_csv("obfuscated_data.csv")

# Save the DataFrame as a Feather v2 file
df.to_feather("obfuscated_data_v2.feather", version=2)
