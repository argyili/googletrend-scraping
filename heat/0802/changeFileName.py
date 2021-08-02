import os
path= '/home/li-aiyi/Documents/program/web-scraping/heat/filesCSV/'      

#获取该目录下所有文件，存入列表中
fileList=os.listdir(path)

for i in range(0, len(fileList)):
    fileName = fileList[i]
    a = fileName.split('_', 1)
    if len(a) != 2:
        continue
    if a[1][4] == '0':
        b = a[1].replace(a[1][4], '')
        newFileName = a[0] + '_' + b
        print(newFileName)
        os.rename(os.path.join(path,fileName),os.path.join(path,newFileName))
        # break
