import numpy as np
import pickle
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,root_mean_squared_error,r2_score

#Data split
def split_data(X,y,test_size=0.2):
    """Split data into train and test sets"""
    return train_test_split(X,y,test_size=test_size,random_state=42)
def train_model(X_train,y_train,model_type="Linear Regression Model"):
    """Train the model based on the specified type of the model"""
    if model_type=="Linear Regression":
        model=LinearRegression()
    else:
        model=RandomForestRegressor(n_estimators=150,random_state=42)
    model.fit(X_train,y_train)
    return model

def evaluate_model(model,X_train,y_train,X_test, y_test):
    """Evaluate the model performance"""
    y_pred_train=model.predict(X_train)
    y_pred_test=model.predict(X_test)
    #calculate metrics
    metrics={"train_rmse":root_mean_squared_error(y_train,y_pred_train),
              'test_rmse':root_mean_squared_error(y_test,y_pred_test),
              'train_r2': r2_score(y_train,y_pred_train),
              'test_r2':r2_score(y_test,y_pred_test),
              'y_test': y_test,
              'y_pred_test':y_pred_test}  
    return metrics

#Save the model
def save_model(model,filename="climate_model.jbl"):
    """Save the model to disk"""
    with open(filename,'wb')as file:
        joblib.dump(model,file)
        
#Load the model
def load_model(filename='climate_model.jbl') :
    try:
        with open(filename,'rb') as file:
            model=joblib.load(file)
        return model
    except FileNotFoundError:
        return None     