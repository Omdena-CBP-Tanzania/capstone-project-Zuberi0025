import streamlit as st
from data_utility import prepare_features
from visualize import plot_actual_vs_predicted
from model_utils import split_data,train_test_split,evaluate_model,load_model,save_model,train_model

def show(df1):
    st.header("Model training")
    #Preapre features
    X,y =prepare_features(df1)
    
    test_size=st.slider("Test data size(%)",10,30,20)/100
    X_train,X_test,y_train,y_test=split_data(X,y,test_size)
    
    st.write(f"Training Data:{len(X_train)} samples")
    st.write(f"Testing Data:{len(X_test)} samples")
    
    model_type=st.selectbox("Select the model type",['Linear Regression','Random Forest'])
    
    #Train the model
    if st.button("Train model"):
        with st.spinner("Training in progress"):
            model=train_model(X_train,y_train,model_type)
            metrics=evaluate_model(model,X_train,y_train,X_test,y_test)
            col1,col2=st.columns(2)
            with col1:
                st.subheader("Training Metrics")
                st.write(f"RMSE:{metrics['train_rmse']:.2f} mm")
                st.write(f"R2:{metrics['train_r2']:4f}")
            with col2:
                st.subheader("Testing Metrics")
                st.write(f"RMSE:{metrics['test_rmse']:.2f} mm")
                st.write(f"R2:{metrics['test_r2']:4f}")
                
            #Plot actual vs predicted
            st.subheader('Actual Vs Predicted (test data)')
            fig=plot_actual_vs_predicted(metrics['y_test'],metrics['y_pred_test'])
            st.pyplot(fig)
            
            #SAVE model
            save_model(model)
            st.success('Model trained has saved successfully')
            st.session_state['model']=model
            st.session_state['model_type']=model_type               
    