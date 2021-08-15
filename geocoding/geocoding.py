import time
import geocoder
import pandas as pd

if __name__ == '__main__':
    fileName = './files/list_school.xlsx'
    sheets = pd.read_excel(fileName, sheet_name=None)
    
    for k, v in sheets.items():
        for index, items in v.iterrows():
            # print(items['学校所在地'])
            g = geocoder.arcgis(items['学校所在地'])
            print(g.osm)
            sheets[k].at[index, 'latitude'] = g.osm['y']
            sheets[k].at[index, 'longitude'] = g.osm['x']
            # time.sleep(0.1)
            # break

    newFileName = './files/list_school_geo.xlsx'
    with pd.ExcelWriter(newFileName) as writer:
        for k, v in sheets.items():
            v.to_excel(writer, sheet_name=k, index=False)
    