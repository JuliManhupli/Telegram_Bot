import mysql.connector

TOKEN = "5043775245:AAHQMUKAfbyvZhS2p3YevxwR5YT-9-d7DP4"
APP_URL = f'https://first-try-bot.herokuapp.com/{TOKEN}'

db = mysql.connector.connect(
    host="eu-cdbr-west-02.cleardb.net",
    user="b03a444e15195f",
    password="74eda92c",
    database="heroku_0172a37b43bafa6"
)

