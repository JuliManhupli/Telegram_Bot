"""File with search for meal branch"""


import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

meal_name = ""


def find_meal(message):
    """Finds meal with the same name that user gave"""
    name = message.text
    meal_name = name
    msg = bot.send_message(message.chat.id, 'Вот ваше блюдо:')
    bot.register_next_step_handler(msg, show_meal_info)
    """
    while True:
        if name_of_meal in recipe.py:
            bot.register_next_step_handler(message.chat.id, products_input.show_meal_info)
        else:
            bot.send_message(message.chat.id, "Блюд с таким именем нет(")
    """


def show_meal_info(message, meal_name):
    """Shows full info of meal (name, picture, complexity, category, products, time of cooking, etc.)"""
    bot.send_message(message.chat.id, meal_name)
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


@bot.message_handler(func=lambda message: True, content_types=['text'])
def get_recipe(message):
    """Shows full recipe of chosen meal"""

    """
        open("recipe_db.py")
        full_recipe = "recipe_db.py".get("recipe")
        bot.send_message(message.chat.id, full_recipe)
        if button "Начать готовить":
            bot.register_next_step_handler(message.chat.id, start_cooking)
        elif button "Назад":
            bot.register_next_step_handler(message.chat.id, show_meal_info)
    """

