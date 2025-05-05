import numpy as np
import pandas as pd

#Prediction function
def make_prediction(model,year,month):
    """Temp prediction for given year and month"""
    features=np.array([[year,month]])
    return model.predict(features)[0]

#Get Historical context
def get_historical_context(df, month):
    years=df['year'].unique()
    hist_temps=[]
    
    for year in years:
        month_data=df[(df['year']==year)&(df['month']==month)]
        if not month_data.empty:
            hist_temps.append((year,month_data['temperature'].values[0]))
    return hist_temps

def get_historical_average(df,month):
    return df[df['month']==month]['temperature'].mean()
