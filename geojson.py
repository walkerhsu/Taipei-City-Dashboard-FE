# -*- coding: utf-8 -*-
"""GeoJson.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hGTMN7vk3URohIY7txxyJSgr-XisqNhL
"""

# Commented out IPython magic to ensure Python compatibility.
import json
import requests
import geopandas as gpd
import geocoder
import pandas as pd
from shapely.geometry import LineString, Point, Polygon

import json

with open("electricMoterLngLat.json", "r",encoding="utf-8") as coorFile:
    coorData = json.load(coorFile)
with open("electricMoter.json", "r",encoding="utf-8") as welfareFile:
    welfareData = json.load(welfareFile)
features = []
for coor, welfare in zip(coorData, welfareData):
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [coor["lat"], coor["lng"]],
        },
        "properties": {
            # "name": welfare.get("機構名稱"),  # Using get to handle missing keys
            # "長照床位數量": welfare.get("長照床位數量", ""),

            "單位": welfare.get("單位", ""),
            "行政區": welfare.get("行政區", ""),
            "地址": welfare.get("地址", ""),
            "備註": welfare.get("備註", ""),
        },
    }
    features.append(feature)

geojson = {
    "type": "FeatureCollection",
    "features": features,
}

# Now 'geojson' contains the desired structure
with open("elecMotor.geojson", "w", encoding="utf-8") as output_file:
    json.dump(geojson, output_file, ensure_ascii=False)

print("GeoJSON file has been created and saved.")