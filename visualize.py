import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_time_series(df1):
    fig,ax=plt.subplots(figsize=(8,5))
    ax.scatter(df1['Year'],df1['Rainfall'],color='k')
    ax.set_xlabel("Year")
    ax.set_ylabel("Rainfall(mm)")
    ax.set_title("Monthly Rainfall")
    ax.grid(False)
    return fig

def plot_time_series1(df1):
    fig,ax=plt.subplots(figsize=(8,5))
    ax.scatter(df1['Year'],df1['TMX'],color='r')
    ax.set_xlabel("Year")
    ax.set_ylabel("Temperature")
    ax.set_title("Maximum temperature")
    return fig

def plot_time_series2(df1):
    fig,ax=plt.subplots(figsize=(8,5))
    ax.scatter(df1['Year'],df1['TMN'],color='g')
    ax.set_xlabel("Year")
    ax.set_ylabel("Temperature")
    ax.set_title("Minimum temperature")
    return fig
def plot_seasonal_pattern(df1):
    
    """"Monthly Rainfall distribution"""
    fig,ax=plt.subplots(figsize=(8,5))
    avg=df1.groupby('Month')['Rainfall'].mean().reset_index()
    ax.plot(avg["Month"],avg["Rainfall"],marker='o',color='green')
    ax.set_xlabel("Month")
    ax.set_ylabel("Rainfall")
    ax.set_title("Monthly Rainfall distribution")
    ax.grid(False)
    return fig


def plot_yearly_trends(df1):
    year_avg=df1.groupby('Year')['Rainfall'].mean().reset_index()
    fig,ax=plt.subplots(figsize=(8,5))
    ax.plot(year_avg['Year'],year_avg['Rainfall'],marker='o')
    ax.set_xlabel("Year")
    ax.set_ylabel("Rainfall(mm)")
    ax.set_title("Total Yearly Rainfall")
    ax.grid(False)
    return fig
    
def plot_actual_vs_predicted(y_test,y_pred):
    """Plot the actual vs predicted values"""
    fig,ax=plt.subplots(figsize=(8,5))
    ax.scatter(y_test,y_pred,alpha=0.7)
    ax.plot([min(y_test),max(y_test)],[min(y_test),max(y_test)],'r--')
    ax.set_xlabel("Actual Rainfall")
    ax.set_ylabel("Predicted Rainfall")
    ax.set_title("Actual Vs Predicted Rainfall")
    return fig
 
def plot_prediction_context(hist_temps,pred_year,pred_month,prediction):
    years_hist,temp_hist=zip(*hist_temps)
    fig,ax=plt.subplots(figsize=(8,5))
    ax.scatter(years_hist,temp_hist,label=f"Historical(month{pred_month})",color="red")
    ax.plot(years_hist,temp_hist,'b--',alpha=0.6)
    ax.scatter([pred_year],[prediction],color='blue',s=100,label='prediction')
    return fig
     