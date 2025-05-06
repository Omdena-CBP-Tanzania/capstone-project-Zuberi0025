import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data

def load_dt():
    df1=pd.read_csv("tanzania_climate_data.csv")
    
    year=df1['Year']
    month=df1['Month']
    rain=df1['Rainfall']
    max=df1['Max_Temp']
    min=df1['Min_Temp']
    return df1

def prepare_features(df1):
    #Prepare features for model Training 
    X=df1.iloc[:,2:6].values
    y=df1.iloc[:,3].values
    return X, y