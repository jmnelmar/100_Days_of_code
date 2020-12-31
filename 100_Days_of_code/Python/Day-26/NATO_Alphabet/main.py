import pandas
import csv

file = pandas.read_csv("nato_phonetic_alphabet.csv")

df =pandas.DataFrame(file)

data_dict = { row.letter:row.code for (index, row) in df.iterrows() }

word = input("Write a word to code: ")
result = list()
for c in word:
    if c.upper() in data_dict:
        result.append(data_dict[c.upper()])
    else:
        result.append(c)

print(result)