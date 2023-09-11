import os
import sys
import pickle
import numpy as np 
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

from src.exception import CustomException
from src.logger import logging

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)  #os.path.dirname - it gives the the path of folder in which file or folder is present for which the path is given
                                               #for path = '/home/User/Documents' it gives /home/User
                                               #for this /home/User/Documents/file.txt it gives /home/User/Documents

        os.makedirs(dir_path, exist_ok=True)   #it will create the directory specified if not exist , if exist it shows error
                                               #if exist_ok is False
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)         #pickle.dump - to serialize the file
                                               #pickle.load - to deserialize the serialized file

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            # Train model
            model.fit(X_train,y_train)

            

            # Predict Testing data
            y_test_pred =model.predict(X_test)

            # Get R2 scores for train and test data
            #train_model_score = r2_score(ytrain,y_train_pred)
            test_model_score = r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]] =  test_model_score

        return report

    except Exception as e:
        logging.info('Exception occured during model training')
        raise CustomException(e,sys)
    
def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info('Exception Occured in load_object function utils')
        raise CustomException(e,sys)

    