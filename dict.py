
import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print(df)
print("**********************")
print(df.iloc[1])
print("**********************")
df = pd.read_csv(r"C:\Users\aditya.joshi_infobea\Downloads\student.csv")
print(df.head())
print("**********************")
print(df.tail())
print("**********************")
print(df.dtypes)
print("**********************")
print(df.describe())
print("**********************")
print(df.isnull().sum())
print("**********************")
df_clean = df.dropna()

