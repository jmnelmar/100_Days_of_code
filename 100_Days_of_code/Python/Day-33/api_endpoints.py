import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

print(response.status_code)

if response.status_code == 404:
    raise Exception("That resource doesnt exist")
elif response.status_code == 401:
    raise Exception("You are not authorised to access this")