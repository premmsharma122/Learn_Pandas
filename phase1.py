import pandas as pd
# Read data from csv file
# df = pd.read_csv('sales_data_sample.csv', encoding='latin1')
# print(df)
# creating a data frame 
data ={
    "Name" : ["Prem", "Sharma", "CSaini"],
    "Age" : [20,19, 19],
    "City" : ["Vrindavan", "London", "Vrindavan"]
}
df2 = pd.DataFrame(data,)
print(df2)
df2.to_csv('output.csv', index=False) // Save the DataFrame to a CSV file or convert it to a CSV file
