from config import db
import random

class Dish:
    def __init__(self):
        self.id = None
        self.name = None
        self.recipe = None
        self.ingredient = None
        self.category = None
        self.complexity = None

    @staticmethod
    def get_id(name):
        cursor = db.cursor()
        select = f"SELECT id FROM dish WHERE meal_name = '{name}'"
        cursor.execute(select)
        records = cursor.fetchall()
        cursor.close()
        return records

    def get_name_by_name(self):
        cursor = db.cursor()
        title_name = self.name.title()
        lower_name = self.name.lower()
        select_title = f"SELECT meal_name FROM dish WHERE meal_name LIKE '%{title_name}%'"
        select_lower = f"SELECT meal_name FROM dish WHERE meal_name LIKE '%{lower_name}%'"
        cursor.execute(select_title)
        records_tl = cursor.fetchall()
        cursor.close()
        cursor = db.cursor()
        cursor.execute(select_lower)
        records_lw = cursor.fetchall()
        for tpl in records_lw:
            records_tl.append(tpl)
        cursor.close()
        return records_tl

    def get_info_by_id(self):
        cursor = db.cursor()
        select = f"SELECT meal_name, ingredients, recipe_text, sum(step_time) FROM dish, recipe WHERE dish.id = {self.id} and meal_id = {self.id} GROUP BY dish.id"
        cursor.execute(select)
        records = cursor.fetchall()
        cursor.close()
        return records

    def get_name_by_ingredient(self):
        cursor = db.cursor()
        select = f"SELECT meal_name FROM dish WHERE ingredients LIKE '%{self.ingredient}%'"
        cursor.execute(select)
        records = cursor.fetchall()
        cursor.close()
        return records

    def category_check_with_ingredient(self):
        cursor = db.cursor()
        select = f"SELECT meal_name FROM dish WHERE meal_name = '{self.name}' and category_id = {self.category}"
        cursor.execute(select)
        records = cursor.fetchall()
        cursor.close()
        if len(records) == 0:
            return None
        return records

    def complexity_check(self):
        cursor = db.cursor()
        select = f"SELECT meal_name FROM dish WHERE meal_name = '{self.name}' and category_id = {self.category} and complexity = {self.complexity}"
        cursor.execute(select)
        records = cursor.fetchall()
        cursor.close()
        if len(records) == 0:
            return None
        return records

    def get_recipe_and_steps_by_id(self):
        cursor = db.cursor()
        select = f"SELECT recipe_step, step_time FROM recipe WHERE meal_id = (SELECT id from dish WHERE id = '{self.id}')"
        cursor.execute(select)
        records = cursor.fetchall()
        cursor.close()
        return records

    @staticmethod
    def get_random_package(category):
        cursor = db.cursor()
        select = f"SELECT id FROM dish WHERE category_id = {category}"
        cursor.execute(select)
        records = cursor.fetchall()
        cursor.close()
        return random.choice(records)


