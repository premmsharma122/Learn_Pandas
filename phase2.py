import pandas as pd

data  = {
    "Name": ["Prem", "Jay", "Arpit", "Aadarsh", "Dev", "Chirag", "Mridul", "Hitesh", "ShyamJi"],
    "Age": [20, 21, 22, 23, 24, 25, 26, 27, 28],
    "City": ["Vrindavan", "Delhi", "Agra", "Mathura", "Gwalior", "Indore", "Bhopal", "Jaipur", "Udaipur"],
    "Country": ["India", "India", "India", "India", "India", "India", "India", "India", "India"],
    "Salary": [1000000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000],
    "Experience": [2, 3, 4, 5, 6, 7, 8, 9, 10]
}
df = pd.DataFrame(data)
print(df)
# Insert a colum in Data Frame-> Ist Method
df["Bounce"] = df["Salary"] *0.1
print("DataFrame after adding 'Bounce' column:" )
print(df)
# Insert a column in Data Frame -> 2nd Method
df.insert(2, "Bonus", df["Salary"] * 0.05)
print("DataFrame after adding 'Bonus' column:")
print(df)

#Update a column value 
df.loc[0, "Salary"]  = 1200000
print("DataFrame agter update salary of the first employee : ",df)  
