import streamlit as st
import matplotlib.pyplot as plt
from visualization import plot_time_series,plot_seasonal_pattern,plot_actual_vs_predicted,plot_yearly_trends,plot_prediction_context
def show(df):
    """
    Display the data exploartion page
    
    """
    st.header('Data Exploration')
    st.subheader("Raw temperature Data")
    st.dataframe(df.head(10))
    st.subheader("Statistical summary")
    st.write(df['temperature'].describe())
    
    #
    st.subheader("Temperature Over time")
    fig=plot_time_series(df)
    st.pyplot(fig)
    st.subheader("Seasonal temperature patterns")
    fig=plot_seasonal_pattern(df)
    st.pyplot(fig)
    st.subheader("Yearly Avg temp")
    fig=plot_yearly_trends(df)
    st.pyplot(fig)