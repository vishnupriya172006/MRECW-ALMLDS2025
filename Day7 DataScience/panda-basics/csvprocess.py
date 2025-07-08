import pandas as pd

df=pd.read_csv("people_data.csv")

print(df)

df1 = pd.read_csv("people_data.csv", usecols=["First Name", "Email"])
print(df1)

df2 = pd.read_csv("people_data.csv", index_col="First Name")
print(df2)