"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
def string_comparison(line1, line2):
  if type(line1) != str or type(line2) != str:
    return 0 
  elif line1 == line2:
    return 1    
  elif line1 != line2 and line2 == "learn":
    return 3
  elif len(line1) > len(line2) and line2 != "learn":
    return 2
  else:
    return "Неизвестное условие"
  
    
string_comparison(5, 6)
print(string_comparison(5,6))
print(string_comparison(5,"Зима"))
print(string_comparison("Привет","пока"))
print(string_comparison("Привет","Привет"))
print(string_comparison("Python","learn"))
print(string_comparison("Hi","learn"))