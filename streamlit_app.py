import streamlit as st
import pandas as pd

df_protein = pd.read_csv ('proteinvalues-foods.csv')
df_protein = df_protein.sort_values("Food").reset_index(drop=True)
df_kids = pd.read_csv ('proteinvalues-kids.csv')
df_protein = df_protein.rename(columns={' Portion size': 'Portion', 'Grams protein': 'Protein (grams)'})


st.title("Protein calculator for kids - test2")
st.write("""
My kids are picky eaters and I am always worried if they are getting enough calories or protein! 
Try this quick calculator to see how much protein your kid gets in a day
""")
a,b = st.columns(2)
with a:
    age = st.selectbox("Child's age",["1 to 3 years","4 to 8 years","9 to 13 years","14 to 18 years"])
with b:
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

st.subheader("Meal plan")

foods = st.multiselect("Select what your kid is eating today to see how much protein they're getting.", df_protein["Food"])
st.write("")

if foods:
    sum_grams = 0
    for food, col in zip(foods, st.columns(len(foods))):
        with col:
            st.write(f"**{food}**")
            st.write("Serving size:  ", df_protein["Portion"].loc[df_protein["Food"]==food].to_string(index=False))
            st.write("Protein per serving (grams):  ",df_protein["Protein (grams)"].loc[df_protein["Food"]==food].to_string(index=False))
            portion = st.number_input("Number of portions", 1, key=food)
            grams = df_protein["Protein (grams)"].loc[df_protein["Food"]==food] * portion
            grams = grams.iloc[0]
            sum_grams = sum_grams + grams

    
    total_prot = sum_grams
    diff = prot - total_prot

    st.write("")
    st.write("")
    st.subheader("Total protein in meal")
    if diff == 0:
        st.write("Congrats! Your kid is getting enough protein. They need ", prot, " grams and they are getting ", total_prot, " grams!")
        st.balloons()
    if diff > 0:
        st.write("This meal contains ", total_prot," grams of protein. You need to add another ", diff, " grams of protein.")
    if diff <0:
        st.write("Your kid might be getting too much protein! They need ", prot, " grams and they are getting ", total_prot, " grams")

st.write("")
st.write("")
st.write("")
with st.expander("View full foods table"):
    df_protein
