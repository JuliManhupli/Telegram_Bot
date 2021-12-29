import random

import telebot
import os
import time
from Classes.classes import Dish
from config import TOKEN, db, APP_URL
from telebot import types
from help import *
from pyrogram.errors import FloodWait
from flask import Flask, request

bot = telebot.TeleBot(TOKEN)
# server = Flask(__name__)
user_dict = {}


@bot.message_handler(commands=['start'])
def welcome(message): \
    # keyboard
    user_dict['select_a'] = []
    user_dict['select_b'] = []


    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button1 = types.KeyboardButton("Случайные блюда")
    button2 = types.KeyboardButton("Поиск по продуктам")
    button3 = types.KeyboardButton("Поиск по названию")
    button4 = types.KeyboardButton("Помощь")

    markup.row(button2)
    markup.row(button3)
    markup.row(button1, button4)

    msg = bot.send_message(message.chat.id,
                           "Готовность к приготовлению есть? Тогда выберите пункт для поиска нового блюда!",
                           reply_markup=markup)
    bot.register_next_step_handler(msg, user_choice)


@bot.message_handler(content_types=['text'])
def user_choice(message):
    if message.text == 'Поиск по продуктам':
        msg = bot.send_message(message.chat.id, "Введите ингредиент, с которым собираетесь готовить!")
        bot.register_next_step_handler(msg, product_input)
    elif message.text == 'Поиск по названию':
        msg = bot.send_message(message.chat.id, "Введите название блюда, которое ищете!")
        bot.register_next_step_handler(msg, find_meal)
    elif message.text == 'Случайные блюда':
        bot.send_message(message.chat.id, text="Выберите случайное блюдо:", reply_markup=keyboard_for_random())
    elif message.text == 'Помощь':
        bot.send_message(message.chat.id, text="Выберите вопрос что интересует", reply_markup=keyboard_for_help())


def keyboard_for_help():
    buttons = [
        [types.InlineKeyboardButton(text="Поиск по продуктам", callback_data="products")],
        [types.InlineKeyboardButton(text="Поиск по названию", callback_data="name")],
        [types.InlineKeyboardButton(text="Вопросы", callback_data="questions")],
    ]
    return types.InlineKeyboardMarkup(buttons)


@bot.callback_query_handler(func=lambda call: call.data in ['products', 'name', 'questions'])
def bot_help(call):
    if call.data == 'products':
        bot.send_message(call.message.chat.id, products)
    elif call.data == 'name':
        bot.send_message(call.message.chat.id, name)
    elif call.data == 'questions':
        bot.send_message(call.message.chat.id, text="Вопросы", reply_markup=keyboard_for_questions())


def keyboard_for_questions():
    buttons = [
        [types.InlineKeyboardButton(text="Что такое пакет?", callback_data="package")],
        [types.InlineKeyboardButton(text="Какие есть категории?", callback_data="complexity")],
        [types.InlineKeyboardButton(text="Какие есть сложности приготовления?", callback_data="category")],
        [types.InlineKeyboardButton(text="Что делает этот бот?", callback_data='use bot')]
    ]
    return types.InlineKeyboardMarkup(buttons)


@bot.callback_query_handler(func=lambda call: call.data in ['package', 'complexity', 'category', 'use bot'])
def answer_markup_for_questions(call):
    if call.data == 'package':
        bot.send_message(call.message.chat.id, package)
    elif call.data == 'complexity':
        bot.send_message(call.message.chat.id, complexity)
    elif call.data == 'category':
        bot.send_message(call.message.chat.id, category)
    elif call.data == 'use bot':
        bot.send_message(call.message.chat.id, use_bot)


@bot.message_handler(content_types=['text'])
def product_input(message):
    bot.reply_to(message, 'Вот ваш ингредиент:')
    search_by_ingredient = Dish()
    search_by_ingredient.ingredient = message.text
    user_dict['ingredient_object'] = search_by_ingredient
    records = search_by_ingredient.get_name_by_ingredient()
    if not records:
        bot.send_message(message.chat.id, "К сожалению блюд c таким ингредиентом не существует(((")
    else:
        if not user_dict.get('select_a'):
            user_dict['select_a'] = records
            bot.send_message(message.chat.id, text="Вводим ещё блюда?", reply_markup=keyboard_for_ingredients())
        else:
            user_dict['select_b'] = records
            select_c = list(set(user_dict['select_a']) & set(user_dict['select_b']))
            if not select_c:
                bot.send_message(message.chat.id, "К сожалению блюд c таким набором ингредиентов не было найдено(((")
                user_dict['select_a'].clear()
                user_dict['select_b'].clear()
            else:
                user_dict['select_a'] = select_c
                bot.send_message(message.chat.id, text="Вводим ещё блюда?", reply_markup=keyboard_for_ingredients())


def keyboard_for_ingredients():
    buttons = [
        [types.InlineKeyboardButton(text="Вводить ещё", callback_data="yes ingredient")],
        [types.InlineKeyboardButton(text="Достаточно", callback_data='no ingredient')]
    ]
    return types.InlineKeyboardMarkup(buttons)


@bot.callback_query_handler(func=lambda call: call.data in ['yes ingredient', 'no ingredient'])
def answer_markup_for_additional_ingredient(call):
    if call.data == 'no ingredient':
        msg = bot.send_message(call.message.chat.id, "Хорошо, тогда приступим к следующему шагу!")
        bot.send_message(msg.chat.id, text="Выберите категорию блюда:", reply_markup=keyboard_for_category())
    elif call.data == 'yes ingredient':
        msg = bot.send_message(call.message.chat.id, "Введите ингредиент, с которым собираетесь готовить!")
        bot.register_next_step_handler(msg, product_input)


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
    user_dict['selected_by_name_and_category'] = []
    if user_dict.get('select_a'):
        user_dict['selected_by_ingredient'] = []
        for tupl in user_dict['select_a']:
            user_dict['selected_by_ingredient'].append(tupl)
    if user_dict.get('select_a'):
        user_dict['select_a'].clear()
    if user_dict.get('select_b'):
        user_dict['select_b'].clear()
    if call.data == "Первое":
        user_dict['ingredient_object'].category = 1
        for pair in user_dict['selected_by_ingredient']:
            user_dict['ingredient_object'].name = pair[0]
            record = user_dict['ingredient_object'].category_check_with_ingredient()
            if record is not None:
                user_dict['selected_by_name_and_category'].append(record[0])
        if not user_dict['selected_by_name_and_category']:
            bot.send_message(call.message.chat.id,
                             "К сожалению блюда с этими ингредиентами в этой категории не было найдено(((")

        else:
            msg = bot.send_message(call.message.chat.id, "Окей, берём первое!")
            bot.send_message(msg.chat.id, "Введите сложность блюда!", reply_markup=keyboard_for_complexity())
    elif call.data == "Второе":
        user_dict['ingredient_object'].category = 2
        for pair in user_dict['selected_by_ingredient']:
            user_dict['ingredient_object'].name = pair[0]
            record = user_dict['ingredient_object'].category_check_with_ingredient()
            if record is not None:
                user_dict['selected_by_name_and_category'].append(record[0])
        if not user_dict['selected_by_name_and_category']:
            bot.send_message(call.message.chat.id,
                             "К сожалению блюда с этими ингредиентами в этой категории не было найдено(((")

        else:
            msg = bot.send_message(call.message.chat.id, "Окей, берём второе!")
            bot.send_message(msg.chat.id, "Введите сложность блюда!", reply_markup=keyboard_for_complexity())
    elif call.data == "Напитки":
        user_dict['ingredient_object'].category = 3
        for pair in user_dict['selected_by_ingredient']:
            user_dict['ingredient_object'].name = pair[0]
            record = user_dict['ingredient_object'].category_check_with_ingredient()
            if record is not None:
                user_dict['selected_by_name_and_category'].append(record[0])
        if not user_dict['selected_by_name_and_category']:
            bot.send_message(call.message.chat.id,
                             "К сожалению блюда с этими ингредиентами в этой категории не было найдено(((")

        else:
            msg = bot.send_message(call.message.chat.id, "Окей, берём напитки!")
            bot.send_message(msg.chat.id, "Введите сложность блюда!", reply_markup=keyboard_for_complexity())
    elif call.data == "Закуски":
        user_dict['ingredient_object'].category = 4
        for pair in user_dict['selected_by_ingredient']:
            user_dict['ingredient_object'].name = pair[0]
            record = user_dict['ingredient_object'].category_check_with_ingredient()
            if record is not None:
                user_dict['selected_by_name_and_category'].append(record[0])
        if not user_dict['selected_by_name_and_category']:
            bot.send_message(call.message.chat.id,
                             "К сожалению блюда с этими ингредиентами в этой категории не было найдено(((")

        else:
            msg = bot.send_message(call.message.chat.id, "Окей, берём закуски!")
            bot.send_message(msg.chat.id, "Введите сложность блюда!", reply_markup=keyboard_for_complexity())
    elif call.data == "Десерт":
        user_dict['ingredient_object'].category = 5
        for pair in user_dict['selected_by_ingredient']:
            user_dict['ingredient_object'].name = pair[0]
            record = user_dict['ingredient_object'].category_check_with_ingredient()
            if record is not None:
                user_dict['selected_by_name_and_category'].append(record[0])
        if not user_dict['selected_by_name_and_category']:
            bot.send_message(call.message.chat.id,
                             "К сожалению блюда с этими ингредиентами в этой категории не было найдено(((")

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
def answer_markup_for_complexity(call):
    user_dict['selected_by_name_category_complexity'] = []
    if call.data == 'easy':
        user_dict['ingredient_object'].complexity = 1
        for pair in user_dict['selected_by_name_and_category']:
            user_dict['ingredient_object'].name = pair[0]
            record = user_dict['ingredient_object'].complexity_check()
            if record is not None:
                user_dict['selected_by_name_category_complexity'].append(record[0])
        if not user_dict['selected_by_name_category_complexity']:
            bot.send_message(call.message.chat.id,
                             "К сожалению блюдо э введённым ингредиентом, выбранными категорией и сложностью не было найдено(((")

        else:
            names = get_list_out_of_fetchall(user_dict['selected_by_name_category_complexity'])
            user_dict['found_dishes_by_name'] = names
            bot.send_message(call.message.chat.id, "Вот блюда, которые соответсвуют всем параметрам:",
                             reply_markup=dish_names_keyboard(names))
    elif call.data == 'medium':
        user_dict['ingredient_object'].complexity = 2
        for pair in user_dict['selected_by_name_and_category']:
            user_dict['ingredient_object'].name = pair[0]
            record = user_dict['ingredient_object'].complexity_check()
            if record is not None:
                user_dict['selected_by_name_category_complexity'].append(record[0])
        if not user_dict['selected_by_name_category_complexity']:
            bot.send_message(call.message.chat.id,
                             "К сожалению блюдо э введённым ингредиентом, выбранными категорией и сложностью не было найдено(((")

        else:
            names = get_list_out_of_fetchall(user_dict['selected_by_name_category_complexity'])
            user_dict['found_dishes_by_name'] = names
            bot.send_message(call.message.chat.id, "Вот блюда, которые соответсвуют всем параметрам:",
                             reply_markup=dish_names_keyboard(names))
    elif call.data == 'hard':
        user_dict['ingredient_object'].complexity = 3
        for pair in user_dict['selected_by_name_and_category']:
            user_dict['ingredient_object'].name = pair[0]
            record = user_dict['ingredient_object'].complexity_check()
            if record is not None:
                user_dict['selected_by_name_category_complexity'].append(record[0])
        if not user_dict['selected_by_name_category_complexity']:
            bot.send_message(call.message.chat.id,
                             "К сожалению блюдо э введённым ингредиентом, выбранными категорией и сложностью не было найдено(((")

        else:
            names = get_list_out_of_fetchall(user_dict['selected_by_name_category_complexity'])
            user_dict['found_dishes_by_name'] = names
            bot.send_message(call.message.chat.id, "Вот блюда, которые соответсвуют всем параметрам:",
                             reply_markup=dish_names_keyboard(names))
    bot.answer_callback_query(call.id)


################################################

@bot.message_handler(content_types=['text'])
def find_meal(message):
    bot.reply_to(message, 'Вот ваше блюдо:')
    search_by_name = Dish()
    search_by_name.name = message.text.lower()
    user_dict['dish_by_name_object'] = search_by_name
    records = search_by_name.get_name_by_name()
    names = get_list_out_of_fetchall(records)
    user_dict['found_dishes_by_name'] = names
    if not records:
        bot.send_message(message.chat.id, "К сожалению такое блюдо не было найдено(((")
    else:
        bot.send_message(message.chat.id, text="Вот блюда, которые мы нашли:", reply_markup=dish_names_keyboard(names))


def get_list_out_of_fetchall(records):
    names = []
    for pair in records:
        names.append(pair[0])
    return names


def dish_names_keyboard(names):
    ids = []
    buttons = []
    for value in names:
        id = Dish.get_id(value)
        buttons.append([types.InlineKeyboardButton(text=value, callback_data=str(id[0][0]))])
        ids.append(str(id[0][0]))
    user_dict['ids'] = ids
    return types.InlineKeyboardMarkup(buttons)


@bot.callback_query_handler(func=lambda call: call.data in user_dict['ids'])
def answer_markup_for_name(call):
    final_dish = Dish()
    final_dish.id = call.data
    user_dict['dish_by_name_object'] = final_dish
    records = final_dish.get_info_by_id()
    recipe = bot.send_message(call.message.chat.id, text=f'{records[0][0]}\n\n\tИнгредиенты: {records[0][1]}\n\n\t'
                                                         f'Время для приготовления: {records[0][3]} минут\n\n\t'
                                                         f'Полный рецепт: {records[0][2]}')
    msg = bot.send_message(recipe.chat.id, text="Вот вся информация про блюдо!")
    bot.send_message(msg.chat.id, text="Начинаем пошаговую готовку?", reply_markup=keyboard_for_steps())
    bot.answer_callback_query(call.id)


def keyboard_for_steps():
    buttons = [
        [types.InlineKeyboardButton(text="Готовить пошагово", callback_data="start steps")],
        [types.InlineKeyboardButton(text="Готовить самостоятельно по рецепту", callback_data='no steps')]
    ]
    return types.InlineKeyboardMarkup(buttons)


@bot.callback_query_handler(func=lambda call: call.data in ['start steps', 'no steps'])
def answer_markup_for_recipe(call):
    if call.data == "no steps":
        msg = bot.send_message(call.message.chat.id, "Хорошо, тогда удачного приготовления!")
    elif call.data == "start steps":
        msg = bot.send_message(call.message.chat.id, "Приступим к пошаговому приготовлению!")
        user_dict['records'] = user_dict['dish_by_name_object'].get_recipe_and_steps_by_id()
        user_dict['iterator'] = 0
        start_timer(msg, user_dict['records'])
        bot.answer_callback_query(call.id)


def start_timer(message, records):
    if user_dict['iterator'] == len(records):
        msg = bot.send_message(message.chat.id, "Готовка законченна!")
    else:
        user_dict['step_time'] = records[user_dict['iterator']][1]
        msg = bot.send_message(message.chat.id, text=records[user_dict['iterator']][0])
        bot.send_message(msg.chat.id, text=f"Запускаем таймер на {user_dict['step_time']} минут?",
                         reply_markup=keyboard_for_timer())


def keyboard_for_timer():
    buttons = [
        [types.InlineKeyboardButton(text="Начать таймер", callback_data="yes timer")],
        [types.InlineKeyboardButton(text="Без таймера", callback_data='no timer')]
    ]
    return types.InlineKeyboardMarkup(buttons)


@bot.callback_query_handler(func=lambda call: call.data in ['yes timer', 'no timer'])
def answer_markup_for_steps(call):
    user_dict['iterator'] += 1
    if call.data == 'no timer':
        msg = bot.send_message(call.message.chat.id, "Хорошо, тогда приступим к следующему шагу!")
        start_timer(msg, user_dict['records'])
    elif call.data == 'yes timer':
        msg = bot.send_message(call.message.chat.id,
                               f"Через {user_dict['step_time']} минут прийдёт сообщение об окончании таймера!")
        time.sleep(user_dict['step_time'])
        start_timer(msg, user_dict['records'])


##############################################


def get_random_dish(message, category):
    category_list = ['Первое:', 'Второе:', 'Напитки:', 'Закуска:', 'Десерт:']
    package = Dish()
    if category:
        ids = Dish.get_random_package(category)
        package.id = ids[0]
        meal = package.get_info_by_id()
        msg = bot.send_message(message.chat.id, category_list[category-1])
        recipe = bot.send_message(msg.chat.id, text=f'{meal[0][0]}\n\n\tИнгредиенты: {meal[0][1]}\n\n\t'
                                                    f'Время для приготовления: {meal[0][3]} минут\n\n\t'
                                                    f'Полный рецепт: {meal[0][2]}')
    else:
        ids = [Dish.get_random_package(1), Dish.get_random_package(2), Dish.get_random_package(3),
           Dish.get_random_package(4), Dish.get_random_package(5)]
        for id_tuple, category_tuple in zip(ids, category_list):
            package.id = id_tuple[0]
            meal = package.get_info_by_id()
            msg = bot.send_message(message.chat.id, category_tuple)
            recipe = bot.send_message(msg.chat.id, text=f'{meal[0][0]}\n\n\tИнгредиенты: {meal[0][1]}\n\n\t'
                                                        f'Время для приготовления: {meal[0][3]} минут\n\n\t'
                                                        f'Полный рецепт: {meal[0][2]}')



def keyboard_for_random():
    buttons = [
        [types.InlineKeyboardButton(text="Пакет", callback_data='random package')],
        [types.InlineKeyboardButton(text="Первое", callback_data='random first')],
        [types.InlineKeyboardButton(text="Второе", callback_data='random second')],
        [types.InlineKeyboardButton(text="Напитки", callback_data='random drink')],
        [types.InlineKeyboardButton(text="Закуски", callback_data='random snacks')],
        [types.InlineKeyboardButton(text="Десерт", callback_data='random dessert')]
    ]
    return types.InlineKeyboardMarkup(buttons)


@bot.callback_query_handler(func=lambda call: call.data in ['random package', 'random first', 'random second',
                                                            'random drink', 'random snacks', 'random dessert'])
def answer_markup_for_random(call):
    if call.data == "random package":
        msg = bot.send_message(call.message.chat.id, "Вот ваш пакет:")
        get_random_dish(msg, None)
    elif call.data == 'random first':
        msg = bot.send_message(call.message.chat.id, "Вот ваше блюдо:")
        get_random_dish(msg, 1)
    elif call.data == 'random second':
        msg = bot.send_message(call.message.chat.id, "Вот ваше блюдо:")
        get_random_dish(msg, 2)
    elif call.data == 'random drink':
        msg = bot.send_message(call.message.chat.id, "Вот ваше блюдо:")
        get_random_dish(msg, 3)
    elif call.data == 'random snacks':
        msg = bot.send_message(call.message.chat.id, "Вот ваше блюдо:")
        get_random_dish(msg, 4)
    elif call.data == 'random dessert':
        msg = bot.send_message(call.message.chat.id, "Вот ваше блюдо:")
        get_random_dish(msg, 5)

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
