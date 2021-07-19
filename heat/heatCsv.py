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
    loDegree = dfRegion.at[0, 'loDegree']
    loMinute = dfRegion.at[0, 'loMinute']
    lo = loDegree + loMinute / 60
    laDegree = dfRegion.at[0, 'laDegree']
    laMinute = dfRegion.at[0, 'laMinute']
    la = laDegree + laMinute / 60
    return lo, la

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

def pageRequests(address):
    cnt = 0
    page = requests.Response()
    while cnt < 10:
        try:
            page = requests.get(address, timeout=10)
        except requests.exceptions.RequestException or requests.exceptions.ConnectionError:
            cnt += 1
            print('cnt ' + str(cnt))
            continue
        return page

def downloadCSVFiles(address):
    page = pageRequests(address)

    soup = BeautifulSoup(page.content, 'html.parser')
    # Access from [3] to [4]
    cities = soup.find_all('p',attrs={'class':'recorddata'})[1].find_all('a')
    # print(cities)
    string = 'https://www.wbgt.env.go.jp/'
    for city in cities:
        fileAddress = string + city.attrs['href']
        fileName = city.attrs['href'].split('/')[-1].split('.')[0].split('_', 2)[-1]
        print(fileName)
        r = pageRequests(fileAddress)
        with open('./filesCSV/datas/' + fileName + '.csv', 'wb') as f:
            f.write(r.content)

def decorate(pdList, pointName):
    geoCodeLo, geoCodeLa = checkGeo(pointName)
    cityList = []
    for i in range(len(pdList)):
        cityList.append(pointName)    
    geoLoList = []
    for i in range(len(pdList)):
        geoLoList.append(geoCodeLo)
    geoLaList = []
    for i in range(len(pdList)):
        geoLaList.append(geoCodeLa)
    pdGeoList = pd.concat([pd.DataFrame(geoLaList), pd.DataFrame(geoLoList)], axis=1)

    pdCityList = pd.DataFrame(cityList)
    pdCityList.columns=['City']
    pdGeoList.columns=['Longtitude', 'Latitude']
    pdList = pd.concat([pdCityList, pdList, pdGeoList], axis=1)

    return pdList

def process():
    if not os.path.exists('./filesCSV'):
        os.makedirs('./filesCSV')    

    f = open('data.json')
    geoDict = json.load(f)

    regionDict = geoDict['region']
    prefectureDict = geoDict['prefecture']
    pointDict = geoDict['point']

    # for i in range(len(regionDict)):
    #     region = regionDict[i][0]
    #     if region != '07':
    #         continue
    #     prefectureList = prefectureDict.get(region)
    #     for j in range(len(prefectureList)):
    #         prefecture = prefectureList[j][0]
    #         if prefecture != '62':
    #             continue
    #         pointList = pointDict.get(prefecture)
    #         for k in range(len(pointList)):
    #             # if k > 1:
    #                 # break
    #             point = pointList[k][0]
    #             string = 'https://www.wbgt.env.go.jp/record_data.php?region=' + region + '&prefecture=' + prefecture + '&point=' + point
    #             print(string)
    #             downloadCSVFiles(string)    
                
    for i in range(len(regionDict)):
        region = regionDict[i][0]
        if region != '07':
            continue
        prefectureList = prefectureDict.get(region)
        for j in range(len(prefectureList)):
            prefecture = prefectureList[j][0]
            if prefecture != '62':
                continue
            pointList = pointDict.get(prefecture)
            
            dfList = []
            year = 2010
            for iy in range(11):
                iyStr = str(iy + year)
                month = 4
                for im in range(7):
                    im = im + month
                    imStr = str(im)
                    if im / 10 < 0:
                        imStr = '0'.join(str(im))
                    for k in range(len(pointList)):
                        # if k > 1:
                            # break
                        point = str(pointList[k][0])
                        pointName = pointList[k][1]
                        # string = 'https://www.wbgt.env.go.jp/record_data.php?region=' + region + '&prefecture=' + prefecture + '&point=' + point
                        # print(string)

                        fileName = './filesCSV/datas/' + point + '_' + iyStr + imStr + '.csv'
                        dfRead = pd.DataFrame()
                        try:
                            dfRead = pd.read_csv(fileName)
                        except Exception:
                            continue
                        
                        # print(dfRead)
                        dfList.append(decorate(dfRead, pointName))

                    # if not dfList[im].empty:
                    #     dfList[im].columns=['City', 'Date', 'Time', 'WBGT', 'Tg', 'Longitude', 'Latitude']
            
                with pd.ExcelWriter('./filesCSV/heatstroke'+iyStr+'_pref'+str(prefecture)+'.xlsx') as writer:
                    for index in range(len(dfList)):
                        indexM = index + month
                        if dfList[index].empty:
                            # print('empty')
                            continue
                        df = dfList[index]
                        df.to_excel(writer, sheet_name=iyStr+str(indexM)+'_pref'+str(prefecture), index=False)
                        



if __name__ == '__main__':
    process()