# Load pandas
import pandas as pd

# Read CSV file into DataFrame df
df = pd.read_csv('sample.csv', index_col=0)

# Show dataframe
print(df)