import requests
# latlong.net -> check latitue and longitude
#https://home.openweathermap.org/myservices
# jmnel_mar 


api_key = "8682a293fbd0d9c0c576f644784d429a"


members ={
    "lat":33.441792,
    "lon":-94.037689,
    "exclude":"current,minutely,daily,alerts",
    "appid":"8682a293fbd0d9c0c576f644784d429a"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall",members)
response.raise_for_status()
data = response.json()["hourly"]
print(data)
