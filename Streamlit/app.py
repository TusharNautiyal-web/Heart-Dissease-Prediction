
import streamlit as st
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('mainmodel.pkl', 'rb'))
#------------MAIN CODE------------------
def predictions(sex,cp,trestbps,fbs,restecg,thalach,exang,slope,ca,thal,oldpeak,age,chol):
    prediction=model.predict([[sex,cp,trestbps,fbs,restecg,thalach,exang,slope,ca,thal,oldpeak,age,chol]])
    if prediction == 0:
        return "No Presence of heart dissease"
    else:
        return "You have a chance of heart dissease"
    
def main():
    st.title("Heart Dissease Prediction Streamlit Version")
    sex = st.number_input('sex')
    cp = st.number_input('cp')
    trestbps = st.number_input('trestbps')
    age = st.number_input('age')
    oldpeak = st.number_input('oldpeak')
    exang = st.number_input('exang')
    fbs = st.number_input('fbs')
    restecg = st.number_input('restecg')
    thalach = st.number_input('thalach')
    slope = st.number_input('slope')
    thal = st.number_input('thal')
    chol = st.number_input('chol')
    ca = st.number_input('ca')

    # ----------- age -------------
    if(age>=28.952 and age<45.0):
        age = 1
    elif(age>=45 and age<61):
        age = 2
    elif(age>=61):
        age = 0
    elif(age<28.952):
        age = 1
    # --------- Cholestrol -----------
    if(chol>=125.562 and chol<272.0):
        chol = 0
    elif(chol>=272.0 and chol<418.0):
        chol = 1        
    elif(chol>=418.0 and chol<564.0):
        chol = 2
    elif(chol<125.562):
        chol = 0      
    # --------- old peak -----------
    if(oldpeak>= 0 and oldpeak<1.5):
        oldpeak = 2
    elif(oldpeak>=1.5 and oldpeak<2.55):
        oldpeak = 0       
    elif(oldpeak>=2.55 and oldpeak<7.0):
        oldpeak = 1
    elif(oldpeak<0):
        oldpeak = 2    
    
    if st.button("Info"):
        html_temp = """
        <p>Oldpeak categorization p>
        <p>1. Low => 0.0 to 1.5</p>
        <p>2. Risk => 1.5 to 2.55 </p>
        <p>3. Terrible => 2.55 to 7.0  </p>
        <p></p>
        <br>
        <p>Age Categorization p>
        <p>1. adult => 28.952, 45.0</p>
        <p>2. old => 45.0, 61.0</p>
        <p>3. senior => 61.0, 77.0</p>
        <p></p>
        <br>

        <p>Chol = ['Desirable Level','Borderline High Level','High Level']</p>
        <p>125.562, 272.0    222</p>
        <p>272.0, 418.0       80</p>
        <p>418.0, 564.0       1</p>
        <p></p>
        <br>

        <p>sex: sex (1 = male; 0 = female)</p>
        <p></p>
        <p>cp: chest pain type</p>
        <p>- Value 1: typical angina</p>
        <p>- Value 2: atypical angina</p>
        <p>- Value 3: non-anginal pain</p>
        <p>- Value 4: asymptomatic</p>
        <p></p>
        <br>

        <p>trestbps: resting blood pressure (in mm Hg on admission to the hospital)</p>
        <p></p>
        <br>

        <p>ca: number of major vessels (0-3) colored by flourosopy</p>
        <p></p>
        <br>

        <p>fbs: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)</p>
        <p></p>
        <br>

        <p>thal: 3 = normal; 6 = fixed defect; 7 = reversable defect</p>
        <p></p>
        <br>

        <p>restecg: resting electrocardiographic results</p>
        <p>- Value 0: normal </p>
        <p>- Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)</p>
        <p>- Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria</p>
        <p></p>
        <br>

        <p>thalach: maximum heart rate achieved</p>
        """
        st.markdown(html_temp,unsafe_allow_html=True)
    #---------------PREDICTION--------------------------    
    if st.button("Predict"):
        result=predictions(sex,cp,trestbps,fbs,restecg,thalach,exang,slope,ca,thal,oldpeak,age,chol)
        st.success(result)
    
if __name__=='__main__':
    main()