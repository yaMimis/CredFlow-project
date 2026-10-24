from pathlib import Path
import numpy as np
import pandas as pd

RENAME = {
    "person_age": "idade", "person_income": "renda_anual",
    "person_home_ownership": "moradia", "person_emp_length": "anos_emprego",
    "loan_intent": "finalidade", "loan_grade": "grade_original",
    "loan_amnt": "valor_imprestimo", "loan_int_rate": "taxa_juros",
    "loan_status": "inadimplencia", "loan_percent_income": "comprometimento_renda",
    "cb_person_defalt_on_file": "historico_calote", "cb_person_cred_hist_length": "anos_hist_credito",
    }

IDADE_MIN, IDADE_MAX =18, 100
EMPREGO_MAX = 60
IDADE_INICIO_TRAB = 14