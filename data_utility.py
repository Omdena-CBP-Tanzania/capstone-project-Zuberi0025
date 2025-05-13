import pandas as pd
import numpy as np
import streamlit as st
from sklearn.preprocessing import MinMaxScaler
@st.cache_data

def load_dt():
    df1=pd.read_csv("stationX.csv")
    
    year=df1['Year']
    month=df1['Month']
    Yield=df1['Rainfall']
    avg=df1['AVG']
    max=df1['TMX']
    min=df1['TMN']
    #spi=df1['SPI']
    return df1

def prepare_features(df1):
    #Prepare features for model Training 
    X=df1.iloc[:,2:6].values
    y=df1.iloc[:,1].values
    return X, y

