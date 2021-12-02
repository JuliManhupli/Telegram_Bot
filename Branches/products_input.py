"""File with product input branch"""


import main
import json
import telebot
import config
from telebot import types
bot = telebot.TeleBot(config.TOKEN)


# def add_all_ingredients(*ingredients):
#     all_ingredients = []
#     for ingredient in ingredients:
#         if any(not isinstance(ingredient, str) for ingredient in ingredients):
#             raise TypeError("Wrong type of ingredients")
#         if ingredient in all_ingredients:
#             raise ValueError("This ingredient is already on the list!")
#         all_ingredients.append(ingredient)
#     with open("ingredients.json", "w") as write_file:
#         json.dump(all_ingredients, write_file)
#
#
# def add_meal(name, ingredients):
#     meal_info = []
#     meal = {
#         "Name": name,
#         "Ingredients": ingredients
#     }
#     meal_info.append(meal)
#     with open("meals.json", "w") as write_file:
#         json.dump(meal_info, write_file)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def get_products(message):
    """Products input"""

    """
    while True:
        product_check()
        input = product
        if button "Добавить еще один ингредиент":
            pass
        elif button "Удалить ингредиент":
            bot.register_next_step_handler(message.chat.id, delete_product)
        elif button "Назад":
            bot.register_next_step_handler(message.chat.id, first_try.user_choice)
    bot.register_next_step_handler(message.chat.id, get_category)
    """


@bot.message_handler(func=lambda message: True, content_types=['text'])
def delete_product(message):
    """Deletes product"""

    """
    dict.remove(product)
    """


@bot.message_handler(func=lambda message: True, content_types=['text'])
def product_check(message):
    """Check whether  product"""

    """
    with open("ingredients.json", "r") as products_file:
        products_info = json.dump(products_file, write_file)
    if product not in products_info:
        bot.send_message(message.chat.id, "Продукт не существует!")
        bot.register_next_step_handler(message.chat.id, get_products)
    else:
        dict.get("products") = product
        bot.register_next_step_handler(message.chat.id, get_products)
    """

    # first_try.bot.send_message(message.chat.id, "reply")
    # chat_id = message.chat.id
    # reply = message.text
    # meal_dict[chat_id] = reply
    # first_try.bot.send_message(message.chat.id, meal_dict[chat_id])
    # msg = bot.reply_to(message, 'Какая категория?')
    # bot.register_next_step_handler(msg, get_category)
    # with open("meals.json", "r") as meals_file:
    #     meals_info = json.load(meals_file)
    # with open("ingredients.json", "r") as ingredients_file:
    #     ingredients_info = json.load(ingredients_file)

    # first_try.bot.send_message(message.chat.id, "reply")

    # if reply == 'private':
    #     if reply not in ingredients_info:
    #         first_try.bot.send_message(message.chat.id, "Такого продукта нет в списке")
    #     else:
    #         for meal in meals_info:
    #             if meal in meal.get("Ingredients"):
    #                 first_try.bot.send_message(message.chat.id, meal.name + meals_amount)
    #             else:
    #                 first_try.bot.send_message(message.chat.id, "Нет рецепта с таким продуктом")


@bot.message_handler(func=lambda message: True, content_types=['text'])
def get_category(message):
    """Choice of category"""

    """
        meal_check()
        if button "Первое":
            dict.get("Category") = "Первое"
        elif button "Второе":
            dict.get("Category") = "Второе"
        elif button "Напитки":
            dict.get("Category") = "Напитки"
        elif button "Закуски":
            dict.get("Category") = "Закуски"
        elif button "Салаты":
            dict.get("Category") = "Салаты"
        elif button "Десерты":
            dict.get("Category") = "Десерты"
        elif button "Назад":
            bot.register_next_step_handler(message.chat.id, get_products)
    bot.register_next_step_handler(message.chat.id, get_complexity)
    """

    # first_try.bot.send_message(message.chat.id, "reply")
    # chat_id = message.chat.id
    # reply = message.text
    # meal_dict[chat_id] = reply
    # first_try.bot.send_message(message.chat.id, meal_dict[chat_id])
    # msg = bot.reply_to(message, 'How old are you?')
    # bot.register_next_step_handler(msg, get_category)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def get_complexity(message):
    """Choice of complexity"""

    """
        meal_check()
        if button "Junior":
            dict.get("Complexity") = "Junior"
        elif button "Middle":
            dict.get("Complexity") = "Middle"
        elif button "Senior":
            dict.get("Complexity") = "Senior"
        elif button "Master Chief":
            dict.get("Complexity") = "Master Chief"
        elif button "Назад":
            bot.register_next_step_handler(message.chat.id, get_category)
    bot.register_next_step_handler(message.chat.id, show_all_meals)
    """


@bot.message_handler(func=lambda message: True, content_types=['text'])
def meal_check(message):
    """Checks whether the meal exist with given"""

    """
        if parameter(category, complexity with input products) in recipe.py:
            Ok
            bot.register_next_step_handler(message.chat.id, func_of_the_next_step)
        else:
            bot.send_message(message.chat.id, "Таких блюд, к сожалению, нет(")
            bot.register_next_step_handler(message.chat.id, previous_func)
    """


@bot.message_handler(func=lambda message: True, content_types=['text'])
def show_all_meals(message):
    """Shows the list of meal for user to choose from"""

    """ 
        show buttons with names of meals
        if button "name1":
            show_meal_info(name1)
        elif button "name2":
            show_meal_info(name2)
        ...
        elif button "Назад":
            bot.register_next_step_handler(message.chat.id, get_complexity)
        bot.register_next_step_handler(message.chat.id, meal_input.show_meal_info)

    """
