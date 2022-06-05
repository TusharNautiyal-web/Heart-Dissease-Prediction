import pickle
from fastapi import FastAPI
import uvicorn
import numpy as np
import pandas as pd
from HeartDisseases import hd

# Pydantic will give errors during the api calls.
# We need to inherit the Base Model if we want to use Pydantic.
app = FastAPI()
pickler = open("mainmodel.pkl","rb")
model = pickle.load(pickler)

@app.get("/")
def index():
    return {'messsage' : "Hello This My API for Heart Dissease Prediction"}

@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To Tushar Youtube Channel': f'{name}'}

@app.post('/predict')
def give_prediction(data:hd):
    data=data.dict()
    sex=data['sex']
    cp=data['cp']
    trestbps=data['trestbps']
    age=data['age']
    oldpeak=data['oldpeak']
    exang=data['exang']
    fbs=data['fbs']
    restecg=data['restecg']
    thalach=data['thalach']
    slope=data['slope']
    thal=data['thal']
    chol=data['chol']
    ca=data['ca']
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
    prediction = model.predict([[sex,cp,trestbps,fbs,restecg,thalach,exang,slope,ca,thal,oldpeak,age,chol]])
    if(prediction[0] == 0):
        prediction="No heart Dissease"
    else:
        prediction="Heart Dissease Present"
    return {
        'prediction': prediction
    }



if __name__=='__main__':
    uvicorn.run(app, host = 'localhost',port = '8000')