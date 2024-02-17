#!/usr/bin/python3

"""
Author:             John-Philipp Vogt
Date:               2024-01-12
Synopsis:           Main file for execution.
Filename:           main.py
"""
import datetime
import time
import os

import objects as kdo
import functions as kdf

DATA_DIR = os.path.expanduser('~/Documents/Keto Diary/data/')
year = datetime.datetime.now().strftime("%Y")
month_name = datetime.datetime.now().strftime("%B")
path_to_save_to = os.path.join(DATA_DIR, year, month_name, '')


"""
# Test object(Meal)
Butter = kdo.Ingredient('Butter', 82, 2, 1, 8)
MCT = kdo.Ingredient('MCT', 91, 0, 0, 8)
BPC = kdo.Meal('BPC', [Butter, MCT])      
"""
# Preperatory

kdf.make_paths(path_to_save_to)
time.sleep(1)
kdf.clear()

# Main program -- exec

print('\nWelcome to the MacroDiary!!\nWhat do you want to do?\n')

# Main programme loop

while True:
    choice = kdf.get_choice()
    if choice == '1':  # Shows today's total (tbi)
        kdf.retrieve_todays_total(file_total, path)
        #  Insert function here that retrieves all totals for a given day (or just today).
        #  It should retrieve those that mdf.store_total_as_json() can write to storage.
        #  It should then sum them up and display the sum.
        #  And then it should continue to the main menu.
        continue

    elif choice == '2':  # Record a new meal
        while True:
            meal = kdf.get_meal_name()  # Makes user create a meal() object
            meal = kdf.get_ingredients(meal)
            print(f'Your meal contains:')
            meal.info()
            meal.self()
            break

    elif choice == '3':  # Exits
        print('Exiting programme.')
        break

    else:  # Input confirmation
        print('Invalid input')
        continue
    

print("End of program.")  # Signal prompt that the show is over

#---------------------------------------------------------------#
