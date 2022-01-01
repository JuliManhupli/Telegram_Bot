import mysql.connector

TOKEN = "5043775245:AAHQMUKAfbyvZhS2p3YevxwR5YT-9-d7DP4"
APP_URL = f'https://culinary-bot.herokuapp.com/{TOKEN}'

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anutka.1257.z",
    database="culinary_bot"
)

