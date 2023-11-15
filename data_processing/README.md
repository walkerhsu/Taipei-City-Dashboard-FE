# Usage of geocoding.py 

### Convert a location (Chinese or US English) to global coordinates

Inputs: input and output file path </br>
Outputs: global coordinates of a json file </br>

```shell
	python geocoding.py <input_file_path> <output_file_path>
```
### Suggestions: output file path should be a json file

Example:
```shell
 	python geocoding.py ../public/chartData/2.json ./test.json
```

# Usage of csvToJson_3d.py

### Convert a csv file to a json file with specific data format

Inputs: input and output file path </br>
Outputs: chart data of a json file </br>

```shell
 	python csvToJson_3d.py <input_file_path> <output_file_path>
```
Example:

```shell
	python csvToJson_3d.py ../public/csvData/arg.csv ../public/chartData/3.json
```

