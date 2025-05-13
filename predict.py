import numpy as np
import pandas as pd

#Prediction function
def make_prediction(model,year,month,avg,max,min):
    """Rainfall prediction for given year and month"""
    features=np.array([[year,month,avg,max,min]])
    return model.predict(features)[0]

#Get Historical context
def get_historical_context(df1, month):
    years=df1['Year'].unique()
    hist_temps=[]
    
    for year in years:
        month_data=df1[(df1['Year']==year)&(df1['Month']==month)]
        if not month_data.empty:
            hist_temps.append((year,month_data['Rainfall'].values[0]))
    return hist_temps

def get_historical_average(df,month):
    return df[df['Month']==month]['Rainfall'].mean()
