import string
import pandas as pd
class MenuItem:
    def __init__(self, name, category, restaurant, description, calories, total_fat, saturated_fat,
                 trans_fat, cholesterol, sodium, carbs, dietary_fiber, sugar, protein):
        self.name = name
        self.category = category
        self.restaurant = restaurant
        self.description = description
        self.calories = calories
        self.total_fat = total_fat
        self.saturated_fat = saturated_fat
        self.trans_fat = trans_fat
        self.cholesterol = cholesterol
        self.sodium = sodium
        self.carbs = carbs
        self.dietary_fiber = dietary_fiber
        self.sugar = sugar
        self.protein = protein
        self.next = None # Used for seperate chaining in hashmap

    def to_dict(self):
        return {
            'name': self.name,
            'category': self.category,
            'restaurant': self.restaurant,
            'description': self.description,
            'calories': self.calories,
            'total_fat': self.total_fat,
            'saturated_fat': self.saturated_fat,
            'trans_fat': self.trans_fat,
            'cholesterol': self.cholesterol,
            'sodium': self.sodium,
            'carbs': self.carbs,
            'dietary_fiber': self.dietary_fiber,
            'sugar': self.sugar,
            'protein': self.protein
        }