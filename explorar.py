import pandas as pd

df = pd.read_csv("data/raw/credit_risk_dataset.csv")
print(df.shape)
print(df.columns.tolist())
df.info()
print(df.isna().sum())
print(df.describe().T)
print(df["person_home_ownership"].unique())
print(df["loan_intent"].unique())
