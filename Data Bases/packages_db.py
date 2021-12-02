"""
Database which contains information about packages
"""

import connector
from connector import db

cursor = db.cursor(buffered=True)

"""
    Database Recipe. 
    Tables:
        package;
        category;
        day_users;
        recipe;
        ...
        
"""

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