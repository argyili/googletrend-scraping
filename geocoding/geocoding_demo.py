import time
import geocoder
import pandas as pd

if __name__ == '__main__':
    g = geocoder.arcgis('')
    print(g.osm)
    