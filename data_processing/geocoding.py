import os
import sys
import requests
import json
from dotenv import load_dotenv

encoding = "utf-8"

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


if __name__ == "__main__":
    inputPath = sys.argv[1]
    outputPath = sys.argv[2]
    
    load_dotenv()
    geocoding_key = os.getenv("GEOCODING_KEY")
    result = []

    with open(inputPath) as file:
        data = json.load(file)
        
	#  modify the position of "location" in data, in this case it's at data["data"][i]["name"]
    for i in range(len(data["data"][0]["data"])):
        location = data["data"][i]["name"]
        parameters = {
            "address": location,
            "key": geocoding_key,
        }
        response = requests.get(
            "https://maps.googleapis.com/maps/api/geocode/json", params=parameters
        )
        if (
            response.json()["results"] == []
            and response.json()["status"] == "ZERO_RESULTS"
        ):
            print(location)
            continue
        result.append(response.json()["results"][0]["geometry"]["location"])
    
    # print(result)
        
    with open(outputPath, 'w', encoding=encoding) as jsonf: 
        jsonString = json.dumps(result, indent=4, ensure_ascii=False)
        jsonf.write(jsonString)
