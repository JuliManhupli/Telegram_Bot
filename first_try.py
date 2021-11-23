import telebot
from telebot import types
import config
import json
import products_input

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Пакеты👥")
    button2 = types.KeyboardButton("Поиск по продуктам👥")
    button3 = types.KeyboardButton("Поиск по названию👥")
    button4 = types.KeyboardButton("Help👥")

    markup.row(button2)
    markup.row(button3)
    markup.row(button1, button4)
    bot.send_message(message.chat.id, "Приветствие", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def user_choice(message):
    if message.chat.type == 'private':
        if message.text == 'Поиск по продуктам👥':
            bot.send_message(message.from_user.id, "Введите продукты")
            bot.register_next_step_handler(message, get_products)
        elif message.text == 'Поиск по названию👥':
            bot.send_message(message.chat.id, "2")
        elif message.text == 'Пакеты👥':
            bot.send_message(message.chat.id, "3")
        elif message.text == 'Help👥':
            bot.send_message(message.chat.id, "4")


def get_products(message):
    meals_amount = 0
    with open("meals.json", "r") as meals_file:
        meals_info = json.load(meals_file)
    with open("ingredients.json", "r") as ingredients_file:
        ingredients_info = json.load(ingredients_file)
    reply = message.text
    bot.send_message(message.chat.id, "reply")


bot.infinity_polling()