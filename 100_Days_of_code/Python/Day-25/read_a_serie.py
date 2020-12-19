import pandas

def get_serie(path, serie_name):
    data = pandas.read_csv(path)
    return data[serie_name]


path = "weather_data.csv"
serie_name = "temp"

serie = get_serie(path, serie_name)
print(serie)