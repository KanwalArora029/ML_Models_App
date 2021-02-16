# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 19:57:48 2021

@author: kanwal 
"""
from flask import Flask, request, render_template, url_for
from pickle import load
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

model = open('models/cancer_model.pkl','rb')
forecast = load(model)

app = Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return (render_template('index.html'))


@app.route('/healthcare')
def healthcare():
    return(render_template(
        'healthcare.html',
        title="Health Care",
        description="Welcome to Health Care section"))

@app.route('/cancer', methods=['GET'])
def cancer():
    return(render_template('cancer.html',
                                 title = 'Breast Cancer Prediction',
                                 description = "Enter the details to check the type of Breast Cancer"))

@app.route('/cancer_predict', methods=['GET', 'POST'])
def check_cancer():    
    if request.method =='POST':
        
        input_features = [float(x) for x in request.form.values()]
        features_value = [np.array(input_features)]
        
        features_name = ['radius_mean', 'texture_mean', 'smoothness_mean',
                         'compactness_mean', 'symmetry_mean', 'fractal_dimension_mean',
                         'radius_se', 'texture_se', 'smoothness_se', 'compactness_se',
                         'symmetry_se', 'fractal_dimension_se'
                         ]
        
        df = pd.DataFrame(features_value, columns=features_name)
        output = forecast.predict(df)
        
        if output == 0:
            res_val = "** No breast cancer **"
        else:
           res_val = "breast cancer"
           
        return render_template('cancer.html', 
                               prediction_text='Patient has {}'.format(res_val),
                               title = 'Breast Cancer Prediction',
                               description = "Enter the details to check the type of Breast Cancer")
        

@app.route('/finance')
def finance():
    return(render_template(
        'finance.html',
        title="Finance",
        description="Welcome to Finance section"))

@app.route('/aggriculture')
def aggriculture():
    return(render_template(
        'aggriculture.html',
        title="Aggriculture",
        description="Welcome to Aggriculture section"))

@app.route('/opencv')
def opencv():
    return(render_template(
        'opencv.html',
        title="Open CV",
        description="Welcome to Open CV section"))


if __name__ == '__main__':
	app.run(debug=True)
