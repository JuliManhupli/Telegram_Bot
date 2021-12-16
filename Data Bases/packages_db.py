"""
Database which contains information about packages
"""

import connector
from connector import db

cursor = db.cursor(buffered=True)

"""
    Database Recipe (IT WAS MEANT TO BE PACKAGE, BUT I SCREWED UP)
    Tables:
        package;
        category;
        day_users;
        recipe;
        ...
        
"""
cursor.execute("create database recipe;")

"""
Create table package that will contain packages.
"""
cursor.execute("create table package "
               "(id int auto_increment,"
               "package_name varchar (30) not null, "
               "package_description varchar (80),"
               "constraint id_pack_pk primary key(id),"
               "id_day int not null, id_category int not null,"
               "foreign key (id_day) references day_users(id),"
               "foreign key (id_category) references category(id));")

"""
Create table category for categories of Packages.
"""
cursor.execute("create table category"
               "(id int auto_increment,"
               "Category_name varchar(30) not null,"
               "constraint id_cat_pk primary key (id));")


"""
Create table day_users which contain id of the day of the week and weekdays.
"""
cursor.execute("create table day_users"
               "(id int,"
               "Day_of_week varchar(30) not null,"
               "constraint id_day_pk primary key (id));")

"""
Create table recipe to contain steps, ingredients, etc.
"""
cursor.execute("create table recipe"
               "(id int auto_increment,"
               "recipe_name varchar(30) not null,"
               "recipe_description varchar (80),"
               "recipe_ingredients varchar (30),"
               "steps varchar(255),"
               "constraint id_rec_pk primary key(id));")

# Table: Packages
# Fields:
# id
# name
# description
# Monday 1
# Tuesday 1
# Wednesday 1
# Thursday 1
# Friday 1
# Saturday 1
# Sunday 1
#
# Table: Day
# Fields:
# id
# breakfast 1
# lunch 1
# dinner 1
#
# Table: Dish
# From db with dishes