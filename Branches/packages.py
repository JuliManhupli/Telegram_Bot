"""File for packages that give dishes everyday"""

import first_try
import json
import telebot
from telebot import types


@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_package(message):
    """Checks whether user chose package already"""

    """
    if package exists:
        show_package()
        if button "Изменить пакет":
            bot.register_next_step_handler(message.chat.id, edit_package)
        elif button "Удалить пакет":
            bot.register_next_step_handler(message.chat.id, delete_package)
        elif button "Назад":
            bot.register_next_step_handler(message.chat.id, user_choice)
    else:
        bot.send_message(message.chat.id, "Вы ещё не активировали пакет!")
        if button "Выбрать пакет":
            bot.send_message(message.chat.id, "Выбрать категорию пакета")
            bot.register_next_step_handler(message.chat.id, choose_category)
        elif button "Назад":
            bot.register_next_step_handler(message.chat.id, user_choice)
    """


@bot.message_handler(func=lambda message: True, content_types=['text'])
def choose_category(message):
    """Chooses category of package"""

    """
        if package exist:
            delete_package()
        if button "name1":
            dict.get("Category") = "name1"
            bot.register_next_step_handler(message.chat.id, choose_time)
        elif button "name2":
            dict.get("Category") = "name2"
            bot.register_next_step_handler(message.chat.id, choose_time)
        ...
        elif button "Назад":
            bot.register_next_step_handler(message.chat.id, check_package)
    """


@bot.message_handler(func=lambda message: True, content_types=['text'])
def choose_time(message):
    """Chooses time of package"""

    """
        if button "Утро":
            dict.get("Time_range") = "Утро"
            bot.register_next_step_handler(message.chat.id, choose_exact_time)
        elif button "День":
            dict.get("Time_range") = "День"
            bot.register_next_step_handler(message.chat.id, choose_exact_time)
        elif button "Вечер":
            dict.get("Time_range") = "Вечер"
            bot.register_next_step_handler(message.chat.id, choose_exact_time)
        elif button "Стандартное время":
            dict.get("Time_range") = "Стандартное время"
            bot.register_next_step_handler(message.chat.id, choose_exact_time)
        elif button "Назад":
            bot.register_next_step_handler(message.chat.id, choose_category)
    """


@bot.message_handler(func=lambda message: True, content_types=['text'])
def choose_exact_time(message):
    """Chooses exact time of package"""

    """
        if parameter(time) in data_base:
            if button "time1":
                dict.get("exact_time") = "time1"
                show_package()
            elif button "time2":
                dict.get("exact_time") = "time2"
                show_package()
                ...
            elif button "Назад":
                bot.register_next_step_handler(message.chat.id, check_package)
        else:
            data_base.get("time")
            show_package()
    """


@bot.message_handler(func=lambda message: True, content_types=['text'])
def show_package(message):
    """Shows full package with info(name, description, time, current day)"""

    """
        open("packages_db.py")
        full_package = "packages_db.py".get("full_package_info")
        bot.send_message(message.chat.id, full_package)
    """


@bot.message_handler(func=lambda message: True, content_types=['text'])
def delete_package(message):
    """Deletes the package for user"""

    """
        dict_packages.remove(package)
    """


@bot.message_handler(func=lambda message: True, content_types=['text'])
def edit_package(message):
    """Edits package"""

    """
        if button "Изменить время":
            bot.register_next_step_handler(message.chat.id, edit_package_with_save)
        elif button "Изменить категорию пакета":
            bot.register_next_step_handler(message.chat.id, edit_package_with_save)
        elif button "Изменить пакет полностью":
            bot.register_next_step_handler(message.chat.id, choose_category)
        elif button "Назад":
            bot.register_next_step_handler(message.chat.id, check_package)
    """


@bot.message_handler(func=lambda message: True, content_types=['text'])
def edit_package_with_save(message):
    """Edits package with parameter"""

    """
        if button "Изменить {parameter}":
           dict.get("parameter") = "given value"
        elif button "Назад":
            bot.register_next_step_handler(message.chat.id, edit_package)
    """
