import json
import requests


api_url = "https://reqres.in"
param = {"page": 2}
response = requests.get(api_url + "/api/users", params=param)

#Serializing json
json_obj = json.dumps(response.json(), indent=4)
#print(json_obj)

#Deserialize to python object
p = json.loads(json_obj)

#fetch data from
print(p["data"][1]["email"])


