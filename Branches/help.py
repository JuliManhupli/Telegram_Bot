"""File with questions and help branch"""

import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def bot_help(message):
    """Displaying menu of help branch"""

    """
    if button "Туториал":
        bot.register_next_step_handler(message.chat.id, tutorial)
    elif button "Вопросы":
        bot.register_next_step_handler(message.chat.id, get_category)
    elif button "Все команды":
        bot.register_next_step_handler(message.chat.id, all_commands)
    elif button "Назад":
        bot.register_next_step_handler(message.chat.id, user_choice)
    """


@bot.message_handler(func=lambda message: True, content_types=['text'])
def tutorial(message):
    """Function with tutorials for each branch"""

    """
    if button "Поиск блюда по названию":
        bot.send_message(message.chat.id, 'Information about branch of search dish by name(meal_input.py)')
    elif button "Поиск блюда по продуктам":
        bot.send_message(message.chat.id, 'Information about branch of search dish by ingredients(product_input.py)')
    elif button "Пакеты":
        bot.send_message(message.chat.id, 'Information about branch of packages(packages.py)')   
    """


@bot.message_handler(func=lambda message: True, content_types=['text'])
def questions(message):
    """Function that displays information about questions"""

    """
    if button "Про что этот бот?":
        bot.send_message(message.chat.id, 'Information about this question')
    elif button "Что такое сложность блюда?":
        bot.send_message(message.chat.id, 'Information about this question')
    elif button "Что такое категории блюда?":
        bot.send_message(message.chat.id, 'Information about this question')
    elif button "Что такое пакеты?":
        bot.send_message(message.chat.id, 'Information about this question')
    elif button "Как работают пакеты?":
        bot.send_message(message.chat.id, 'Information about this question')
    elif button "Как удалить или изменить пакет?":
        bot.send_message(message.chat.id, 'Information about this question')
    elif button "Назад":
        bot.register_next_step_handler(message.chat.id, bot_help)   
    """


def all_commands(message):
    """Function that displays information about all commands"""

    """
    bot.register_next_step_handler(message.chat.id, bot_help)
    """