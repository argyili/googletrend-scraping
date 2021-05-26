# from .pytrends.request import TrendReq
import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq(hl='ja-jp',tz=540)

kw_list = ['花粉症']

# For complete daily data, gain one year data by two times.
# Tokyo's code is JP-13
pytrend.build_payload(kw_list, timeframe='2018-01-01 2018-06-30', geo='JP-13')
df_tokyo_1 = pytrend.interest_over_time()
pytrend.build_payload(kw_list, timeframe='2018-07-01 2018-12-30', geo='JP-13')
df_tokyo_2 = pytrend.interest_over_time()
df_tokyo = pd.concat([df_tokyo_1, df_tokyo_2])
df_tokyo.columns = ['Tokyo']

# Osaka's code is JP-27
pytrend.build_payload(kw_list, timeframe='2018-01-01 2018-06-30', geo='JP-27')
df_osaka_1 = pytrend.interest_over_time()
pytrend.build_payload(kw_list, timeframe='2018-07-01 2018-12-30', geo='JP-27')
df_osaka_2 = pytrend.interest_over_time()
df_osaka = pd.concat([df_osaka_1, df_osaka_2])
df_osaka.columns = ['Osaka']

df = pd.concat([df_tokyo, df_osaka], axis=1)
df.index.name = None

with pd.ExcelWriter('pollen_tokyo-osaka.xlsx', date_format='YYYY-MM-DD') as writer:
    df.to_excel(writer)