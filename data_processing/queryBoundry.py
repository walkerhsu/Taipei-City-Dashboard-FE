import os
import sys
import requests
import json
from dotenv import load_dotenv
       
def addBoundaryProperty(inputfile, outputfile):
    load_dotenv()
    ACCESS_TOKEN = os.getenv("VITE_MAPBOXTOKEN")
    
    all_districts = {
        "DAAN": os.getenv("VITE_MAPBOXTILE_DAAN"),
        "ZHONGZHENG": os.getenv("VITE_MAPBOXTILE_ZHONGZHENG"),
        "XINYI": os.getenv("VITE_MAPBOXTILE_XINYI"),
        "SONGSHAN": os.getenv("VITE_MAPBOXTILE_SONGSHAN"),
        "NANGANG": os.getenv("VITE_MAPBOXTILE_NANGANG"),
        "SHILIN": os.getenv("VITE_MAPBOXTILE_SHILIN"),
        "BEITOU": os.getenv("VITE_MAPBOXTILE_BEITOU"),
        "NEIHU": os.getenv("VITE_MAPBOXTILE_NEIHU"),
        "WENSHAN": os.getenv("VITE_MAPBOXTILE_WENSHAN"),
        "ZHONGSHAN": os.getenv("VITE_MAPBOXTILE_ZHONGSHAN"),
        "WANHUA": os.getenv("VITE_MAPBOXTILE_WANHUA")
    }
    
    parameters = {
        "access_token": ACCESS_TOKEN,
    }
    
    with open(inputfile, 'r') as file:
        data = json.load(file)
        
    for feature in data['features']:
        lng, lat = feature['geometry']['coordinates']
        in_district = ""
        # Check which district the point belongs to
        for district, tile in all_districts.items():
            res = requests.get(f'https://api.mapbox.com/v4/{tile}/tilequery/{lng},{lat}.json', params=parameters)
            if res.json()['features']:
                in_district = district
                break

        # Add district name to properties
        feature['properties']['district'] = in_district

    # Write output file
    with open(outputfile, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        
if __name__ == "__main__":
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    addBoundaryProperty(inputfile, outputfile)