

import pandas
def max(path,serie_name):
    data = pandas.read_csv(path)
    return data[serie_name].max()

#print("Temperature max is "+str(mean("weather_data.csv","temp")))