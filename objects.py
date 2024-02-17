#!/usr/bin/python3

"""
Author:             John-Philipp Vogt
Date:               2024-01-12
Synopsis:           Objects for the Keto Diary.
Filename:           objects.py
"""
import datetime
import jsonpickle
import os

class Ingredient:
    def __init__(self, name: str, fat: float=0.0, carbohydrates: float=0.0, protein: float=0.0, amount: float=0) -> None:
        self.name = name
        self.macro_nutrients_per_100g = {'fat' : fat, 'net carbohydrates' : carbohydrates, 'protein' : protein}
        self.amount = amount
        self.macro_nutrients_total = {'fat' : round((self.amount/100)*fat, 2),
                                      'net carbohydrates' : round((self.amount/100)*carbohydrates, 2),
                                      'protein' : round((self.amount/100)*protein, 2)}

    def __str__(self):
        return f"{self.name} contains:\n {self.macro_nutrients_total}"

    def info(self) -> str:
        print(f"{self.name} contains per 100g: ")
        for k, v in self.macro_nutrients_per_100g.items():
            print("\t\t",v, "\tgrams of", k)

    def update(self, k: str, v: float) -> None:
        self.macro_nutrients_total.update({k: round((self.amount/100)*v, 2)})

    def total(self):
        print(f"{self.amount} grams of {self.name} contain: ")
        for k, v in self.macro_nutrients_total.items():
            print("\t\t", v, "\tgrams of", k)
        print()
            
class Meal:
    def __init__(self, name: str, list_of_ingredients: list=[]) -> None:
        self.name = name
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.filename = self.date+' - '+self.name
        self.list_of_ingredients = list_of_ingredients
        if len(list_of_ingredients) == 0:
            self.total_macro_nutrients = {'fat' : 0.0, 'net carbohydrates' : 0.0, 'protein' : 0.0}
        else:
            total_fat = 0
            total_carbs = 0
            total_protein = 0
            for ingredient in self.list_of_ingredients:
                total_fat += ingredient.macro_nutrients_total.get('fat')
                total_carbs += ingredient.macro_nutrients_total.get('net carbohydrates')
                total_protein += ingredient.macro_nutrients_total.get('protein')
            self.total_macro_nutrients = {'total fat' : total_fat, 'total net carbohydrates' : total_carbs, 'total proteins' : total_protein}

    def __str__(self):
        return f"{self.name} contains: {self.total_macro_nutrients}"
    
    def info(self) -> None:
        print(f"Ingredients for {self.name} are:\n")
        totals = self.total_macro_nutrients
        for ingredient in self.list_of_ingredients:
            ingredient.total()
        print(f"|{'Total':=^60}|\n")
        print(f"Fat:\t\t\t{totals.get('total fat')}\tgrams\nCarbohydrates:\t\t{totals.get('total net carbohydrates')}\tgrams\nProteins:\t\t{totals.get('total proteins')}\tgrams\n\n")

    def add_ingredient(self, ingredient):
        self.list_of_ingredients.append(ingredient)

    def save(self) -> None:
        filepath = path_to_save_to+self.filename
        meal = jsonpickle.encode(self)
        with open(filepath, 'x') as file:
            file.write(meal)


