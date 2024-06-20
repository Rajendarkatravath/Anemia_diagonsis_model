import streamlit as st
import joblib
import streamlit as st
import sklearn
import pickle
import pandas as pd
import numpy as np
#model = pickle.load(open('model.sav', 'rb'))
# Load the model
model = joblib.load('model.joblib')
st.title("Model development ")

with st.form("container"):
     WBC=st.number_input("WBC")
     LYMp=st.number_input(" LYMp ")
     NEUTp=st.number_input("NEUTP")
     LYMn=st.number_input("LYMn")
     NEUTn=st.number_input("NEUTPn")
     RBC=st.number_input("RBC")
     HGB=st.number_input("HGB")
     HCT=st.number_input("HCT")
     MCV =st.number_input("MCV")
     MCH=st.number_input("MCH")
     MCHC=st.number_input("MCHC")
     PLT=st.number_input("PLT")
     PDW=st.number_input("PDW")
     PCT=st.number_input("PCT")
     columns={"WBC":WBC,
                "LYMp":LYMp,
                "NEUTp":NEUTp,
                "LYMn":LYMn,
                "NEUTn":NEUTn,
                "RBC":RBC,
                "HGB":HGB,
                "HCT":HCT,
                "MCV":MCV,
                "MCH":MCH,
                "MCHC":MCHC,
                "PLT":PLT,
                "PDW":PDW,
                "PCT":PCT
                }

     data=pd.DataFrame(columns,index=[0])

     

     diagonsis_data=model.predict(data)
     submit=st.form_submit_button("Diagonsis")
st.write("the entered values are :",data)

if submit:

    st.write(diagonsis_data)
