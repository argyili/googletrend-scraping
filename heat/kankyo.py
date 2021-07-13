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
import csv

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

def checkGeo(region):
    df = pd.read_csv('geoData.csv')
    querySentence= 'name=="'+ str(region) + '"'
    dfRegion = df.query(querySentence)

    if dfRegion.empty:
        with open('lostCity.txt', 'a+') as f:
            f.write(region + ' ')
        return 0, 0
    dfRegion = dfRegion.reset_index(drop=True)
    laDegree = dfRegion.at[0, 'laDegree']
    laMinute = dfRegion.at[0, 'laMinute']
    la = laDegree + laMinute / 60
    loDegree = dfRegion.at[0, 'loDegree']
    loMinute = dfRegion.at[0, 'loMinute']
    lo = loDegree + loMinute / 60

    
    return la, lo

def searchRegion2nd(address, date, temp_date_day, temp_date_night, temp_date):
    page = requests.get(address)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    region = soup.find(class_="data selected").text
    if region == '':
        return temp_date_day, temp_date_night, temp_date

    # print(region)
    geoCodeLa, geoCodeLo = checkGeo(region)

    regionList = []
    for i in range(len(date)):
        regionList.append(region)
    geoLaList = []
    for i in range(len(date)):
        geoLaList.append(geoCodeLa)
    geoLoList = []
    for i in range(len(date)):
        geoLoList.append(geoCodeLo)
    pdRegionList = pd.DataFrame(regionList)
    pdRegionList.columns=['City']
    pdGeoList = pd.concat([pd.DataFrame(geoLaList), pd.DataFrame(geoLoList)], axis=1)
    pdGeoList.columns=['Latitude', 'Longtitude']
    temp = []
    for el in soup.find_all(class_= re.compile("data map_ct_lv" + "."  + " selected")):
        temp.append(float(el.text))
    if temp == []:
        return temp_date_day, temp_date_night, temp_date
    midLen = len(temp) // 2
    temp_day = pd.DataFrame(temp[:midLen])
    temp_night = pd.DataFrame(temp[midLen:])
    temp_day.columns=['WBGT_Day']
    temp_night.columns=['WBGT_Night']

    temp_date_day = pd.concat([temp_date_day, temp_day], axis=1)
    temp_date_night = pd.concat([temp_date_night, temp_night], axis=1)
    temp_temp = pd.concat([pdRegionList, date, temp_day, temp_night, pdGeoList], axis=1)
    temp_date = pd.concat([temp_date, temp_temp], axis=0)

    return temp_date_day, temp_date_night, temp_date

def process(tab):
    
    tempDateList = []

    f = open('data.json')
    geoDict = json.load(f)

    regionDict = geoDict['region']
    prefectureDict = geoDict['prefecture']
    pointDict = geoDict['point']

    for i in range(len(regionDict)):
    # for i in range(1):
        # if i != 2:
        #     continue
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
                # break
            prefecture = prefectureList[j][0]
            pointList = pointDict.get(prefecture)
            for k in range(len(pointList)):
                # if k > 1:
                    # break
                point = pointList[k][0]
                string = 'https://www.wbgt.env.go.jp/doc_trendcal.php?region=' + region + '&prefecture=' + prefecture + '&point=' + point + '&tab='+tab
                # string = 'https://www.wbgt.env.go.jp/doc_trendcal.php?region=' + '10' + '&prefecture=' + '86' + '&point=' + '86156' + '&tab=1'
                print(string)

                # temp_date_day, temp_date_night, temp_date = searchRegion(string, date, temp_date_day, temp_date_night, temp_date)
                temp_date_day, temp_date_night, temp_date = searchRegion2nd(string, date, temp_date_day, temp_date_night, temp_date)
                

        print(temp_date)
        tempDateList.append(temp_date)

    if not os.path.exists('./files'):
        os.makedirs('./files')
        

    year = str(int(tab) + 2015)
    with pd.ExcelWriter('./files/heatStroke'+year+'.xlsx') as writer:
        for i in range(len(tempDateList)):
            df = pd.DataFrame(tempDateList[i])
            df.to_excel(writer, sheet_name=regionDict[i][1], index=False)

            # plt.rcParams['font.family'] = 'IPAexGothic'
            # tempDateList[i].set_index('').plot(figsize=(8,8))
            # plt.savefig('./files/temp_date_japan_' + regionDict[i][1] + '.jpg')

if __name__ == '__main__':
    for index in range(0, 5):
        print(index)
        process(str(index+1))