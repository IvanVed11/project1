name = input('Введите ваше имя' )
surname = input('Введите фамилию' )
city = input('Введите город, в котором вы живете' )
school = input('введите номер школы' )
class_number = int(input('введите номер класса обучения' ))

print('Сейчас вы будете проходить тест по математике. Будет 5 вопросов. приступим')

counter = 0 

print('Сколько будет 2 в степени 9')

answer_1 = int(input())
if answer_1 == 512:
    counter += 1

print('Вычислите устно: 448 + 7 * 4')

answer_2 = int(input())
if answer_2 == 476:
    counter += 1

print('Найдите значение x: (3x + 75) / 5 = (6x + 42) / 5 Введите числа на 1 строке')

answer_3 = map(int, input().split())
for i in answer_3:
    if i == 11:
        counter += 2
 
print('Округлите число 8.14144571 до десятитысечных')

answer_4 = float(input())
if answer_4 == 8.1425:
    counter += 3

print('Катер прошел 12 км по течению реки и 4  км против течения, затратив на весь путь 2 ч. Чему равна собственная скорость катера, если скорость течения 4 км/ч?')

answer_5 = int(input())
if answer_5 == 24:
    counter += 3
    
print('Поздравляем с прохождением теста!', surname, name, 'ученик', 'школы', school, 'города', city, class_number, 'класса', 'набрал', counter, 'баллов из 10')  