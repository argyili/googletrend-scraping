import os
import pandas as pd
path= '/home/li-aiyi/Documents/program/web-scraping/heat/filesCSV/'      

#获取该目录下所有文件，存入列表中
fileList=os.listdir(path)

for i in range(0, len(fileList)):
    fileName = fileList[i]
    filePath = os.path.join(path,fileName)
    sheet = pd.read_excel(filePath, sheet_name=None)
    print(fileName)
    # for v in sheet.values():
    #     v.columns=['City', 'Date', 'Time', 'WBGT', 'Tg', 'Latitude', 'Longitude']

    with pd.ExcelWriter(filePath) as writer:
        for k, v in sheet.items():
            v.columns=['City', 'Date', 'Time', 'WBGT', 'Tg', 'Latitude', 'Longitude']
            v.to_excel(writer, sheet_name=k, index=False)
    