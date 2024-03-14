import requests


base_url = "https://reqres.in/api/users/"

payload = {
    "name": "Sarvada",
    "job": "leader"
}

response = requests.post(base_url , json=payload)
print(response.json())
print(response.status_code)

#UPDATE
payload1 = {
    "name": "Sarvada",
    "job": "SSE"
}
response =  requests.put(base_url + "2", data=payload1)
print(response.status_code)
print(response.json())
