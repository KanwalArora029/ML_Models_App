# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 19:57:48 2021

@author: kanwal 
"""
import flask
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler




app = flask.Flask(__name__, template_folder='templates')
@app.route('/')
def main():
    return (flask.render_template('index.html'))


@app.route('/healthcare')
def healthcare():
    return(flask.render_template(
        'healthcare.html',
        title="Health Care",
        description="Welcome to Health Care section"))

@app.route('/cancer')
def cancer():
    return(flask.render_template('cancer.html',
                                 title = 'Breast Cancer Prediction',
                                 description = "Predict the type of Breast Cancer"))

@app.route('/finance')
def finance():
    return(flask.render_template(
        'finance.html',
        title="Finance",
        description="Welcome to Finance section"))

@app.route('/aggriculture')
def aggriculture():
    return(flask.render_template(
        'aggriculture.html',
        title="Aggriculture",
        description="Welcome to Aggriculture section"))

@app.route('/opencv')
def opencv():
    return(flask.render_template(
        'opencv.html',
        title="Open CV",
        description="Welcome to Open CV section"))


if __name__ == '__main__':
	app.run(debug=True)
