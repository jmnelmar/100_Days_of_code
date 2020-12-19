

import pandas
def mean(path,serie_name):
    data = pandas.read_csv(path)
    return data[serie_name].mean()

print("Temperature average is "+str(mean("weather_data.csv","temp")))