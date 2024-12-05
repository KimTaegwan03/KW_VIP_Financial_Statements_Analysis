from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd
from FinDataLoader import FinDataLoader
import joblib
import pickle

DL = FinDataLoader()
code = '005930'

data = DL(code,30)

data_len = len(data)


train_data = data.iloc[:int(data_len*0.6),1:]
valid_data = data.iloc[int(data_len*0.6):int(data_len*0.8),1:]
test_data = data.iloc[int(data_len*0.8):,1:]

print(train_data)
print(valid_data)
print(test_data)

rgr = RandomForestRegressor()
rgr = rgr.fit(train_data.iloc[:,:-1],train_data.iloc[:,-1])

with open(f'{code}_model.pkl', 'wb') as f:
    pickle.dump(rgr, f)

pred = rgr.predict(valid_data.iloc[:,:-1])

print(f"Mean Squared Error : {mean_squared_error(valid_data.iloc[:,-1],pred):.4f}")

