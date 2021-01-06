#syntax
#new_dict = { new_key:new_value for item in list }
#new_dict = {new_key:new_value for (key,value) in dict.items() }
#new_dict = {new_key:new_value for (key,value) in dict.items() if test}

import random

names = ["Alex","Beth", "Caroline","Dave","Eleanor","Freddie"]

students_scores = { student:random.randint(1,100) for student in names }
print(students_scores)

passed_students = {
    student[0]:student[1] for student in students_scores.items() if student[1]>60
}
print(passed_students)

