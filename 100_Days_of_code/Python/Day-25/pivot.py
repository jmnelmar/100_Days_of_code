import pandas

def pivot(file_path,file_out, series):
    data = pandas.read_csv(file_path)
    #dataframe = pandas.DataFrame(data,columns=[series])
    dataframe = pandas.DataFrame(data, columns=series).pivot_table(index=series, aggfunc="size")
    print(dataframe)
    dataframe.to_csv("squirrel_count.csv")

pivot("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv", "pivot.csv",["Primary Fur Color","Highlight Fur Color"])
