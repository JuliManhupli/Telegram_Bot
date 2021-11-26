import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def start_cooking(message):
    """Function that starts the timer for cooking and displays the cooking steps"""

    """
    open("recipe_db.py")
        steps = "recipe_db.py".get("steps")
    for i in len(steps)
        bot.send_message(message.chat.id, 'steps[i]')
        bot.register_next_step_handler(message.chat.id, start_timer)
    bot.send_message(message.chat.id, 'Bon appetit!')
    bot.register_next_step_handler(message.chat.id, user_choice)
    """


@bot.message_handler(func=lambda message: True, content_types=['text'])
def start_timer(message):
    """Timer function"""

    """
    Timer
    if button "Готово":
        bot.register_next_step_handler(message.chat.id, start_cooking)
    elif button "Назад":
        bot.register_next_step_handler(message.chat.id, get_recipe)
    """