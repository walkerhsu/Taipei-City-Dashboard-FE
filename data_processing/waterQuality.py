import requests
import xml.etree.ElementTree as ET
from datetime import datetime
import pandas as pd
import json
import requests
import geopandas as gpd
import geocoder
import pandas as pd
from shapely.geometry import LineString, Point, Polygon
def fetch_and_save_data(url):
    # Send HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the XML from the response
        root = ET.fromstring(response.content)

        # Initialize a list to store the data
        data = []

        # Loop through each 'qua_data' element in the XML
        for qua_data in root.findall('.//qua_data'):
            record = {
                'update_date': qua_data.find('update_date').text,
                'update_time': qua_data.find('update_time').text,
                'qua_id': qua_data.find('qua_id').text,
                'code_name': qua_data.find('code_name').text,
                'lng': qua_data.find('longitude').text,
                'lat': qua_data.find('latitude').text,
                '濁度(NTU)': qua_data.find('qua_cntu').text,
                '餘氯(mg/L)': qua_data.find('qua_cl').text,
                '酸鹼度(PH)': qua_data.find('qua_ph').text
            }
            data.append(record)

        # Convert the list of dictionaries to a pandas DataFrame
        df = pd.DataFrame(data)
        gdf = gpd.GeoDataFrame(df, geometry=[Point(xy) for xy in zip(df.lng, df.lat)])
        gdf.set_crs(epsg=4326, inplace=True)
        filename = f"data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.geojson"
        gdf.to_file(filename, driver="GeoJSON")
        return f"Data successfully fetched and saved as {filename}"
    else:
        return "Failed to fetch data from the URL"

# URL of the dataset
url = "https://twd.water.gov.taipei/opendata/wqb/wqb.asmx/GetQualityData"

# Fetch and save the data
result = fetch_and_save_data(url)
result

