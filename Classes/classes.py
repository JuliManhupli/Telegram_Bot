dict = {}


class Meal:
    """Additional class for storing info of products"""
    def __init__(self, name, complexity, category, *products):
        self.name = name
        self.complexity = complexity
        self.category = category
        self.products = products


class Package:
    """Additional class for storing info of packages"""
    def __init__(self, name, breakfast_time, lunch_time, dinner_time):
        self.dinner_time = dinner_time
        self.lunch_time = lunch_time
        self.breakfast_time = breakfast_time
        self.name = name
