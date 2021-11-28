import json
json_file = open("ETL_load4.json", "r", encoding="utf-8")
json_data = json.load(json_file)
json_file.close()
