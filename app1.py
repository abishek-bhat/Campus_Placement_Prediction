import pickle
import streamlit as st
import numpy as np
import pandas as pd
from flask import Flask, app, jsonify, render_template, request, url_for

app=Flask (__name__)
model=pickle.load(open('model_svm.pkl','rb'))

def main():
    st.title("Campus Placement Prediction")

    Gender =st.selectbox("Gender",("Male","Female"))
    st.write('You selected:', Gender)
    ssc_p = st.text_input('Secondary Education - 10th Grade')
    hsc_p = st.text_input('Higher Secondary Education Percentage -12th Grade')
    hsc_s = st.selectbox('Specialization in Higher Secondary Education',('Commerce','Science','Others'))
    st.write('You selected:', hsc_s)
    degree_p = st.text_input('Degree Percenatge')
    degree_t = st.selectbox('Under Graduation(Degree type)- Field of degree education',('Sci&Tech','Comm&Mgmt'))
    st.write('You selected:', degree_t)
    workex = st.selectbox('Work Experience',('Yes','No'))
    etest_p = st.text_input('Employability test Percentage')
    specialisation = st.selectbox('Specialisation',('Mkt&HR','Mkt&Fin'))
    st.write('You selected:',specialisation )
    mba_p =st.text_input('MBA Percantage')
    if Gender == 'Male':
        Gender = 0
    else:
        Gender = 1       
    if degree_t == 'Sci&Tech':
        degree_t = 2
    elif degree_t == 'Comm&Mgmt':
        degree_t = 0
    else:
        degree_t = 1 
    
    if workex == 'Yes':
        workex = 1
    else:
        workex = 0
        
    if hsc_s == 'Commerce':
        hsc_s = 1
    elif hsc_s== 'Science':
        hsc_s = 2
    else:
        hsc_s = 0
        
    if specialisation == 'Mkt&HR':
        specialisation = 1
    else:
        specialisation = 0
    result=""
    output=""
    if st.button("Predict"):
        result=model.predict([[Gender,ssc_p,hsc_p,hsc_s,degree_p,degree_t,workex,etest_p,specialisation,mba_p]])
        if(result[0]==1):
            output="You are Doing well!! You Will Get placements"
        else:
            output="Work Hard!!! Chances are less"

    st.success(output)


    

if __name__=="__main__":
    main()
