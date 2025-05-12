import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data

def load_dt():
    df1=pd.read_csv("stationX.csv")
    
    year=df1['Year']
    month=df1['Month']
    Yield=df1['Rainfall']
    day=df1['Date']
    max=df1['TMX']
    min=df1['TMN']
    #spi=df1['SPI']
    return df1

def prepare_features(df1):
    #Prepare features for model Training 
    X=df1.iloc[:,3:6].values
    y=df1.iloc[:,3].values
    return X, y