# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 19:57:48 2021

@author: kanwal 
"""
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def main():
    """All Ml Projects in One """
    
    st.title(" All in one Web App")
    
    sectors = ["Health Care", "Finance", "Open CV"]
    choice = st.sidebar.selectbox("Select your sector", sectors)
    
    hc_models = ["Heart Disease", "Cancer"]
     
        
    if choice == 'Health Care':
        st.subheader("Welcome to Healthcare Section")
        hc_choice = st.sidebar.radio("Select your sector", hc_models)
        if hc_choice == 'Heart Disease':
            st.subheader('Know your heart health')
        
        if hc_choice == 'Cancer':
            st.subheader('Please check your health')
            
    
    if choice == 'Finance':
        st.subheader('Welcome to finance section')
        
    
    if choice == 'Open CV':
        st.subheader('Welcome to the world of Artificial Intelligence')


if __name__ == '__main__':
	main()
