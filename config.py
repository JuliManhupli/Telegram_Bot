import psycopg2

TOKEN = "2083866513:AAHT-VDh0budXvmH-Dik9savYEV__dYF5n0"

db = psycopg2.connect(
        host='localhost',
        user='culinary_user_bot',
        database='culinary',
        password='123')

