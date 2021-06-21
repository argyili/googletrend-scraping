import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os

def searchDate(address, temp_date_day, temp_date_night):
    page = requests.get(address)

    soup = BeautifulSoup(page.content, 'html.parser')
    region = soup.find(class_="data selected").text

    yy = []
    mm = []
    dd = []
    for el in soup.find_all(class_= "yy"):
        yy.append(el.text)
    for el in soup.find_all(class_= "mm"):
        mm.append(el.text)
    for el in soup.find_all(class_= "dd"):
        dd.append(el.text)
    
    date = []
    for i in range(len(yy)):
        if yy[i] == '年':
            continue
        date.append(datetime.date(int(yy[i]), int(mm[i]), int(dd[i])))
        
    # del(date[0])
    midLen = len(date) // 2
    date_day = pd.DataFrame(date[1:midLen])
    date_day.columns=['']
    date_night = pd.DataFrame(date[midLen + 1:])
    date_night.columns=['']

    return date_day, date_night

def searchRegion(address, temp_date_day, temp_date_night):
    page = requests.get(address)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    region = soup.find(class_="data selected").text

    temp = []
    for el in soup.find_all(class_= re.compile("data map_ct_lv" + "."  + " selected")):
        temp.append(float(el.text))
    
    midLen = len(temp) // 2
    temp_day = pd.DataFrame(temp[:midLen])
    temp_night = pd.DataFrame(temp[midLen:])
    temp_day.columns=[region]
    temp_night.columns=[region]

    temp_date_day = pd.concat([temp_date_day, pd.DataFrame(temp_day)], axis=1)
    temp_date_night = pd.concat([temp_date_night, pd.DataFrame(temp_night)], axis=1)

    return temp_date_day, temp_date_night

if __name__ == '__main__':

    temp_date_day = pd.DataFrame()
    temp_date_night = pd.DataFrame()

    # 天気
    temp_date_day, temp_date_night = searchDate('https://www.wbgt.env.go.jp/doc_trendcal.php?region=07&prefecture=62&point=62016&tab=5', temp_date_day, temp_date_night)

    # 能勢
    temp_date_day, temp_date_night = searchRegion('https://www.wbgt.env.go.jp/doc_trendcal.php?region=07&prefecture=62&point=62016&tab=5', temp_date_day, temp_date_night)

    # 枚方
    temp_date_day, temp_date_night = searchRegion('https://www.wbgt.env.go.jp/doc_trendcal.php?region=07&prefecture=62&point=62046&tab=5', temp_date_day, temp_date_night)

    # 大阪
    temp_date_day, temp_date_night = searchRegion('https://www.wbgt.env.go.jp/doc_trendcal.php?region=07&prefecture=62&point=62078&tab=5', temp_date_day, temp_date_night)

    # 生駒山
    temp_date_day, temp_date_night = searchRegion('https://www.wbgt.env.go.jp/doc_trendcal.php?region=07&prefecture=62&point=62081&tab=5', temp_date_day, temp_date_night)

    # 堺
    temp_date_day, temp_date_night = searchRegion('https://www.wbgt.env.go.jp/doc_trendcal.php?region=07&prefecture=62&point=62091&tab=5', temp_date_day, temp_date_night)

    # 熊取
    temp_date_day, temp_date_night = searchRegion('https://www.wbgt.env.go.jp/doc_trendcal.php?region=07&prefecture=62&point=62131&tab=5', temp_date_day, temp_date_night)

    if not os.path.exists('./files'):
        os.makedirs('./files')
        
    plt.rcParams['font.family'] = 'IPAexGothic'
    temp_date_day.plot(figsize=(8,8))
    plt.savefig('./files/temp_date_osaka_day.jpg')

    plt.rcParams['font.family'] = 'IPAexGothic'
    temp_date_night.plot(figsize=(8,8))
    plt.savefig('./files/temp_date_osaka_night.jpg')

    with pd.ExcelWriter('./files/temp_date_osaka.xlsx') as writer:
        df = pd.DataFrame(temp_date_day)
        df.to_excel(writer, sheet_name='temp_day_2020', header=False, index=False)
        df = pd.DataFrame(temp_date_night)
        df.to_excel(writer, sheet_name='temp_night_2020', header=False, index=False)
  