from numpy.lib.function_base import append
from pandas.core.frame import DataFrame
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
import csv
import re

def txtToCsv():
    ls = open("./files/provinces.txt").readlines()
    newTxt = ""
    for line in ls:
        newTxt = newTxt + ",".join(line.split()) + "\n"

    fo = open("./files/provinces.csv", "x")
    fo.write(newTxt)
    fo.close()

def readCsv():
    csvFile = open("./files/provinces.csv", 'r')
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
        index = str(i.attrs['href']).split('=')[1]
        ret = np.append(ret, [[index, str(i.text)]], axis=0)
         
    return ret

def classify(cities, provinces, provList):
    templatePrefix = 'http://agora.ex.nii.ac.jp/cgi-bin/cps/warning_list.pl?acode='
    templateSuffix = '&page='
    # i = 0
    for city in cities:
        # i = i+1
        # if i > 1:
            # return provList
        address = templatePrefix + city[0] + templateSuffix
        provIndex = recognizeIndex(city[0])
        print(provinces[provIndex-1])
        province = provinces[provIndex - 1]
        provList[provIndex - 1].append(collectData(city, province, address))

    return provList

def recognizeIndex(index):
    return int(index[:2])

def collectData(city, province, address):
    index = 0
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
            if item == None or item == []:
                continue
            column =  ['']*7
            column[0] = city[1]
            column[1] = province[1]
            column[2] = city[0]
            column[3] = province[0]
            column[4] = item[2].text
            column[5] = item[4].text
            column[6] = item[5].text
            columns.append(column)

    cityData = pd.concat([cityData, pd.DataFrame(columns)], axis=0)
    if not cityData.empty:
        cityData.columns=['cityname', 'prefecture', 'cityid', 'prefid', 'type', 'start', 'end']
    print(cityData)

    return cityData

if __name__ == '__main__':
    provinces = readCsv()
    # txtToCsv()
    homePage = "http://agora.ex.nii.ac.jp/cps/weather/warning/area/"
    cities = getCities(homePage)
    # provList = [[pd.DataFrame()]]*47
    provList = [[] for i in range(47)]
    print(type(provList))
    provList = classify(cities, provinces, provList)

    for i in range(47):
        if provList[i] == []:
            # print('empty')
            continue

        # print(i)
        provIndex = str(i + 1)
        with pd.ExcelWriter('./files/weathers_warnings_'+provIndex+'.xlsx') as writer:
            for j in range(len(provList[i])):
                if provList[i][j].empty:
                # print('empty')
                    break
                df = provList[i][j]
                cityName = df.iloc[2][0] + ' ' +df.iloc[2][2]
                df.to_excel(writer, sheet_name=cityName, index=False)

