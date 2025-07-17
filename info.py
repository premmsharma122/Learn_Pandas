import pandas as pd
df = pd.read_csv('sales_data_sample.csv', encoding='latin1')
print("Information about the DataFrame:")
print(df.info())  # Display information about the DataFrame
