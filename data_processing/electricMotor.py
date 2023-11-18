import json
import requests
import geopandas as gpd
import geocoder
import pandas as pd
from shapely.geometry import LineString, Point, Polygon
import func
RID = "eff59f75-4a84-463d-adbe-59446dbf94c8"
raw_electricMoter = func.get_datataipei_api(RID)
electricMoter = raw_electricMoter.copy()  # avoid reloading raw data
electricMoter = electricMoter[['_id','單位', '行政區', '地址', '備註']]

# save it as json file:
electricMoter.to_json('electricMoter.json', orient='records', force_ascii=False)

