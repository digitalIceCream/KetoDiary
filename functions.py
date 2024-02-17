#!/usr/bin/python3

"""
Author:             John-Philipp Vogt
Date:               2024-01-12
Synopsis:           Functions for Keto Diary.
Filename:           functions.py
"""
import os
import pprint
import time

import objects as kdo

breakstatements = ['stop', 'break', 'back', 'halt']
correctly_formatted_answers = ('n', 'y')

def make_paths(path_to_save_to):
    if not os.path.exists(path_to_save_to):
        os.makedirs(path_to_save_to)
        print('New path to save files created.')
    else:
         print('No new paths created.')

def load_todays_data():
    None

def clear():
    os.system('clear')
    
def confirm_user_input(user_input_to_confirm) -> str:
    """ To confirm data input by user. Pretty prints data with pprint. Returns only values
    from correctly_formatted_answers[]'. """
    while True:
        print(f"\nYour input was: \n\n{user_input_to_confirm}")
        user_input_confirmation_response = input("\nIs that correct? [y/n] -> ").lower()
        if user_input_confirmation_response not in correctly_formatted_answers:
            print('Please try again.')
            continue
        else:
            return user_input_confirmation_response

# Menu navigation

def get_choice() -> str:
    """ To guide the user through options """
    print('1 -- Show me today\'s total. (not implemented yet)')
    print('2 -- Record a new meal.')
    print('3 -- End programme.\n')
    choice = input('Your choice ->  ')
    return choice


# UI/UX functionality to handle user input


def get_meal_name() -> object:
    """"To get a meal name from user"""
    global breakstatements
    while True:
        clear()
        meal_name = input('Give your meal a name ->  ')
        if meal_name.lower() in breakstatements: 
            print(f"Triggered breakstatement: {meal_name}")
            time.sleep(3)
            return
        user_input_confirmation_response = confirm_user_input(meal_name)
        if user_input_confirmation_response == 'y':
            clear()
            meal = kdo.Meal(meal_name)
            return meal
        else:
            print('Please try again.')
            continue
 
def get_ingredients(meal) -> object:
    """To get ingredients for the meal and return a custom object"""
    global breakstatements
    while True:
        meal.info()
        user_input_ingredient = input('Name of ingredient to add: ')
        if user_input_ingredient.lower() in breakstatements: 
            print(f"Triggered breakstatement: {meal}")
            time.sleep(3)
            return 
        user_input_confirmation_response = confirm_user_input(user_input_ingredient)
        if user_input_confirmation_response == 'y':
            clear()
            user_input_total = float(input(f'How many grams of {user_input_ingredient} in total?\n-> '))
            ingredient = kdo.Ingredient(name=user_input_ingredient, amount=user_input_total) 
            for k,v in ingredient.macro_nutrients_per_100g.items():
                amount = float(input(f'How much {k} per 100g in {user_input_ingredient}?\n-> '))
                ingredient.update(k, amount)
            user_input_confirmation_response = confirm_user_input(ingredient)
            if user_input_confirmation_response == 'y':
                meal.add_ingredient(ingredient)
                meal.info()
                user_input_response = input(f'Add more ingredients to {meal.name}? [y/n] -> ')
                user_input_response = confirm_user_input(user_input_response)
                if user_input_confirmation_response == 'y':
                    continue
                else:
                    return meal
            elif user_input_confirmation_response == 'n':
                print("Please try again.")
                continue
