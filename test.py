import requests
import json

BASE = "http://127.0.0.1:5000/"

patch_data = {'iso_code':'HSY',
                'continent': 'OOKK',
                'location': 'KSA',
                }

# patch operation
response = requests.patch(BASE + "covid_data/" + "9009", json=patch_data)

# put operation
data = ['TESTASIA', 'TESTAFRICA', 8267372]
jsonstr = json.dumps(data)
response = requests.put(BASE + "covid_data_update", json=jsonstr)

# get operation
response = requests.get(BASE + "covid_data/" + "5")
# print(response.json())

# delete operation
response = requests.delete(BASE + "covid_data/" + "8008")


authorize = {
    "username":"user1",
    "password":"leef2"
}

# authorization
response = requests.post(BASE + "/auth", json=authorize)
print(response.json())