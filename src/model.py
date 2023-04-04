import pickle
import os
import numpy as np
from sklearn.ensemble import RandomForestRegressor

current_path = os.path.dirname(os.path.realpath(__file__))

target_dict = {0: 'Đúng hạn', 1: 'Quá hạn'}

# with open('model/model_best.pkl', 'rb') as file:
#     model = pickle.load(file) # importing model to predict

def get_prediction(model, data):
    pred = model.predict_proba(data)
    return pred
