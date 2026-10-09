import streamlit as st
import pickle

liver = pickle.load(open('Liver.pkl','rb'))
st.title("Liver Disease Prediction")
st.number_input("Age", min_value=0, max_value=100)
age=st.number_input("Total Bilirubin", min_value=5, max_value=100)
gender=st.selectbox("Gender", ["Male", "Female"])
total_bilirubin=st.number_input("Total Bilirubin", min_value=0.0, max_value=100.0)
direct_bilirubin=st.number_input("Direct Bilirubin", min_value=0.0, max_value=100.0)
Liver_Enzymes=st.number_input("Liver Enzymes", min_value=0.0, max_value=100.0)
sgpt=st.number_input("SGPT", min_value=0.0, max_value=100.0)
sgot=st.number_input("SGOT", min_value=0.0, max_value=100.0)
total_proteins=st.number_input("Total Proteins", min_value=0.0, max_value=100.0)
albumin=st.number_input("Albumin", min_value=0.0, max_value=100.0)
agra=st.number_input("AG Ratio", min_value=0.0, max_value=100.0)

if st.button('Liver Disease Test Result'):
            liver_pred = liver.predict([[float(age),{'Male':0,"Female":1}[gender],float(total_bilirubin),float(direct_bilirubin),float(Liver_Enzymes),float(sgpt),float(sgot),float(total_proteins),float(albumin),float(agra)]])
            
            if liver_pred[0] == 1:
                st.success('The person liver is Healthy')
            elif liver_pred[0]==2:
                st.success('The person liver is UnHealthy (Moderate)')
            else:
                st.success('The person liver is in UnHealthy (High)')