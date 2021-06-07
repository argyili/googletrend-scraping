# from .pytrends.request import TrendReq
from pytrends.request import TrendReq
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def interest_over_time(kw_list, place):
    pytrend.build_payload(kw_list, timeframe='2018-01-01 2018-12-30', geo=place)
    df = pytrend.interest_over_time()
    # # The google trend data is not absoluted, so we can not get data for multiple times without decorating.
    # pytrend.build_payload(kw_list, timeframe='2018-01-01 2018-06-30', geo=place)
    # df_1 = pytrend.interest_over_time()
    # pytrend.build_payload(kw_list, timeframe='2018-07-01 2018-12-30', geo=place)
    # df_2 = pytrend.interest_over_time()
    # df = pd.concat([df_1, df_2])
    return df

if __name__ == '__main__':
    
    pytrend = TrendReq(hl='ja-jp',tz=540)
    kw_list = ['花粉症']

    pytrend.build_payload(kw_list, timeframe='2019-02-01 2019-06-30', geo='JP-27')
    # print(pytrend.interest_over_time())

    # # Tokyo's code is JP-13
    # df_tokyo = interest_over_time(kw_list, 'JP-13')
    # df_tokyo.columns = ['Tokyo']
    # # Osaka's code is JP-27
    # df_osaka = interest_over_time(kw_list, 'JP-27')
    # df_osaka.columns = ['Osaka']

    # df = pd.concat([df_tokyo, df_osaka], axis=1)
    # df.index.name = None
    # df.plot()
    # plt.savefig('./pollen_tokyo-osaka.jpg')

    # with pd.ExcelWriter('pollen_tokyo-osaka.xlsx', date_format='YYYY-MM-DD') as writer:
    #     df.to_excel(writer)

    print(pytrend.interest_by_region(resolution='CITY', inc_low_vol=True))