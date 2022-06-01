from flask import Flask, render_template, request
import requests
import pickle
import numpy as np
app = Flask(__name__)
model = pickle.load(open('mainmodel.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('Index.html')
# Target value = 0 => No Presence of heart dissease.
# Target value = 1 => Presence of heart dissease.
# sex	cp	trestbps	fbs	restecg	thalach	exang	slope	ca	thal	oldpeak_cat	age_cat	chol_cat
# Oldpeak categorization
# 1. Low => 0.0 to 1.5
# 2. Risk => 1.5 to 2.55 
# 3. Terrible => 2.55 to 7.0  
# Age Categorization
# 1. adult => 28.952, 45.0
# 2. old => 45.0, 61.0
# 3. senior => 61.0, 77.0
#  Chol = ['Desirable Level','Borderline High Level','High Level']
# (125.562, 272.0]    222
# (272.0, 418.0]       80
# (418.0, 564.0]        1

# Complete attribute documentation:
# sex: sex (1 = male; 0 = female)

# cp: chest pain type
# - Value 1: typical angina
# - Value 2: atypical angina
# - Value 3: non-anginal pain
# - Value 4: asymptomatic
# trestbps: resting blood pressure (in mm Hg on admission to the hospital)

# ca: number of major vessels (0-3) colored by flourosopy

# fbs: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)

# thal: 3 = normal; 6 = fixed defect; 7 = reversable defect

# restecg: resting electrocardiographic results
# - Value 0: normal
# - Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
# - Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria

# thalach: maximum heart rate achieved

# dtype
# age           int64 .
# sex           int64 .
# cp            int64 .
# trestbps      int64 .
# chol          int64 .
# fbs           int64 .
# restecg       int64 .
# thalach       int64 .
# exang         int64 .
# oldpeak     float64 .
# slope         int64 .
# ca            int64 .
# thal          int64 .
# target        int64
# oldpeak_cat 
# {'Risk': 0, 'Terrible': 1, 'Low': 2}
# age_cat 
#  {'senior': 0, 'adult': 1, 'old': 2}
# chol_cat 
#  {'Desirable Level': 0, 'Borderline High Level': 1, 'High Level': 2}

#------------MAIN CODE------------------
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        sex = int(request.form['sex'])
        cp = int(request.form['cp'])
        trestbps = int(request.form['trestbps'])
        age = int(request.form['age'])
        oldpeak = float(request.form['oldpeak'])
        exang = int(request.form['exang'])
        fbs = int(request.form['fbs'])
        restecg = int(request.form['restecg'])
        thalach = int(request.form['thalach'])
        slope = int(request.form['slope'])
        thal = int(request.form['thal'])
        chol = int(request.form['chol'])
        ca = int(request.form['ca'])
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
            
        #---------------PREDICTION--------------------------    

        prediction=int(model.predict([[sex,cp,trestbps,fbs,restecg,thalach,exang,slope,ca,thal,oldpeak,age,chol]]))
        if prediction == 0:
            return render_template('Index.html',prediction_text = "No Presence of heart dissease",output = prediction)
        else:
            return render_template('Index.html',prediction_text="You have a chance of heart dissease", output = prediction)
    else:
        return render_template('Index.html')

if __name__=="__main__":
 app.run(host="localhost", port=8080, debug=True)
