def read_csv():
    with open("weather_data.csv") as file:
        lines = file.readlines()
        print(lines)

read_csv()