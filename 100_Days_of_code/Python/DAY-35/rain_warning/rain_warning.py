
import requests
# latlong.net -> check latitue and longitude
#https://home.openweathermap.org/myservices
# jmnel_mar 


api_key = "8682a293fbd0d9c0c576f644784d429a"
rain_codes = [
    200,
    201,
    202,
    210,
    211,
    212,
    221,
    230,
    231,
    232,
    500,
    501,
    502,
    503,
    504,
    511,
    520,
    521,
    522,
    531
]



members ={
    "lat":33.441792,
    "lon":-94.037689,
    "exclude":"current,minutely,daily,alerts",
    "appid":"8682a293fbd0d9c0c576f644784d429a"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall",members)
response.raise_for_status()
data = response.json()["hourly"]

for index in range(0,11):
    weather = data[index]["weather"]
    
    if weather[0]["id"] in rain_codes:
        print("carry in your umbrella it's going to rain today")
    else:
        print(weather[0]["description"])
        break
    #print(weather["id"])
#print(data)
