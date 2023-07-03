import joblib
import pandas as pd
import streamlit as st
from sklearn.tree import DecisionTreeClassifier

df = pd.read_excel('Tree_decision.xlsx')

X = df[['DIVIDEND YIELD', 'LIQUIDEZ DIÁRIA', 'P/VP', 'CAGR LUCRO']]
y = df["INVESTIR"]

clf = DecisionTreeClassifier(criterion='entropy', random_state=0)
clf.fit(X, y)

# Title
st.header("Fe²")

# Input bar 1
liquidez = st.number_input("Liq. Diária: ")

# Input bar 2
pvp = st.number_input("P/VP: ")

# Input bar 3
dy = st.number_input("Dividend Yield: ")

# Input bar 4
cagr = st.number_input("CAGR: ")

# If button is pressed
if st.button("Submit"):
    # Previsão com o modelo
    y_pred = clf.predict([[dy, liquidez, pvp, cagr]])
    
    # Mapear os valores da previsão para "Investir" ou "Não Investir"
    investimento = "Investir" if y_pred[0] == 1 else "Não Investir"
    
    st.text("Resultado da previsão: " + investimento)
