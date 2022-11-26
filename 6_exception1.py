"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
def hello_user():
  try:
    while True:    
      user_say = input("Как дела? ")
      if user_say == "Хорошо":
        print("Хорошо")
        break
  except KeyboardInterrupt:
    print("Пока!")
           
hello_user()
