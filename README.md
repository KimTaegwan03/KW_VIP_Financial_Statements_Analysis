# 데이터
## 기간
- 2016년 1분기 ~ 2024년 3분기
  - 과거 데이터의 경우 종목에 따라 가격 및 재무제표 데이터가 존재하지 않음
#### Train 데이터
- 존재하는 데이터 중 과거 60%

#### Valid 데이터
- Train 데이터 이후 20%

#### Test 데이터
- 존재하는 데이터 중 최근 20%

## 종목
- 2024/11 [코스피50 종목](https://github.com/KimTaegwan03/KW_VIP_Financial_Statements_Analysis/blob/master/data/kospi_50.txt)의 기술적지표 및 분기재무제표 데이터

## 기술적지표
- stockstats 라이브러리 사용
- SMA 10, 20, 60
- EMA 10, 20, 60

## 분기재무제표
- OpenDartReader 라이브러리 사용
- 비유동자산, 자산총계, 유동부채, 비유동부채, 부채총계, 이익잉여금, 자본총계, 매출액, 영업이익, 법인세차감전 순이익, 당기순이익, 당기순이익(손실), 총포괄손익, 자본금

## 전처리
#### 기술적지표
- 수집한 기술적지표들을 각 날짜의 종가로 나눈 값 사용 (load_price_data 함수)

#### 분기재무제표
- 재무제표 항목에 결측값이 존재하기 때문에 Soft Imputation을 사용하여 보간 (data_processing 함수)
- 직전분기 대비 각 항목의 변화율을 사용하여 추세를 반영 (data_processing 함수)

#### 기술적지표 + 분기재무제표
- 일일 기술적지표 데이터에 대해 해당 되는 분기의 재무제표 데이터를 연결 (map_financial_to_price 함수)

# 학습 및 평가
#### 모델
- Sklearn의 RandomForestRegressor 사용

#### 종목
- SK하이닉스(000660)

#### 학습 결과
- 모델로부터 특징 중요도를 추출함
![특징중요도](https://github.com/user-attachments/assets/27a4d100-b06b-4f5e-aef6-b60cb86234ea)

#### 평가
- Valid 데이터에 대한 MSE : 0.0183

#### 테스트
![SK하이닉스 백테스트 매수 매도](https://github.com/user-attachments/assets/bdc884f3-ae42-47f1-a8bc-a79d117320e1)

