import pandas as pd
from pandas.io.pytables import IndexCol
import csv
from pandas.core.frame import DataFrame

if __name__ == '__main__':
    totalDf = pd.DataFrame()
    for i in range(54):
        df = pd.read_excel('ame_master.xlsx', sheet_name=i+3, usecols=[1,3,6,7,8,9], header = None)
        # df = pd.read_excel('ame_master.xlsx', sheet_name=i+3, usecols=[1,6,7,8,9], header = None, index_col=0)
        df = df.drop(df.index[[0,1,2]])
        totalDf = pd.concat([totalDf, df], axis=0)

    totalDf = totalDf.reset_index(drop=True)
    totalDf.columns=['index','name','laDegree','laMinute','loDegree','loMinute']
    totalDf.to_csv('geoData.csv', index=False)
    print(totalDf)
    

