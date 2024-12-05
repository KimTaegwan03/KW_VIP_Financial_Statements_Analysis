from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from FinDataLoader import FinDataLoader
import pickle
import pandas as pd

DL = FinDataLoader()
code = '005930'

data = DL(code,30)

data_len = len(data)

train_data = data.iloc[:int(data_len*0.6),1:]
valid_data = data.iloc[int(data_len*0.6):int(data_len*0.8),1:]
test_data = data.iloc[int(data_len*0.8):,1:]

with open(f'{code}_model.pkl','rb') as f:
    model = pickle.load(f)
    
pred = model.predict(test_data.iloc[:,:-1])

sr_pred = pd.Series(pred,test_data.index)

print(sr_pred)
print(f"Mean Squared Error : {mean_squared_error(test_data.iloc[:,-1],pred):.4f}")