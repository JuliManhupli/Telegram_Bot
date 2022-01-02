import psycopg2

TOKEN = "5043775245:AAHQMUKAfbyvZhS2p3YevxwR5YT-9-d7DP4"
APP_URL = f'https://culinary-bot.herokuapp.com/{TOKEN}'
DB_URL = 'postgres://lznczooiiaxtdm:a00c14251cb705cfba5925444311e8000590da31193bb3338d57f33e158e016a@ec2-63-34-223-144.eu-west-1.compute.amazonaws.com:5432/d53hpkt98jd90q'


db = psycopg2.connect(DB_URL, sslmode='require')

