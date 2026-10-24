import numpy as np
import pandas as pd

df = pd.read_csv("data/raw/credit_risk_dataset.csv")
pd.set_option("display.width", 140)

print("\n-- 1. ESTRUTURA")
print("Linhas, colunas:", df.shape)
print(df.dtypes)


print("\n-- 2. NULOS")
nulos = df.isna().sum().to_frame("qtd")
nulos["%"] = (nulos["qtd"] / len(df) * 100).round(2)
print(nulos[nulos["qtd"] > 0])

print("\n-- 3. DUPLICADOS")
print("Linhas total duplicado:", int(df.duplicated().sum()))

print("\n-- 4. NUMERICAS")
print(df.describe().T[["min", "25%", "50%", "75%", "max"]])

print("\n-- 5. VALOS IRREAIS")
checks = {
    "idade < 18 ou > 100": ~df["person_age"].between(18, 100),
    "tempo de emprego > 60 anos": df["person_emp_length"] > 60,
    "emprego > idade - 14 (empregado antes dos 14)": df["person_emp_length"] - df["person_age"] - 14,
    "historico de credito > idade - 18": df["cb_person_cred_hist_length"] > df["person_age"] - 18,
    "renda <= 0": df["person_income"] <= 0,
    "valor do emprestimo <= 0": df["loan_amnt"] <= 0,
    "loan_status fora de 0/1": ~df["loan_status"].isin([0,1]),
    "loan_percent_income difere de valor/renda (> 0,02)": (df["loan_percent_income"] - df["loan_amnt"] / df["person_income"]).abs() > 0.02,
}

for nome, mascara in checks.items():
    print(f"{nome:62s} {int(mascara.sum()):6d} ({mascara.mean():.2%})")

print("\n-- 6. RENDA")
print(df["person_income"].quantile([.5, .9, .99, .999, 1]).round(0).to_string())
print("Renda acima de 1 milhão:", int((df["person_income"] > 1_000_000).sum()))

print("\n-- 7.CATEGORIAS")
for c in ["person_home_ownership", "loan_intent", "loan_grade", "cb_person_default_on_file"]:
    print(c, "->", df[c].value_counts(dropna=False).to_dict())

print("-- 8.ANALISE DE OBJETIVO")
print("Taxa de INADIMPLENCIA:", round(df["loan_status"].mean(), 4))
print("Inadimplencia por GRADE (A -> G):")
print(df.groupby("loan_grade")["loan_status"].agg(["count", "mean"]).round(3).to_string())
print("\n O fato de o dado estar ausente é informativo? (inadimplencia de quem tem vs quem não tem)")
for c in ["person_emp_length", "loan_int_rate"]:
 print(c, df.groupby(df[c].isna())["loan_status"].agg(["count", "mean"]).round(3).rename(index={False: "preenchido", True: "ausente"}).to_string(), sep="\n")