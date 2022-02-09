import streamlit as st
import pandas as pd

df_protein = pd.read_csv ('proteinvalues-foods.csv')
df_kids = pd.read_csv ('proteinvalues-kids.csv')

st.title("Protein calculator for kids - test")
st.write("""
My kids are picky eaters and I am always worried if they are getting enough calories or protein! 
Try this quick calculator to see how much protein your kid gets in a day
""")

age = st.selectbox("Child's age",["1 to 3 years","4 to 8 years","9 to 13 years","14 to 18 years"])
sex = st.selectbox("Child's sex",["Boy","Girl"])

def protein(age,sex):
    if age == "1 to 3 years":
        return 0
    elif age == "4 to 8 years":
        return 1
    elif age == "9 to 13 years":
        return 2
    elif age == "14 to 18 years" and sex == "Boy":
        return 3
    else:
        return 4

age_calc = protein(age,sex)
prot = df_kids.iloc[age_calc].iloc[1]
st.write("Your child needs ",prot," grams of protein a day")