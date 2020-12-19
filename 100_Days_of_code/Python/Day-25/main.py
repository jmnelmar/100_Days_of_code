

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])
data_dict = data.to_dict()
print(data_dict)
average = sum(data["temp"]) / len(data["temp"])
print("temperature average " + str(average))