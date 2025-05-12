import streamlit as st
from visualize import plot_time_series1,plot_time_series2
from visualize import plot_time_series,plot_seasonal_pattern,plot_actual_vs_predicted,plot_yearly_trends,plot_prediction_context
def show(df1):
    """
    Display the data exploartion page
    
    """
    st.header('EDA')
    st.subheader("Rainfall and Temperature Data")
    st.dataframe(df1.head(5))
    st.subheader("Statistical summary")
    st.write(df1['Rainfall'].describe())
    st.write(df1['TMX'].describe())
    st.write(df1['TMN'].describe())
    st.write(df1['AVG'].describe())    
    #VISUALIZE
    st.subheader("Rainfall Over time")
    fig=plot_time_series(df1)
    st.pyplot(fig)
    st.subheader('Maximum temperature')
    fig=plot_time_series1(df1)
    st.pyplot(fig)
    st.subheader('Minimum temperature')
    fig=plot_time_series2(df1)
    st.pyplot(fig)
    st.subheader("Seasonal Rainfall patterns")
    fig=plot_seasonal_pattern(df1)
    st.pyplot(fig)
    st.subheader("Yearly Avg Rainfall")
    fig=plot_yearly_trends(df1)
    st.pyplot(fig)