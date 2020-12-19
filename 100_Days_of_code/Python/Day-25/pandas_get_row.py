import pandas

def get_row(path, serie_name, condition):
    data = pandas.read_csv(path)
    return data[data[serie_name] == condition]
    
#path = "weather_data.csv"
#serie_name = "day"
#condition = "Monday"
#serie = get_row(path, serie_name,condition)
#print(serie)