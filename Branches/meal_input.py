"""File with search for meal branch"""


import telebot
from telebot import types
import config
import products_input
import timer

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def find_meal(message):
    """Finds meal with the same name that user gave"""

    """
    while True:
        if name_of_meal in recipe.py:
            bot.register_next_step_handler(message.chat.id, products_input.show_meal_info)
        else:
            bot.send_message(message.chat.id, "Блюд с таким именем нет(")
    """


@bot.message_handler(func=lambda message: True, content_types=['text'])
def show_meal_info(message):
    """Shows full info of meal (name, picture, complexity, category, products, time of cooking, etc.)"""

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

