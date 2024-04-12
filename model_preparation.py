import pandas as pd
from sklearn.svm import SVR
import joblib


preprocessed_train_data = pd.read_csv('train/preprocessed_train_data.csv')

model = SVR(kernel='rbf', C=100, gamma=0.1)
model.fit(preprocessed_train_data[['x']], preprocessed_train_data['y'])

joblib.dump(model, 'model.joblib')
