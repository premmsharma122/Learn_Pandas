import pandas as pd
data ={
    "Time" : ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00"],
    "Value" : [10, 20, 30, None, 50, None, 70, 80, None]
}
df = pd.DataFrame(data)
print("Original DataFrame W/O Interpolation:")
print(df)
# Interpolate missing values
df["Valuue"] = df["Value"].interpolate(method='linear')
print("DataFrame after Interpolation:")
print(df)
# thera are main three methods of interpolation-> 1. linear, 2. polynomial, 3. spline
