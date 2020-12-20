import pandas

def pivot(file_path, out_file, serie, col_names):
    data = pandas.read_csv(file_path)
    conditions = list(set(data[serie].to_list()))
    conditions = [x for x in conditions if x == x ]
    print(conditions)
    counts = []
    dict = {}
    for condition in conditions:
        counts.append(len(data[ data[serie] == condition ]))
        dict[col_names[0]] = conditions
        dict[col_names[1]] = counts
    dataframe = pandas.DataFrame(dict)
    dataframe = dataframe[ col_names ]
    dataframe.to_csv(out_file)
    print(dataframe)

pivot("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv","squirrel_count.csv","Primary Fur Color",["Fur Color","Count"])