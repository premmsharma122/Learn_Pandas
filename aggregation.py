import pandas as pd
data ={
   "Name" : ["Prem", "Jay", "Arpit", "Aadarsh", "Dev", "Chirag", "Mridul", "Hitesh", "ShyamJi"],
   "Age" : [20, 20, 22, 23, 24, 25, 26, 27, 28],
   "City" : ["Vrindavan", "Delhi", "Agra", "Mathura", "Gwalior", "Indore", "Bhopal", "Jaipur", "Udaipur"],
}
df = pd.DataFrame(data)
age_sum = df["Age"].sum()
# print("Sum of Age column:", age_sum)
# # Same as we calculate mean, median, mode, std, var, min, max
# age_mean = df["Age"].mean()
# print("Mean of Age column:", age_mean)
# age_median = df["Age"].median()
# print("Median of Age column:", age_median)
# age_mode = df["Age"].mode()[0]  # mode() returns a Series, take the first element
# print("Mode of Age column:", age_mode)
# age_std = df["Age"].std() # Standard deviation
# print(age_std)

# Grouping DataFrame
grouped_df = df.groupby("Age").sum()  # Group by City and calculate mean for each group
print("Grouped DataFrame by Age with sum:")
print(grouped_df)
print("Grouped DataFrame by Age with sum for each group:")
grouped_df2 = df.groupby(["Age", "Name"])["City"].sum() 
print(grouped_df2)
