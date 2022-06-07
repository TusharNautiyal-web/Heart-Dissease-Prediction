#Import necessary libraries
import pickle
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
import numpy as np

# Create your views here.
@api_view(['GET'])
def index_page(request):
    return_data = {
        "error" : "0",
        "message" : "Successful",
    }
    return Response(return_data)

@api_view(["POST"])
def predict_heart(request):
    try:
        sex = request.data.get('sex',None)
        cp = request.data.get('cp',None)
        trestbps = request.data.get('trestbps',None)
        age = request.data.get('age',None)
        oldpeak = request.data.get('oldpeak',None)
        exang = request.data.get('exang',None)
        fbs = request.data.get('fbs',None)
        restecg = request.data.get('restecg',None)
        thalach = request.data.get('thalach',None)
        slope = request.data.get('slope',None)
        thal = request.data.get('thal',None)
        chol = request.data.get('chol',None)
        ca = request.data.get('ca',None)
        
        fields = [sex,cp,trestbps,age,oldpeak,exang,fbs,restecg,thalach,slope,thal,chol,ca]
        if not None in fields:
            #Datapreprocessing Convert the values to float
            sex = int(sex)
            cp = int(cp)
            trestbps = int(trestbps)
            age = int(age)
            oldpeak = float(oldpeak)
            exang = int(exang)
            fbs = int(fbs)
            restecg = int(restecg)
            thalach = int(thalach)
            slope = int(slope)
            thal = int(thal)
            chol = int(chol)
            ca = int(ca)
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
    
            result = [sex,cp,trestbps,age,oldpeak,exang,fbs,restecg,thalach,slope,thal,chol,ca]
            #Passing data to model & loading the model from disks
            model_path = 'ml_model/mainmodel.pkl'
            classifier = pickle.load(open(model_path, 'rb'))
            prediction = classifier.predict([result])
            if prediction == 0:
                prediction =  "No Presence of heart dissease"
            else:
                prediction =  "You have a chance of heart dissease"
                
            predictions = {
                'error' : '0',
                'message' : 'Successfull',
                'prediction' : prediction
            }
        else:
            predictions = {
                'error' : '1',
                'message': 'Invalid Parameters'                
            }
    except Exception as e:
        predictions = {
            'error' : '2',
            "message": str(e)
        }
    
    return Response(predictions)