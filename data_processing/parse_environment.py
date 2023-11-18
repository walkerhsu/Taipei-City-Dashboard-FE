import os
import sys
import json

if __name__ == "__main__":
    jsonFilePath = sys.argv[1]
    chartjsonFilePath = sys.argv[2]
    # read json file
    allData = {}
    days = 7
    with open(jsonFilePath, 'r', encoding="utf-8") as jsonf:
        # load json file data using json library
        data = json.load(jsonf)

        for i in range(len(data["data"])):
            if(data["data"][i]["name"] != '空氣品質指標'):
                allData[data["data"][i]["name"]] = data["data"][i]["data"]
    print(allData)
    print(allData["測站"])
    geojsonDict = {
        "type": "FeatureCollection",
        "features": []
    }
    features = []
    for i in range(0, 84, days):
        # i from 0 to 83
        features.append({
            "type": "Feature",
            "properties": {
                "測站": allData["測站"][i],
                "地址": allData["地址"][i],
                "AQI": allData["AQI"][i],
                "日期": allData["日期"][i+6],
            },
            "geometry": {
                "type": "Point",
                "coordinates": [float(allData["經度"][i]), float(allData["緯度"][i])]
            }
        })
    # geojsonDict["features"] = features
    # jsonString = json.dumps(geojsonDict, indent=4, ensure_ascii=False)
    # # without history data
    # with open(geojsonFilePath, 'w') as geojsonf:
    #     geojsonf.write(jsonString)

    jsonDict = {
        "data": []
    }
    for day in range(days):
        # i from 0 to 83
        date_data = []
        for j in range(12):
            date_data.append({
                "x": allData["測站"][day + j * days],
                "y": allData["AQI"][day + j * days]
            })
        date_data = sorted(date_data, key=lambda k: -1 * int(k['y']))
        jsonDict["data"].append({
            "name": allData["日期"][day],
            "data": date_data
        })
    # with history data
    with open(jsonDataPath, 'w') as jsonf:
        jsonf.write(json.dumps(jsonDict, indent=4, ensure_ascii=False))

    # only last day data
    # jsonDict = {
    #     "data" : []
    # }
    # today_data = []
    # for j in range(12):
    #     today_data.append({
    #         "x": allData["測站"][j * days + days - 1],
    #         "y": allData["AQI"][j * days + days - 1]
    #     })
    # jsonDict["data"].append({
    #     "name": "",
    #     "data": today_data
    # })
    
    # with open(chartDataPath, 'w') as jsonf:
    #     jsonf.write(json.dumps(jsonDict, indent=4, ensure_ascii=False))