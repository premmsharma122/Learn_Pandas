import pandas as pd
custumer_data =pd.DataFrame({
    'cust_Id' : [1, 2, 3, 4, 5],
    'cust_Name' : ['Prem', 'Jay', 'Arpit', 'Aadarsh', 'Dev'],
})

custumer_Order = pd.DataFrame({
    'cust_Id': [1, 2, 3, 4, 5],
    'order_name' : ['Order1', 'Order2', 'Order3', 'Order4', 'Order5'],
})
# Merging DataFrames on 'cust_Id'
merge_df = pd.merge(custumer_data, custumer_Order, on='cust_Id', how='inner')
print("Merged DataFrame:")
print(merge_df)
# Types -> inner, outer, left, right
