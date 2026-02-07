import streamlit as st
import pandas as pd
import numpy as np
import joblib

# load the trained model
model=joblib.load("model.pkl")

st.set_page_config(page_title="Diamond Price Predictor",layout="centered")

st.title(" 💎 Diamond Price Prediction App ")
st.write("Enter diamond details to predict the price")

# ------user_inputs-------
carat=st.number_input("carat (in_carats)",min_value=0.2,max_value=5.0,step=0.01)
depth=st.number_input("Depth",min_value=50,max_value=70)
table=st.number_input("Table",min_value=50,max_value=70)
x=st.number_input("Length (x)",min_value=1.0)
y=st.number_input("width (y)",min_value=1.0)
z=st.number_input("Height (z)",min_value=1.0)

cut=st.selectbox("cut",['Fair','Good','Very Good','Premium','Ideal'])
color=st.selectbox("color",['D','E','F','G','H','I','J'])
clarity=st.selectbox('Clarity',['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF'])

# convert input into DataFrame
df=pd.DataFrame({"carat":[carat],"depth":[depth],"table":[table],"x":[x],"y":[y],"z":[z],"cut":[cut],"color":[color],"clarity":[clarity]})

# prediction button

if st.button("Predict Price"):
    prediction=model.predict(df)
    st.success(f" 💰 Predicted price: ${prediction[0]:,.2f}")