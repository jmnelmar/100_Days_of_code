lst = [1,2,3,4,5]
print(lst)
new_numbers = [ item + 1 for item in lst ]
print(new_numbers)


names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
print(names)
short_names = [ name.upper() for name in names if len(name) < 5 ]
print(short_names)