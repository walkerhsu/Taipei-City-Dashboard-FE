import csv 
import json 
import sys

encoding = 'Big5'

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = {"data":[]}
    jsonDict = {}
    fieldsname = ("name", "data")
    #read csv file
    with open(csvFilePath, encoding=encoding) as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 
        #convert each csv row into python dict
        i = 0
        for row in csvReader: 
            if(i == 0):
                for j in range(0, len(row)):
                    val = str(list(row)[j])
                    val = val.replace("遊客人次", '')
                    jsonDict.update({j:{val:[]}})
            else:
                for j in range(0, len(row)):
                    key = list(row)[j]
                    key = key.replace("遊客人次", '')
                    val = list(row.values())[j]
                    val = val.replace('�', '')
                    val = val.replace('~', '')
                    val = val.replace("-", "0")
                    jsonDict[j][str(key)].append((val))
            i += 1
        
        for key in jsonDict:
            for value in jsonDict[key]:
                jsonArray["data"].append({fieldsname[0]: value, fieldsname[1]: jsonDict[key][value]})
        print(jsonArray)
        
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4, ensure_ascii=False)
        jsonf.write(jsonString)
    
if __name__ == '__main__':
    csvFilePath = sys.argv[1]
    jsonFilePath = sys.argv[2]
    # csvFilePath = '../public/csvData/arg.csv'
    # jsonFilePath = '../public/chartData/3.json'
    csv_to_json(csvFilePath, jsonFilePath)