import streamlit as st
import numpy as np
import pandas as pd
from model_utils import load_model
from visualize import plot_prediction_context
from predict import make_prediction,get_historical_context,get_historical_average

def show(df1):
    """Display the prediction page"""
    st.header("Rainfall predictions")
    #Chek if the model exit
    if 'model' not in st.session_state:
        model=load_model()
        if model in None:
            st.warning("No training model go back to model training")
            st.stop()
        st.session_state['model']=model
        st.session_state['model_type']='Pre_trained model'
    #show the used model
    st.info(f"Using{st.session_state['model_type']} for prediction")
    
    #Prediction Input
    st.subheader("select date for prediction")
    pred_year=st.slider("Year",2000,2100,2010)
    pred_month=st.slider("month",1,12,6)
    pred_month=st.slider("Day",1,31,15)
    pred_max=st.slider("Max_temp",20,32,25)
    #pred_max=st.sidebar.slider("Max_Temp (°C)",min_value=float( df1['TMX'].min(),max_value=float(df1['TMX'])))
    pred_min=st.slider("Min_Temp",18,25,20) 
    #Make prediction
    if st.button("Predict Rainfall"):
        model=st.session_state['model']
        prediction=make_prediction(model,pred_year,pred_month,pred_max,pred_min)
        #Dipslay results
        st.success(f"Predicted Rainfall for {pred_year}-{pred_month:02d}:{prediction:.2f}")
        
        #Historical compare
        hist_avg=get_historical_average(df1,pred_month)
        st.write(f"historical average for month{pred_month}:{hist_avg:.2f}")
        
        #Calculate the difference
        diff=prediction-hist_avg
        if diff >0:
            st.write(f"Prediction is {diff:.2f} **higher** than the historical average")  
        else:
            st.write(f"Prediction is {abs(diff):.2f} **lower** than the historical average")
            
        #VISUALIZE
        st.subheader("Prediction in historical context")
        
        #Get the context
        hist_temps=get_historical_context(df1,pred_month)
        
        #Plot
        fig=plot_prediction_context(hist_temps,pred_year,pred_month,prediction)
        st.pyplot(fig)                  