import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data
def load_data():
    #create dates for the year
    dates=pd.date_range(start='2010-01-01',end='2024-12-31',freq='ME')
    #Generate temperature
    temps=[]
    for i in range(len(dates)):
        seasonal=15+10*np.cos(2*np.pi*1/12)
        trend=0.03*i
        noise=np.random.normal(0,1.5)
        temps.append(seasonal+trend+noise)
    df=pd.DataFrame({"dates":dates,"temperature":temps})
    df['year']=df['dates'].dt.year
    df['month']=df['dates'].dt.month
    df['day']=df['dates'].dt.day
    return df

def prepare_features(df):
    #Prepare features for model Training 
    X=df[['year','month']].values
    y=df['temperature'].values
    return X, y