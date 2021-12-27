import telebot
import os
import asyncio
import time
from Classes.classes import Dish
from config import TOKEN, db, APP_URL
from telebot import types
from pyrogram.errors import FloodWait
from flask import Flask, request

bot = telebot.TeleBot(TOKEN)
# server = Flask(__name__)
user_dict = {}

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

    msg = bot.send_message(message.chat.id, "Готовность к приготовлению есть? Тогда выберите пункт для поиска нового блюда!", reply_markup=markup)
    bot.register_next_step_handler(msg, user_choice)


@bot.message_handler(content_types=['text'])
def user_choice(message):

    bot.send_message(message.chat.id, "Готовность к приготовлению есть? Тогда выберите пункт для поиска нового блюда!")
    if message.text == 'Поиск по продуктам👥':
        msg = bot.send_message(message.chat.id, "Введите ингредиент, с которым собираетесь готовить!")
        bot.register_next_step_handler(msg, product_input)
    elif message.text == 'Поиск по названию👥':
        msg = bot.send_message(message.chat.id, "Введите название блюда, которое ищете!")
        bot.register_next_step_handler(msg, find_meal)
    elif message.text == 'Пакеты👥':
        c = bot.send_message(message.chat.id, "3")
        # bot.register_next_step_handler(c, packages)
    elif message.text == 'Help👥':
        d = bot.send_message(message.chat.id, "4")
        # bot.register_next_step_handler(d, help)


@bot.message_handler(content_types=['text'])
def product_input(message):
    bot.reply_to(message, 'Вот ваш ингредиент:')
    search_by_ingredient = Dish()
    search_by_ingredient.ingredient = message.text.lower()
    user_dict['ingredient_object'] = search_by_ingredient
    records = search_by_ingredient.get_ingredient()
    if len(records) <= 0:
        bot.send_message(message.chat.id, "К сожалению блюд c таким ингредиентом не было найдено(((")
    else:
        bot.send_message(message.chat.id, text="Выберите категорию блюда:", reply_markup=keyboard_for_category())


def keyboard_for_category():
    buttons = [
        [types.InlineKeyboardButton(text="Первое", callback_data='Первое')],
        [types.InlineKeyboardButton(text="Второе", callback_data='Второе')],
        [types.InlineKeyboardButton(text="Напитки", callback_data='Напитки')],
        [types.InlineKeyboardButton(text="Закуски", callback_data='Закуски')],
        [types.InlineKeyboardButton(text="Десерт", callback_data='Десерт')]
    ]
    return types.InlineKeyboardMarkup(buttons)


@bot.callback_query_handler(func=lambda call: call.data in ['Первое', 'Второе', 'Напитки', 'Закуски', 'Десерт'])
def answer_markup_for_category(call):
    if call.data == "Первое":
        user_dict['ingredient_object'].category = 1
        records = user_dict['ingredient_object'].category_check_with_ingredient()
        if records is None:
            bot.send_message(call.message.chat.id, "К сожалению этот ингредиент в этой категории не было найдено(((")
        else:
            msg = bot.send_message(call.message.chat.id, "Окей, берём первое!")
            bot.send_message(msg.chat.id, "Введите сложность блюда!", reply_markup=keyboard_for_complexity())
    elif call.data == "Второе":
        user_dict['ingredient_object'].category = 2
        records = user_dict['ingredient_object'].category_check_with_ingredient()
        if records is None:
            bot.send_message(call.message.chat.id, "К сожалению этот ингредиент в этой категории не было найдено(((")
        else:
            msg = bot.send_message(call.message.chat.id, "Окей, берём второе!")
            bot.send_message(msg.chat.id, "Введите сложность блюда!", reply_markup=keyboard_for_complexity())
    elif call.data == "Напитки":
        user_dict['ingredient_object'].category = 3
        records = user_dict['ingredient_object'].category_check_with_ingredient()
        if records is None:
            bot.send_message(call.message.chat.id, "К сожалению этот ингредиент в этой категории не было найдено(((")
        else:
            msg = bot.send_message(call.message.chat.id, "Окей, берём напитки!")
            bot.send_message(msg.chat.id, "Введите сложность блюда!", reply_markup=keyboard_for_complexity())
    elif call.data == "Закуски":
        user_dict['ingredient_object'].category = 4
        records = user_dict['ingredient_object'].category_check_with_ingredient()
        if records is None:
            bot.send_message(call.message.chat.id, "К сожалению этот ингредиент в этой категории не было найдено(((")
        else:
            msg = bot.send_message(call.message.chat.id, "Окей, берём закуски!")
            bot.send_message(msg.chat.id, "Введите сложность блюда!", reply_markup=keyboard_for_complexity())
    elif call.data == "Десерт":
        user_dict['ingredient_object'].category = 5
        records = user_dict['ingredient_object'].category_check_with_ingredient()
        if records is None:
            bot.send_message(call.message.chat.id, "К сожалению этот ингредиент в этой категории не было найдено(((")
        else:
            msg = bot.send_message(call.message.chat.id, "Окей, берём десерты!")
            bot.send_message(msg.chat.id, "Введите сложность блюда!", reply_markup=keyboard_for_complexity())
    bot.answer_callback_query(call.id)


def keyboard_for_complexity():
    buttons = [
        [types.InlineKeyboardButton(text="Чайник", callback_data='easy')],
        [types.InlineKeyboardButton(text="Опытный", callback_data='medium')],
        [types.InlineKeyboardButton(text="Мастер-шеф", callback_data='hard')]
    ]
    return types.InlineKeyboardMarkup(buttons)


@bot.callback_query_handler(func=lambda call: call.data in ['easy', 'medium', 'hard'])
def answer_markup_for_category(call):
    if call.data == 'easy':
        user_dict['ingredient_object'].complexity = 1
        records = user_dict['ingredient_object'].category_check_with_ingredient_and_complexity()
        if records is None:
            bot.send_message(call.message.chat.id, "К сожалению блюдо э введённым ингредиентом, выбранными категорией и сложностью не было найдено(((")
        else:
            names = get_list_out_of_fetchall(records)
            user_dict['found_dishes_by_name'] = names
            bot.send_message(call.message.chat.id, "Вот блюда, которые соответсвуют всем параметрам:", reply_markup=dish_names_keyboard(records))
    elif call.data == 'medium':
        user_dict['ingredient_object'].complexity = 2
        records = user_dict['ingredient_object'].category_check_with_ingredient_and_complexity()
        if records is None:
            bot.send_message(call.message.chat.id,
                             "К сожалению блюдо э введённым ингредиентом, выбранными категорией и сложностью не было найдено(((")
        else:
            names = get_list_out_of_fetchall(records)
            user_dict['found_dishes_by_name'] = names
            bot.send_message(call.message.chat.id, "Вот блюда, которые соответсвуют всем параметрам:",
                             reply_markup=dish_names_keyboard(records))
    elif call.data == 'hard':
        user_dict['ingredient_object'].complexity = 3
        records = user_dict['ingredient_object'].category_check_with_ingredient_and_complexity()
        if records is None:
            bot.send_message(call.message.chat.id,
                             "К сожалению блюдо э введённым ингредиентом, выбранными категорией и сложностью не было найдено(((")
        else:
            names = get_list_out_of_fetchall(records)
            user_dict['found_dishes_by_name'] = names
            bot.send_message(call.message.chat.id, "Вот блюда, которые соответсвуют всем параметрам:",
                             reply_markup=dish_names_keyboard(records))
    bot.answer_callback_query(call.id)



################################################

@bot.message_handler(content_types=['text'])
def find_meal(message):
    bot.reply_to(message, 'Вот ваше блюдо:')
    search_by_name = Dish()
    search_by_name.name = message.text.lower()
    user_dict['dish_by_name_object'] = search_by_name
    records = search_by_name.get_name()
    names = get_list_out_of_fetchall(records)
    user_dict['found_dishes_by_name'] = names
    if len(records) <= 0:
        bot.send_message(message.chat.id, "К сожалению такое блюдо не было найдено(((")
    else:
        bot.send_message(message.chat.id, text="Вот блюда, которые мы нашли:", reply_markup=dish_names_keyboard(records))



def get_list_out_of_fetchall(records):

    names = []
    for pair in records:
        names.append(pair[0])
    return names


def dish_names_keyboard(names):
    ids = []
    buttons = []
    for value in names:
        id = Dish.get_id(value[0])
        buttons.append([types.InlineKeyboardButton(text=value[0], callback_data=str(id[0][0]))])
        ids.append(str(id[0][0]))
    user_dict['ids'] = ids
    return types.InlineKeyboardMarkup(buttons)


@bot.callback_query_handler(func=lambda call: call.data in user_dict['ids'])
def answer_markup_for_name(call):

    final_dish = Dish()
    final_dish.id = call.data
    user_dict['dish_by_name_object'] = final_dish
    records = final_dish.get_recipe()
    user_dict['recipe_by_name'] = records[0][0]
    recipe = bot.send_message(call.message.chat.id, text=user_dict['recipe_by_name'])
    msg = bot.send_message(recipe.chat.id, text="Вот весь рецепт блюда")
    bot.send_message(msg.chat.id, text="Начинаем пошаговую готовку?", reply_markup=keyboard_for_timer())
    bot.answer_callback_query(call.id)


def keyboard_for_timer():
    buttons = [
        [types.InlineKeyboardButton(text="Запустить таймер", callback_data="start timer")],
        [types.InlineKeyboardButton(text="Готовить без таймера", callback_data='no')]
    ]
    return types.InlineKeyboardMarkup(buttons)


@bot.callback_query_handler(func=lambda call: call.data in ['start timer', 'no'])
def answer_markup_for_recipe(call):
    if call.data == "no":
        bot.send_message(call.message.chat.id, "Удачной готовки!")
    elif call.data == "start timer":
        msg = bot.send_message(call.message.chat.id, "Приступим к пошаговому приготовлению!")
        # start_timer(msg)
        bot.answer_callback_query(call.id)





# async def start_timer(message):
#     records = user_dict['dish_by_name_object'].get_recipe_steps()
#     for pair in records:
#         step_time = pair[1]
#         msg = bot.send_message(message.chat.id, text=pair[0])
#         new_msg = bot.send_message(msg.chat.id, text="Your time is at:" + step_time)
#         for seconds_left in range(step_time - 1, -1, -1):
#             await asyncio.sleep(1)
#             bot.edit_message_text(new_msg.chat.id, message_id=new_msg.message_id, text="Your time is at:" + seconds_left)



#     # for pair in records:
#     #     step_time = pair[1]
#     #     while step_time and not stoptimer:
#     #         s = step_time % 60
#     #         Countdown_TeLe_TiPs = bot.send_message(message, "Startin the timer")
#     #         finish_msg = bot.send_message(Countdown_TeLe_TiPs.chat.id, "")
#     #         await asyncio.sleep(1)
#     #         step_time -= 1
#     #     bot.send_message(finish_msg.chat.id, "🚨 Beep! Beep!! **TIME'S UP!!!**")
#
#
# @bot.message_handler(commands=['stop_timer'])
# def stop_timer(message):
#     global stoptimer
#     stoptimer = True
#     bot.reply_to(message, "Таймер остановлен!")






bot.polling()

# @bot.message_handler(content_types='text')
# def echo(message: types.Message):
#     bot.send_message(message.from_user.id, message.text)


# @server.route('/' + TOKEN, methods=['POST'])
# def get_message():
#     json_string = request.get_data().decode("utf-8")
#     update = types.Update.de_json(json_string)
#     bot.process_new_updates([update])
#     return "Ok", 200
#

# @server.route('/')
# def webhook():
#     bot.delete_webhook()
#     # bot.remove_webhook()
#     # bot.set_webhook(url=APP_URL)
#     return "Ok", 200


#
# if __name__ == '__main__':
#     server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
