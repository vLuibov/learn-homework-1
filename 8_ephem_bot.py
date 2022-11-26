"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import ephem

from datetime import datetime

import settings

logging.basicConfig(level=logging.INFO, filename='bot.log')

def greet_user(update, context): 
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь Telegram!') 

planets = {
        "Mercury": ephem.Mercury(datetime.now()), 
        "Venus": ephem.Venus(datetime.now()), 
        "Mars": ephem.Mars(datetime.now()), 
        "Jupiter": ephem.Jupiter(datetime.now()),
        "Saturn": ephem.Saturn(datetime.now()),
        "Uranus": ephem.Uranus(datetime.now()),
        "Neptune": ephem.Neptune(datetime.now()),
    }

def talk_to_me(update, context):
    user_text = update.message.text                # принять текст пользователя
    find_planet = user_text.capitalize().split()                 # сделать из него список
    for item in find_planet:          # пройтись по каждому элементу списка
      if item in planets:             # найти планету по ключу
        const = ephem.constellation(planets[item])     # передать переменной знaчение из ephem
        print(const)                                # распечатать расположение планеты
        update.message.reply_text(f'Планета {item} находится в созвездии {const}')
      else:                                         # если планеты нет, вернуть текст пользователя
        print(user_text) 
        update.message.reply_text(user_text)
         
def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Bot started")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
