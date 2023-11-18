import json
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Step 1: Read the JSON file
with open('Taipei_Environment.json', 'r') as file:
    data = json.load(file)

# Convert the nested data structure to a flat DataFrame
flat_data = []
for i in range(len(data['data'][0]['data'])):
    flat_data.append({
        'station': data['data'][0]['data'][i],
        'address': data['data'][1]['data'][i],
        'longitude': float(data['data'][2]['data'][i]),
        'latitude': float(data['data'][3]['data'][i]),
        'date': data['data'][4]['data'][i],
        'aqi': data['data'][5]['data'][i],
        'air': data['data'][6]['data'][i],
        'o3': data['data'][7]['data'][i],
        'pm25_avg': data['data'][8]['data'][i],
        'pm10_avg': data['data'][9]['data'][i],
        'co_8hr': data['data'][10]['data'][i],
        'so2': data['data'][11]['data'][i],
        'no2': data['data'][12]['data'][i]
    })

# Step 2: Create a DataFrame
df = pd.DataFrame(flat_data)
# Step 3: Create a GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=[Point(xy) for xy in zip(df.longitude, df.latitude)])
# Set the coordinate reference system (CRS) to WGS84
gdf.set_crs(epsg=4326, inplace=True)
# Step 4: Save to a GeoJSON file
gdf.to_file("Taipei_Environment_output.geojson", driver="GeoJSON")
print("GeoJSON file created successfully.")
