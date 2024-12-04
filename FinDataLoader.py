import os
import pandas as pd

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
        
        
if __name__ == "__main__":
    data = FinDataLoader("data")
    
    print(data.get_statement("005930",2018,"Q2"))