import json
import ipdb
import requests
import jsonpath

api_url = "https://reqres.in"
param = {"page": 2}
response = requests.get(api_url + "/api/users", params=param)
#print(response.json())
#To get ouput in json format
print(json.dumps(response.json(),indent=4))

resp = response.json()
#for d in resp["data"]:
#    print(d["first_names"])
print([d["first_name"] for d in resp["data"]])
#use python debugger
#ipdb.set_trace()

