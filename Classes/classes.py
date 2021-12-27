from config import db


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
        return records


    def get_name(self):
        cursor = db.cursor()
        select = f"SELECT meal_name FROM dish WHERE meal_name LIKE '%{self.name}%'"
        cursor.execute(select)
        records = cursor.fetchall()
        return records

    def get_recipe(self):
        cursor = db.cursor()
        select = f"SELECT recipe_text FROM dish WHERE id = '{self.id}'"
        cursor.execute(select)
        records = cursor.fetchall()
        return records

    def get_ingredient(self):
        cursor = db.cursor()
        select = f"SELECT meal_name FROM dish WHERE ingredients LIKE '%{self.ingredient}%'"
        cursor.execute(select)
        records = cursor.fetchall()
        return records

    def category_check_with_ingredient(self):
        cursor = db.cursor()
        select = f"SELECT meal_name FROM dish WHERE ingredients LIKE '%{self.ingredient}%' and category_id = {self.category}"
        cursor.execute(select)
        records = cursor.fetchall()
        if len(records) <= 0:
            return None
        return records

    def category_check_with_ingredient_and_complexity(self):
        cursor = db.cursor()
        select = f"SELECT meal_name FROM dish WHERE ingredients LIKE '%{self.ingredient}%' and category_id = {self.category} and complexity = {self.complexity}"
        cursor.execute(select)
        records = cursor.fetchall()
        if len(records) <= 0:
            return None
        return records

    def get_recipe_steps(self):
        cursor = db.cursor()
        select = f"SELECT recipe_step, step_time FROM recipe WHERE meal_id = (SELECT id from dish WHERE meal_name = '{self.name}')"
        cursor.execute(select)
        records = cursor.fetchall()
        return records
