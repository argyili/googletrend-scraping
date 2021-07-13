from numpy.lib.function_base import append
from pandas.core.frame import DataFrame
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import datetime
import os
import json
import csv
import re

def txtToCsv():
    ls = open("./files/provinces.txt").readlines()
    newTxt = ""
    for line in ls:
        newTxt = newTxt + ",".join(line.split()) + "\n"
    # print(newTxt)

    fo = open("./files/provinces.csv", "x")
    fo.write(newTxt)
    fo.close()

def readCsv():
    csvFile = open("/home/li-aiyi/Documents/program/web-scraping/weatheralert/files/provinces.csv", 'r')
    # csvFile = open("./weatheralert/files/provinces.csv", 'r')
    reader = csv.reader(csvFile)
    ret = np.empty(shape=[0,2], dtype=str)
    # ret = []
    for item in reader:

        ret = np.append(ret, [[item[0], item[1]]], axis=0)
        # ret.append([item[0], item[1]])
        # result[item[0]] = {item[1]}

    csvFile.close()
    return ret
    # print(ret)

def getCities(address):
    page = requests.get(address)

    soup = BeautifulSoup(page.content, 'html.parser')
    cities = soup.find_all('ul',attrs={'class':'flat'})[3].find_all('a')
    ret = np.empty(shape=[0,2], dtype=str)
    for i in cities:
        # print(i.attrs['href'])
        index = str(i.attrs['href']).split('=')[1]
        # print(i.text)
        ret = np.append(ret, [[index, str(i.text)]], axis=0)
         
    # print(ret)
    # print(type(ret))
    return ret

def classify(cities, provinces, provList):
    templatePrefix = 'http://agora.ex.nii.ac.jp/cgi-bin/cps/warning_list.pl?acode='
    templateSuffix = '&page='
    for city in cities:
        address = templatePrefix + city[0] + templateSuffix
        # print(address)
        provIndex = recognizeIndex(city[0])
        # print(provIndex)
        print(provinces[provIndex-1])
        province = provinces[provIndex - 1]
        # Here date type maybe wrong 
        provList[provIndex - 1].append(collectData(city, province, address))
        # print(provList[provIndex - 1])
        print(type(provList[provIndex - 1]))
        print(provIndex - 1)
        return provList

    return provList

def recognizeIndex(index):
    # print(index[:2])
    return int(index[:2])

def collectData(city, province, address):
    index = 59
    columns = []
    cityData = pd.DataFrame()
    flag = True

    while flag:
        index = index + 1
        print(city[1] + ' page ' + str(index))
        newAddress = address + str(index)
        page = requests.get(newAddress)
        soup = BeautifulSoup(page.content, 'html.parser')
        # attrs = '/cgi-bin/cps/warning_list.pl?acode=0520100&amp;page=2'
        # pageNum = str(soup.find('a',attrs={attrs}))
        pageData = soup.find_all('tr',attrs={'id':re.compile('\d*-\d*-\d*')})
        if pageData == []:
            flag = False
            break

        for datas in pageData:
            item = datas.find_all('td')
            column =  ['']*7
            column[0] = city[1]
            column[1] = province[1]
            column[2] = city[0]
            column[3] = province[0]
            column[4] = item[2]
            column[5] = item[4]
            column[6] = item[5]
            columns.append(column)
        # print(columns)

    cityData = pd.concat([cityData, pd.DataFrame(columns)], axis=0)
    cityData.columns=['cityname', 'prefecture', 'prefid', 'cityid', 'type', 'start', 'end']
    print(cityData)

    return cityData

if __name__ == '__main__':
    provinces = readCsv()
    # txtToCsv()
    homePage = "http://agora.ex.nii.ac.jp/cps/weather/warning/area/"
    cities = getCities(homePage)
    provList = [[pd.DataFrame()]]*47
    print(type(provList))
    provList = classify(cities, provinces, provList)

    print('--')
    for i in range(47):
        # print(i)
        # if i < 10:
        #     index.insert(0, '0')
        # name = provinces.get(index)
        if provList[i] == None:
            # print('empty')
            continue
        print(i)
        print(provList[i])
        print('--')

        provIndex = str(i)
        with pd.ExcelWriter('./files/weathers_warnings_'+provIndex+'.xlsx') as writer:
            for j in range(len(provList[i])):
                if provList[i][j].empty:
                # print('empty')
                    break
                df = provList[i][j]
                print(df)
                cityName = df.iloc[2][1]
                df.to_excel(writer, sheet_name=cityName, index=False)

