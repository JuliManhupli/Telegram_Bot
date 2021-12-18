import telebot
import os
from telebot import types
from config import TOKEN, db, APP_URL
from flask import Flask, request


bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

user_dict = {}

class User:
    def __init__(self, name):
        self.name = name


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
    if message.text == 'Поиск по продуктам👥':
        a = bot.send_message(message.chat.id, "Введите продукты")

            # bot.register_next_step_handler(a, products_input)
    elif message.text == 'Поиск по названию👥':
        b = bot.send_message(message.chat.id, "Введите название блюда, которое ищете!")
        bot.register_next_step_handler(b, find_meal)
    elif message.text == 'Пакеты👥':
         c = bot.send_message(message.chat.id, "3")
        # bot.register_next_step_handler(c, packages)
    elif message.text == 'Help👥':
        d = bot.send_message(message.chat.id, "4")
        bot.register_next_step_handler(d, help)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def find_meal(message):
    """Finds meal with the same name that user gave"""
    name = message.text
    bot.reply_to(message, 'Вот ваше блюдо:')

    cursor = db.cursor()
    select = "SELECT meaL_name FROM meal " \
             "WHERE meaL_name LIKE '%"+name+"%'"
    cursor.execute(select)
    records = cursor.fetchall()
    if len(records) == 0:
        bot.send_message(message.chat.id, "None")
    else:
        buttons = []
        for value in records:
            buttons.append([types.InlineKeyboardButton(text=value[0], callback_data=value[0])])
        msg = bot.send_message(message.chat.id, reply_markup=types.InlineKeyboardMarkup(buttons), text="Вот блюда, которые мы нашли:")


# @bot.callback_query_handler(func=lambda call: True)
# def answer_markup_for_name(call):
#     bot.send_message(call.message.chat.id,


def show_recept(message):
    """Shows full info of meal (name, picture, complexity, category, products, time of cooking, etc.)"""

    bot.send_message(message.chat.id, message)


    # cursor = db.cursor()
    # cursor.execute(
    #     "SELECT id, Customer_organization_name, Surname, First_name, Patronymic, Customer_phone_number, Customer_mail FROM Customer")
    # records = cursor.fetchall()
    #
    # for i, id in enumerate(records, start=1):
    #     bot.send_message(message.chat.id, id)
    #
    # a = bot.send_message(message.chat.id, "Here is database")
    # bot.register_next_step_handler(a, get_recipe)
    """
        open("meals_db.py")
        meal_info = "meals_db.py".get("full_meal_information")
        bot.send_message(message.chat.id, meal_info)
        if button "Показать рецепт":
            bot.register_next_step_handler(message.chat.id, get_recipe)
        elif button "Начать готовить":
            bot.register_next_step_handler(message.chat.id, start_cooking)
        elif button "Назад":
            bot.register_next_step_handler(message.chat.id, products_input.show_all_meals)
    """


# @bot.message_handler(content_types=['text'])
# def get_recipe(message):
#     """Shows full recipe of chosen meal"""
#     a = bot.send_message(message.chat.id, "here is the recepy")
#     # bot.register_next_step_handler(a, get_recipe)
#     """
#         open("recipe_db.py")
#         full_recipe = "recipe_db.py".get("recipe")
#         bot.send_message(message.chat.id, full_recipe)
#         if button "Начать готовить":
#             bot.register_next_step_handler(message.chat.id, start_cooking)
#         elif button "Назад":
#             bot.register_next_step_handler(message.chat.id, show_meal_info)
#     """
#
#
#
# bot.polling()

# @bot.message_handler(content_types='text')
# def echo(message: types.Message):
#     bot.send_message(message.from_user.id, message.text)


@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode("utf-8")
    update = types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "Ok", 200


@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    return "Ok", 200


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
