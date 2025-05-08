import streamlit as st
from pages import data_explore, model_train,prediction_view
from data_utility import load_dt

#set configurations
st.set_page_config(
    page_title="Climate Trend Prediction",page_icon='',layout="wide"
)
#LOAD DATA
df1=load_dt()
#Give the title and desciption
st.title("Climate Trend Analyis and Prediction")
st.markdown(" Analysis historical Rainfall and predict future trends")
st.sidebar.title("RESOURCES")
page=st.sidebar.radio("Go to",['Data Analysis','Model Train','Prediction'])
#Display selected page
if page =="Data Analysis":
    data_explore.show(df1)
elif page =="Model Train":
    model_train.show(df1)
else:
    prediction_view.show(df1)
    