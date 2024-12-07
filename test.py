from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from FinDataLoader import FinDataLoader
import pickle
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

def signal_marking(code,pred:pd.Series,alpha,beta):
    # alpha는 매수 신호 임계값, beta는 매도 신호 임계값
    
    df_price = pd.read_csv(f"data/price/{code}.csv",index_col=[0])['Close']
    
    df_price = df_price[pred.index]
    
    buy_signal = pd.Series([0]*len(pred),index=pred.index)
    sell_signal = pd.Series([0]*len(pred),index=pred.index)
    
    # 예측이 alpha 이상이면 매수 신호, beta 이하이면 매도 신호
    for date,date_pred in pred.items():
        if date_pred >= alpha:
            buy_signal[date] = 1
            
        if date_pred <= beta:
            sell_signal[date] = 1
            
    buy_signal = buy_signal[buy_signal == 1]
    sell_signal = sell_signal[sell_signal == 1]
    
    # 종가 그래프
    plt.plot(df_price)
    
    # 매수 매도 신호
    for idx in buy_signal.index.tolist():
        plt.plot(idx,df_price[idx],"g^",markersize=10)
        
    for idx in sell_signal.index.tolist():
        plt.plot(idx,df_price[idx],"rv",markersize=10)
    
    # X축 레이블 수 줄이기
    for i, tick in enumerate(plt.gca().axes.xaxis.get_ticklabels()):
        if i % 30 != 0:
            tick.set_visible(False)
    
    plt.xticks(rotation=45)
    plt.show()
    

# 데이터 불러오기
DL = FinDataLoader()
code = '000660'
data = DL(code,30)
data_len = len(data)
test_data = data.iloc[int(data_len*0.8):,1:]

# 모델 불러오기
with open(f'{code}_model.pkl','rb') as f:
    model:RandomForestRegressor = pickle.load(f)

# 특징 중요도 추출 및 시각화
# imp = pd.Series(model.feature_importances_,test_data.iloc[:,:-1].columns).sort_values(ascending=True)
# plt.barh(imp.index,imp.values)
# plt.show()

# 테스트 기간에 대한 예측
pred = model.predict(test_data.iloc[:,:-1])
sr_pred = pd.Series(pred,test_data.index)

print(f"Mean Squared Error : {mean_squared_error(test_data.iloc[:,-1],pred):.4f}")

# 예측 결과를 사용해 테스트 기간의 매수, 매도 시그널 시각화
signal_marking(code,sr_pred,0.1,-0.05)
