import first_try
import json
import telebot
from telebot import types


def add_all_ingredients(*ingredients):
    all_ingredients = []
    for ingredient in ingredients:
        if any(not isinstance(ingredient, str) for ingredient in ingredients):
            raise TypeError("Wrong type of ingredients")
        if ingredient in all_ingredients:
            raise ValueError("This ingredient is already on the list!")
        all_ingredients.append(ingredient)
    with open("ingredients.json", "w") as write_file:
        json.dump(all_ingredients, write_file)


def add_meal(name, ingredients):
    meal_info = []
    meal = {
        "Name": name,
        "Ingredients": ingredients
    }
    meal_info.append(meal)
    with open("meals.json", "w") as write_file:
        json.dump(meal_info, write_file)


def get_products(message):
    first_try.bot.send_message(message.chat.id, "reply")
    meals_amount = 0
    with open("meals.json", "r") as meals_file:
        meals_info = json.load(meals_file)
    with open("ingredients.json", "r") as ingredients_file:
        ingredients_info = json.load(ingredients_file)
    reply = message.text
    first_try.bot.send_message(message.chat.id, "reply")

    # if reply == 'private':
    #     if reply not in ingredients_info:
    #         first_try.bot.send_message(message.chat.id, "Такого продукта нет в списке")
    #     else:
    #         for meal in meals_info:
    #             if meal in meal.get("Ingredients"):
    #                 meals_amount += 1
    #                 first_try.bot.send_message(message.chat.id, meal.name + meals_amount)
    #             else:
    #                 first_try.bot.send_message(message.chat.id, "Нет рецепта с таким продуктом")
    #