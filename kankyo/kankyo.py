from pandas.core.frame import DataFrame
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import datetime
import os
import json

def searchDate(address):
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
    date_day = pd.DataFrame(date[:midLen])
    date_day.columns=['']
    date_night = pd.DataFrame(date[midLen:])
    date_night.columns=['']
    date = date_day
    
    return date

def searchRegion(address, date, temp_date_day, temp_date_night, temp_date):
    page = requests.get(address)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    region = soup.find(class_="data selected").text
    if region == '':
        return temp_date_day, temp_date_night, temp_date

    temp = []
    for el in soup.find_all(class_= re.compile("data map_ct_lv" + "."  + " selected")):
        temp.append(float(el.text))
    
    midLen = len(temp) // 2
    temp_day = pd.DataFrame(temp[:midLen])
    temp_night = pd.DataFrame(temp[midLen:])
    temp_day.columns=[region + ' Day']
    temp_night.columns=[region + ' Night']

    temp_date_day = pd.concat([temp_date_day, temp_day], axis=1)
    temp_date_night = pd.concat([temp_date_night, temp_night], axis=1)
    temp_date = pd.concat([temp_date, temp_day, temp_night], axis=1)

    return temp_date_day, temp_date_night, temp_date

def searchRegion2nd(address, date, temp_date_day, temp_date_night, temp_date):
    page = requests.get(address)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    region = soup.find(class_="data selected").text
    if region == '':
        return temp_date_day, temp_date_night, temp_date

    regionList = []
    for i in range(len(date)):
        regionList.append(region)

    temp = []
    for el in soup.find_all(class_= re.compile("data map_ct_lv" + "."  + " selected")):
        temp.append(float(el.text))
    

    midLen = len(temp) // 2
    temp_day = pd.DataFrame(temp[:midLen])
    temp_night = pd.DataFrame(temp[midLen:])
    temp_day.columns=['WBGT_Day']
    temp_night.columns=['WBGT_Night']

    temp_date_day = pd.concat([temp_date_day, temp_day], axis=1)
    temp_date_night = pd.concat([temp_date_night, temp_night], axis=1)
    temp_temp = pd.concat([pd.DataFrame(regionList), date, temp_day, temp_night], axis=1)
    temp_date = pd.concat([temp_date, temp_temp], axis=0)

    return temp_date_day, temp_date_night, temp_date

if __name__ == '__main__':

    tempDateList = []

    f = open('data.json')
    geoDict = json.load(f)

    regionDict = geoDict['region']
    prefectureDict = geoDict['prefecture']
    pointDict = geoDict['point']

    for i in range(len(regionDict)):
        # if i > 0:
        #     break
        temp_date_day = pd.DataFrame()
        temp_date_night = pd.DataFrame()
        temp_date = pd.DataFrame()
        # 天気 Casual website to access the date information
        date = searchDate('https://www.wbgt.env.go.jp/doc_trendcal.php?region=07&prefecture=62&point=62016&tab=5')
        
        # Use with 1st format
        # temp_date = date;
    
        region = regionDict[i][0]
        prefectureList = prefectureDict.get(region)
        for j in range(len(prefectureList)):
            # if j > 1:
            #     break
            prefecture = prefectureList[j][0]
            pointList = pointDict.get(prefecture)
            for k in range(len(pointList)):
                # if k > 1:
                #     break
                point = pointList[k][0]
                string = 'https://www.wbgt.env.go.jp/doc_trendcal.php?region=' + region + '&prefecture=' + prefecture + '&point=' + point + '&tab=5'
                # string = 'https://www.wbgt.env.go.jp/doc_trendcal.php?region=' + '02' + '&prefecture=' + '34' + '&point=' + '34296' + '&tab=5'
                print(string)

                # temp_date_day, temp_date_night, temp_date = searchRegion(string, date, temp_date_day, temp_date_night, temp_date)
                temp_date_day, temp_date_night, temp_date = searchRegion2nd(string, date, temp_date_day, temp_date_night, temp_date)
        print(temp_date)
        tempDateList.append(temp_date)

    if not os.path.exists('./files'):
        os.makedirs('./files')
        


    with pd.ExcelWriter('./files/temp_date_2020.xlsx') as writer:
        for i in range(len(tempDateList)):
            df = pd.DataFrame(tempDateList[i])
            df.to_excel(writer, sheet_name=regionDict[i][1], index=False)

            plt.rcParams['font.family'] = 'IPAexGothic'
            tempDateList[i].set_index('').plot(figsize=(8,8))
            plt.savefig('./files/temp_date_japan_' + regionDict[i][1] + '.jpg')
