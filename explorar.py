import pandas as pd

df = pd.read_csv("data/raw/credit_data.csv")
print(df.shape)
print(df.columns.tolist())
df.info()
