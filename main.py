import telebot
from telebot import types
import config
from Branches import products_input
from Branches import meal_input
from Branches import packages

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    """Welcoming func"""
    # keyboard
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button1 = types.KeyboardButton("Пакеты👥")
    button2 = types.KeyboardButton("Поиск по продуктам👥")
    button3 = types.KeyboardButton("Поиск по названию👥")
    button4 = types.KeyboardButton("Help👥")

    markup.row(button2)
    markup.row(button3)
    markup.row(button1, button4)
    bot.send_message(message.chat.id, "Приветствие", reply_markup=markup)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def user_choice(message):
    """Choice of branch"""
    if message.chat.type == 'private':
        if message.text == 'Поиск по продуктам👥':
            a = bot.send_message(message.chat.id, "Введите продукты")
            bot.register_next_step_handler(a, products_input)
        elif message.text == 'Поиск по названию👥':
            b = bot.send_message(message.chat.id, "2")
            bot.register_next_step_handler(b, meal_input)
        elif message.text == 'Пакеты👥':
            c = bot.send_message(message.chat.id, "3")
            bot.register_next_step_handler(c, packages)
        elif message.text == 'Help👥':
            d = bot.send_message(message.chat.id, "4")
            bot.register_next_step_handler(d, help)


bot.infinity_polling()
