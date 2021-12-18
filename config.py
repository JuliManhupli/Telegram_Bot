import mysql.connector

TOKEN = "2137770043:AAHcNPNXfJiaw9zMLZ0Ly5aO8m3mRsthw28"
APP_URL = f'https://first-try-bot.herokuapp.com/{TOKEN}'

db = mysql.connector.connect(
    host="eu-cdbr-west-02.cleardb.net",
    user="b03a444e15195f",
    password="74eda92c",
    database="heroku_0172a37b43bafa6"
)