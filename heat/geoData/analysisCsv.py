import pandas as pd
from pandas.io.pytables import IndexCol
import csv
from pandas.core.frame import DataFrame

if __name__ == '__main__':
    df = pd.read_csv('geoData.csv')
    former = 0
    list = []
    for row in df.itertuples():
        if former == getattr(row, 'index'):
            list.append(str(getattr(row, 'index')) + ' ' +  str(getattr(row, 'name')))
            # print(getattr(row, 'index'), getattr(row, 'name'))
        former = getattr(row, 'index')
        # print(type(getattr(row, 'index')))

    with open('repeatedCity.txt', 'a+') as f:
        for city in list:
            f.write(city + '\n')

