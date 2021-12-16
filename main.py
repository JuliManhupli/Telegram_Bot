import telebot
from telebot import types
from config import TOKEN, db
bot = telebot.TeleBot(TOKEN)


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


@bot.message_handler(content_types=['text'])
def user_choice(message):
    """Choice of branch"""
    if message.chat.type == 'private':
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


@bot.message_handler(content_types=['text'])
def find_meal(message):
    """Finds meal with the same name that user gave"""
    name = message.text
    meal_name = name
    msg = bot.send_message(message.chat.id, 'Вот ваше блюдо:')
    bot.register_next_step_handler(msg, show_meal_info(msg, meal_name))
    """
    while True:
        if name_of_meal in recipe.py:
            bot.register_next_step_handler(message.chat.id, products_input.show_meal_info)
        else:
            bot.send_message(message.chat.id, "Блюд с таким именем нет(")
    """


@bot.message_handler(content_types=['text'])
def show_meal_info(message, meal_name):
    """Shows full info of meal (name, picture, complexity, category, products, time of cooking, etc.)"""

    b = bot.send_message(message.chat.id, "Here is database")
    cursor = db.cursor()
    cursor.execute(
        "SELECT id, Customer_organization_name, Surname, First_name, Patronymic, Customer_phone_number, Customer_mail FROM Customer")
    records = cursor.fetchall()

    for i, id in enumerate(records, start=1):
        bot.send_message(message.chat.id, id)

    a = bot.send_message(message.chat.id, "Here is database")
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
#


bot.polling()
