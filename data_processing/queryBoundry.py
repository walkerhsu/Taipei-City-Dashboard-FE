import os
import sys
import requests
import json
from dotenv import load_dotenv

def queryBoundaries(lng, lat):
    load_dotenv()
    ACCESS_TOKEN = os.getenv("VITE_MAPBOXTOKEN")
    MAPBOXTILE_DAAN = os.getenv("VITE_MAPBOXTILE_DAAN")
    MAPBOXTILE_ZHONGZHENG = os.getenv("VITE_MAPBOXTILE_ZHONGZHENG")
    MAPBOXTILE_XINYI = os.getenv("VITE_MAPBOXTILE_XINYI")
    MAPBOXTILE_SONGSHAN = os.getenv("VITE_MAPBOXTILE_SONGSHAN")
    MAPBOXTILE_NANGANG = os.getenv("VITE_MAPBOXTILE_NANGANG")
    MAPBOXTILE_SHILIN = os.getenv("VITE_MAPBOXTILE_SHILIN")
    MAPBOXTILE_BEITOU = os.getenv("VITE_MAPBOXTILE_BEITOU")
    MAPBOXTILE_NEIHU = os.getenv("VITE_MAPBOXTILE_NEIHU")
    MAPBOXTILE_WENSHAN = os.getenv("VITE_MAPBOXTILE_WENSHAN")
    MAPBOXTILE_ZHONGSHAN = os.getenv("VITE_MAPBOXTILE_ZHONGSHAN")
    MAPBOXTILE_ZHONGZHENG = os.getenv("VITE_MAPBOXTILE_ZHONGZHENG")
    MAPBOXTILE_WANHUA = os.getenv("VITE_MAPBOXTILE_WANHUA")
    
    all_districts = []
    all_districts.append({"DAAN": MAPBOXTILE_DAAN})
    all_districts.append({"ZHONGZHENG": MAPBOXTILE_ZHONGZHENG})
    all_districts.append({"XINYI": MAPBOXTILE_XINYI})
    all_districts.append({"SONGSHAN": MAPBOXTILE_SONGSHAN})
    all_districts.append({"NANGANG": MAPBOXTILE_NANGANG})
    all_districts.append({"SHILIN": MAPBOXTILE_SHILIN})
    all_districts.append({"BEITOU": MAPBOXTILE_BEITOU})
    all_districts.append({"NEIHU": MAPBOXTILE_NEIHU})
    all_districts.append({"WENSHAN": MAPBOXTILE_WENSHAN})
    all_districts.append({"ZHONGSHAN": MAPBOXTILE_ZHONGSHAN})
    all_districts.append({"ZHONGZHENG": MAPBOXTILE_ZHONGZHENG})
    all_districts.append({"WANHUA": MAPBOXTILE_WANHUA})
    
    # print(all_districts)
    
    in_district = ""
    
    parameters = {
        "access_token": ACCESS_TOKEN,
    }
    
    for i in range(0, len(all_districts)):
        for key, value in all_districts[i].items():
            # print(key, value)
            res = requests.get(f'https://api.mapbox.com/v4/{value}/tilequery/{lng},{lat}.json', params=parameters)
            # print(res.json()['features'])
            if(res.json()['features'] != []):
                in_district = key
            
    print(in_district)
        
if __name__ == "__main__":
    # lng = sys.argv[1]
    # lat = sys.argv[2]
    lng = 121.54399
    lat = 25.024624
    queryBoundaries(lng, lat)
