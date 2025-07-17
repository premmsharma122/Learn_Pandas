import pandas as pd
df = pd.read_csv('sales_data_sample.csv', encoding='latin1')
print('Display the 10 lines from top')
print(df.head(10))  # Display the first 10 rows of the DataFrame
print('Display the 10 lines from bottom ')
print(df.tail(10))  # Display the last 10 rows of the DataFrame
