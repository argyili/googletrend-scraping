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
import numpy as np

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
    if len(soup.find_all('p',attrs={'class':'recorddata'})) < 2:
        with open('./files/filesCSV/lostDataCities.txt', 'a+') as f:
            f.write(address + ' ')
        return
    cities = soup.find_all('p',attrs={'class':'recorddata'})[1].find_all('a')
    # print(cities)
    string = 'https://www.wbgt.env.go.jp/'
    for city in cities:
        fileAddress = string + city.attrs['href']
        fileName = city.attrs['href'].split('/')[-1].split('.')[0].split('_', 2)[-1]
        print(fileName)
        r = pageRequests(fileAddress)
        with open('./files/filesCSV/datas/' + fileName + '.csv', 'wb') as f:
            f.write(r.content)

def downloadCSVFilesZero(address):
    page = pageRequests(address)

    soup = BeautifulSoup(page.content, 'html.parser')
    # if len(soup.find_all('p',attrs={'class':'recorddata'})) < 2:
    #     with open('./filesCSV/lostDataCities.txt', 'a+') as f:
    #         f.write(address + ' ')
    #     return
    cities = soup.find_all('p',attrs={'class':'recorddata'})[0].find_all('a')
    # print(cities)
    string = 'https://www.wbgt.env.go.jp/'
    for city in cities:
        fileAddress = string + city.attrs['href']
        fileName = city.attrs['href'].split('/')[-1].split('.')[0].split('_', 2)[-1]
        print(fileName)
        r = pageRequests(fileAddress)
        with open('./files/filesCSV/datas/' + fileName + '.csv', 'wb') as f:
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

def checkRealPrefecturePageStr(prefectureName):
    df = pd.read_csv('./files/provinces.csv', header=None)
    dfSingle = df[df[1].str.startswith(prefectureName)]
    # print(dfSingle)
    list = dfSingle[[0]].values
    id = int(list[0][0])
    idStr = str(id)
    if id < 10:
        idStr = '0' + idStr
    return idStr

def process():
    if not os.path.exists('./files/filesCSV'):
        os.makedirs('./files/filesCSV')    

    f = open('data.json')
    geoDict = json.load(f)

    regionDict = geoDict['region']
    prefectureDict = geoDict['prefecture']
    pointDict = geoDict['point']

    # for i in range(len(regionDict)):
    #     region = regionDict[i][0]
    #     if region == '01':
    #         continue
    #     prefectureList = prefectureDict.get(region)
    #     for j in range(len(prefectureList)):
    #         prefecture = prefectureList[j][0]
    #         # if prefecture != '34':
    #         #     continue
    #         pointList = pointDict.get(prefecture)
    #         for k in range(len(pointList)):
    #             point = pointList[k][0]
    #             # if point != '34296':
    #             #     continue
    #             string = 'https://www.wbgt.env.go.jp/record_data.php?region=' + region + '&prefecture=' + prefecture + '&point=' + point
    #             print(string)
    #             downloadCSVFiles(string)  

    # string = 'https://www.wbgt.env.go.jp/record_data.php?region=03&prefecture=44&point=44356'
    # print(string)
    # downloadCSVFilesZero(string)    
    # string = 'https://www.wbgt.env.go.jp/record_data.php?region=10&prefecture=86&point=86156'
    # print(string)
    # downloadCSVFilesZero(string)    


    # Hokkaido only
    # for i in range(len(regionDict)):
    #     region = regionDict[i][0]
    #     if region != '01':
    #         continue
    #     prefectureList = prefectureDict.get(region)

    #     year = 2010
    #     for iy in range(11):
    #         iyStr = str(iy + year)
    #         dfList = []
    #         for j in range(len(prefectureList)):
    #             prefecture = prefectureList[j][0]
    #             # if prefecture != '11':
    #             #     continue
    #             pointList = pointDict.get(prefecture)
    #             month = 4    
    #             for im in range(7):
    #                 im = im + month
    #                 imStr = str(im)
    #                 if im < 10:
    #                     imStr = '0' + (str(im))
                    
    #                 dfData = pd.DataFrame()
    #                 for k in range(len(pointList)):
    #                     # if k > 1:
    #                         # break
    #                     point = str(pointList[k][0])
    #                     pointName = pointList[k][1]
    #                     # fileName = 'https://www.wbgt.env.go.jp/record_data.php?region=' + region + '&prefecture=' + prefecture + '&point=' + point
    #                     fileName = './filesCSV/datas/' + point + '_' + iyStr + imStr + '.csv'
    #                     dfRead = pd.DataFrame()
    #                     try:
    #                         dfRead = pd.read_csv(fileName)
    #                     except Exception:
    #                         continue

    #                     # print(dfRead)
    #                     dfData = pd.concat([dfData, decorate(dfRead, pointName)], axis=0)
    #                 if len(dfList) < im-month+1:
    #                     dfList.append(dfData)
    #                 else:
    #                     dfList[im-month] = pd.concat([pd.DataFrame(dfList[im-month]), dfData], axis=0)
                
    #         with pd.ExcelWriter('./filesCSV/heatstroke'+iyStr+'_pref'+'01'+'.xlsx') as writer:
    #             for index in range(7):
    #                 if dfList[index].empty:
    #                     continue
    #                 df = dfList[index]
    #                 indexStr =str(index+month)
    #                 if index+month < 10:
    #                     indexStr = '0' + indexStr
    #                 df.to_excel(writer, sheet_name=iyStr+str(indexStr)+'_pref'+'01', index=False)

    # Except for Hokkaido
    for i in range(len(regionDict)):
        region = regionDict[i][0]
        if region == '01':
            continue
        prefectureList = prefectureDict.get(region)
        for j in range(len(prefectureList)):
            prefecture = prefectureList[j][0]
            prefectureName = prefectureList[j][1]
            # if prefecture != '11':
            #     continue
            pointList = pointDict.get(prefecture)
            dfList = []
            year = 2010
            prefecturePageStr = checkRealPrefecturePageStr(prefectureName)
            for iy in range(11):
                iyStr = str(iy + year)
                month = 4
                for im in range(7):
                    im = im + month
                    imStr = str(im)
                    if im < 10:
                        imStr = '0' + (str(im))
                    
                    dfData = pd.DataFrame()
                    for k in range(len(pointList)):
                        # if k > 1:
                            # break
                        point = str(pointList[k][0])
                        pointName = pointList[k][1]
                        # fileName = 'https://www.wbgt.env.go.jp/record_data.php?region=' + region + '&prefecture=' + prefecture + '&point=' + point
                        fileName = './files/filesCSV/datas/' + point + '_' + iyStr + imStr + '.csv'
                        dfRead = pd.DataFrame()
                        try:
                            dfRead = pd.read_csv(fileName)
                        except Exception:
                            continue

                        # print(dfRead)
                        dfData = pd.concat([dfData, decorate(dfRead, pointName)], axis=0)
                    dfList.append(dfData)
                # print(dfList)

                with pd.ExcelWriter('./files/filesCSV/heatstroke'+iyStr+'_pref'+prefecturePageStr+'.xlsx') as writer:
                    for index in range(7):
                        if dfList[index].empty:
                            # print('empty')
                            continue
                        df = dfList[index]
                        indexStr =str(index+month)
                        # if index+month < 10:
                        #     indexStr = '0' + indexStr
                        df.to_excel(writer, sheet_name=iyStr+str(indexStr)+'_pref'+prefecturePageStr, index=False)



if __name__ == '__main__':
    process()