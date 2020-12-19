import pandas

def to_dict(path):
    data = pandas.read_csv(path)
    data_dict = data.to_dict()
    return data_dict


path = "weather_data.csv"
dict = to_dict(path)
print(dict)