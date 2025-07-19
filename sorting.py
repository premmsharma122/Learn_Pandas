import pandas as pd
data ={
   
   "Name" : ["Prem", "Jay", "Arpit", "Aadarsh", "Dev", "Chirag", "Mridul", "Hitesh", "ShyamJi"],
   "Age" : [20, 21, 22, 23, 24, 25, 26, 27, 28],
   "City" : ["Vrindavan", "Delhi", "Agra", "Mathura", "Gwalior", "Indore", "Bhopal", "Jaipur", "Udaipur"],
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
df.sort_values(by="City", inplace=True, ascending=True)  # Sort by Age in ascending order
print("DataFrame after sorting by Age in ascending order:")
print(df)
#Sort Multiple Colums
df.sort_values(by=["City","Age"], inplace=True, ascending=[True, False])  # Sort by City ascending and Age descending
print("DataFrame after sorting by City ascending and Age descending:")
print(df)
