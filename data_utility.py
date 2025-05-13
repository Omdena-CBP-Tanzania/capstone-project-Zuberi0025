import pandas as pd
import numpy as np
import streamlit as st
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
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
    X=df1.iloc[:,1:6].values
    y=df1.iloc[:,1].values
    return X, y

##Prepare features for LSTM Model

##Normalize data for LSTM Model
def normalize_data(X):
    scaler=MinMaxScaler()
    X_scaled=scaler.fit_transform(X)
    n_past=30
    return X_scaled,scaler
def createXY(df,n_past):
    """Create a sequence of past observations X and their corresponding next values Y"""
    if not isinstance(df,np.ndarray):
        raise ValueError("Input dataset should be array")
    if len(df.shape)!=2:
        raise ValueError("Input data must be 2D")
    if n_past>=len(df):
        raise ValueError("n_past must be smaller than the dataset length")
    
    dataX,dataY=[],[]
    for i in range(n_past,len(df)):
        dataX.append(df[i-n_past:i,0:df.shape[1]])
        dataY.append(df[i,0])
    return np.array(dataX),np.array(dataY)  