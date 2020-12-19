import pandas

def avg(path,serie_name):
    data = pandas.read_csv(path) 
    serie_list = data[serie_name].to_list() 
    return sum(serie_list) / len(serie_list)
    
    
average = avg("weather_data.csv","temp")    
print("temperature average " + str(average))