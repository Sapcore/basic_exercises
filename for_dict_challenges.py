# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
print('\nTask 1')
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
dict = {}
for student in students:
    dict[student['first_name']] = dict.setdefault(student['first_name'] , 0) + 1

for key, value in dict.items():
    print(f'{key}: {value}')



# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
print('\nTask 2')
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
dict = {}
for student in students:
    dict[student['first_name']] = dict.setdefault(student['first_name'] , 0) + 1

for key, value in dict.items():
    if value == max(dict.values()):
        print(f'Самое частое имя среди учеников: {key}')
        break




# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша
print('\nTask 3')
school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
for i, school_class in enumerate(school_students, 1):
    dict = {}
    for student in school_class:
        dict[student['first_name']] = dict.setdefault(student['first_name'] , 0) + 1

    for key, value in dict.items():
        if value == max(dict.values()):
            print(f'Самое частое имя в классе {i}: {key}')
            break


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2
print('\nTask 4')
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for school_class in school:
    dict_male = {}
    for student in school_class['students']:
        dict_male[is_male[student['first_name']]] = dict_male.setdefault(is_male[student['first_name']], 0) + 1
    print(f"Класс {school_class['class']}: девочки {dict_male.get(False, 0)}, мальчики {dict_male.get(True, 0)}")



# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
print('\nTask 5')
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

boys_class = ''
girls_class = ''
boys_max = 0
girls_max = 0

for sclass in school:
    bcount = 0
    gcount = 0
    for student in sclass['students']:
        if is_male[student['first_name']]:
            bcount += 1
        else:
            gcount += 1
    if bcount > boys_max:
        boys_max = bcount
        boys_class = sclass['class']
    if gcount > girls_max:
        girls_max = gcount
        girls_class = sclass['class']

print(f'Больше всего мальчиков в классе {boys_class}')
print(f'Больше всего девочек в классе {girls_class}')

