import requests

base_url = "https://reqres.in"

#here 7 is the id to delete So its important to store response(id ) when we do POST
response = requests.delete(base_url+"/api/users/7")
print(response.status_code)