import streamlit as st
import matplotlib.pyplot as plt
#st.title('My App')
#st.write('Hello Tanzania') 
from pages import data_exploration, model_training,prediction_page
from data_utilis import load_data

#set configurations
st.set_page_config(
    page_title="Climate Trend Prediction",page_icon='',layout="wide"
)
#LOAD DATA
df=load_data()
#Give the title and desciption
st.title("Climate Trend Analyis and Prediction")
st.markdown(" Analysis historical temperature and predict future trends")
st.sidebar.title("RESOURCES")
page=st.sidebar.radio("Go to",['Data Exploration','Model Training','Prediction'])
#Display selected page
if page =="Data Exploration":
    data_exploration.show(df)
elif page =="Model Training":
    model_training.show(df)
else:
    prediction_page.show(df)
    
