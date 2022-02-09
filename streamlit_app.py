import streamlit as st

st.title("Protein calculator for kids")
st.write("""
My kids are picky eaters and I am always worried if they are getting enough calories or protein! 
Try this quick calculator to see how much protein your kid gets in a day
""")

age = st.selectbox("Child's age",["1 to 3 years","4 to 8 years","9 to 13 years","14 to 18 years"])
sex = st.selectbox("Child's sex",["Boy","Girl"])

def protein(age,sex):
    if age == "1 to 3 years":
        return 1
    elif age == "4 to 8 years":
        return 2
    elif age == "9 to 13 years":
        return 3
    elif age == "14 to 18 years" and sex == "Boy":
        return 4
    else:
        return 5

