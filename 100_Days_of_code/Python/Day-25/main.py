
#with open("weather_data.csv") as file:
#    lines = file.readlines()
#    print(lines)
    
#import csv

#with open("weather_data.csv") as file:
#    data = csv.reader(file)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#    print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])
data_dict = data.to_dict()
print(data_dict)
average = sum(data["temp"]) / len(data["temp"])
print("temperature average " + str(average))