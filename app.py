from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('DecisionTreeRegressor.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        T = float(request.form['T'])
        TM=float(request.form['TM'])
        Tm=float(request.form['Tm'])
        SLP=float(request.form['SLP'])
        H=float(request.form['H'])
        VV=float(request.form['VV'])
        V=float(request.form['V'])
        VM=float(request.form['VM'])
        prediction=model.predict([[T,TM,Tm,SLP,H,VV,V,VM]])
        result=round(prediction[0],2)
        output = ""
        if result>=0 and result <= 12:
            return  render_template('index.html',prediction_texts="GOOD")
        elif result>=12.1 and result<=35.4:
            return render_template('index.html',prediction_text="MODERATE")
        elif result>=35.5 and result<=55.4:
            return render_template('index.html',prediction_text = "Unhealthy for Sensitive Groups")
        elif result>=55.5 and result<=150.4:
            return render_template('index.html',prediction_text="Unhealthy")
        elif result>=150.5 and result<=250.4:
            return render_template('index.html',prediction_text="Very Unhealthy")
        elif result>=250.5 and result<=500.4:
            return render_template('index.html',prediction_text="Hazardous")
        else:
            return render_template('index.html',prediction_text="TOO MUCH DANGEROUS!!")
        
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)