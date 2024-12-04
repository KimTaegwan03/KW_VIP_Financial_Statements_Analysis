import os
import pandas as pd
from fancyimpute import SoftImpute

class FinDataLoader:
    def __init__(self,path):
        self.path = path
        self.stock_list = {}
        
        with open(f"{path}/kospi_50.txt", 'r') as f:
            for line in f:
                code, name = line.strip().split(',')
                self.stock_list[code] = name
                
    def get_statement(self, code, year, quarter):
        
        if os.path.isfile(f"{self.path}/{code}.csv"):
            df_fs = pd.read_csv(f"{self.path}/{code}.csv")
            
            df_fs = df_fs[df_fs['분기'] == quarter]
            df_fs = df_fs[df_fs['연도'] == year]
            
            return df_fs
        else:
            print(f"파일이 존재하지 않습니다: {self.path}/{code}.csv")
            return pd.DataFrame()
        
    def data_processing(self, code):
        if os.path.isfile(f"{self.path}/{code}.csv"):
            df_fs = pd.read_csv(f"{self.path}/{code}.csv")
            
            df_yq = pd.DataFrame(df_fs.loc[:,["연도","분기"]])
            
            df_fs.drop(columns=["연도","분기"],inplace=True)
            
            col = df_fs.columns
            
            impute = SoftImpute(verbose=False)
            
            df_impute = impute.fit_transform(df_fs)
            
            df_impute = pd.DataFrame(df_impute, columns=col).pct_change()
            
            df_concat = pd.concat([df_yq, df_impute],axis=1).dropna()
            
            df_concat.to_csv(f"{self.path}/preprocessed/{code}.csv",index=False, encoding='utf-8-sig')
        
        
if __name__ == "__main__":
    data = FinDataLoader("data")
    
    for code,_ in data.stock_list.items():
        data.data_processing(code)