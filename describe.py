import pandas as pd

data = {
    "Name" : ["Prem", "Jay", "Arpit", "Aadarsh", "Dev", "Chirag", "Mridul","Hitesh", "ShyamJi"],
    "Age" : [20, 21, 22, 23, 24, 25, 26, 27, 28],
    "City" : ["Vrindavan", "Delhi", "Agra", "Mathura", "Gwalior", "Indore", "Bhopal", "Jaipur", "Udaipur"],
    "Country": ["India", "India", "India", "India", "India", "India", "India", "India", "India"],
    "Salary": [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000]
}

df = pd.DataFrame(data)
print("Print Employee DataFrame:")
print(df)
print(f'shape {df.shape}')  # gave info abut row and columns
print(f'Columns {df.columns}') # gave info about columns names
#Accessing single column
name = df["Name"]
print("Accessing single column 'Name':")
print(name)
#Accessing multiple columns
columns = df[["Name", "Age"]]
print("Accessing multiple columns 'Name' and 'Age':")   
print(columns)
