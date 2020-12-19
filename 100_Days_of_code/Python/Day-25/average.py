import pandas

def avg(path,serie_name):
    data = pandas.read_csv(path)
    return sum(data["temp"]) / len(data[serie_name])
    
    
average = avg("weather_data.csv","temp")    
print("temperature average " + str(average))