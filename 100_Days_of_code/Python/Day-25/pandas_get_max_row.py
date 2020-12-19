#get the row which has the maximun value in a serie
from pandas_max import max as maximun
from pandas_get_row import get_row


path = "weather_data.csv"
serie = "temp"
m = maximun(path, serie)
data = get_row(path,serie, m)
print(data)