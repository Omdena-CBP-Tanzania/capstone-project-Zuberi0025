import streamlit as st
from visualize import plot_time_series,plot_seasonal_pattern,plot_actual_vs_predicted,plot_yearly_trends,plot_prediction_context
def show(df1):
    """
    Display the data exploartion page
    
    """
    st.header('Data Exploration')
    st.subheader("Raw Rainfall and Temperature Data")
    st.dataframe(df1.head(10))
    st.subheader("Statistical summary")
    st.write(df1['Rainfall'].describe())
    
    #
    st.subheader("Rainfall Over time")
    fig=plot_time_series(df1)
    st.pyplot(fig)
    st.subheader("Seasonal Rainfall patterns")
    fig=plot_seasonal_pattern(df1)
    st.pyplot(fig)
    st.subheader("Yearly Avg temp")
    fig=plot_yearly_trends(df1)
    st.pyplot(fig)