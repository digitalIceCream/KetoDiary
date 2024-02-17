#!/usr/bin/python3

"""
Author:             John-Philipp Vogt
Date:               2024-01-12
Synopsis:           test file.
Filename:           test.py
"""
from objects import *
#import jsonpickle
#import datetime

path = './data/2024/'
filename = 'test'
file = ''.join([path, filename])

Butter = Ingredient('Butter', 82, 2, 1, 8)
MCT = Ingredient('MCT', 91, 0, 0, 8)
BPC = Meal('BPC', [Butter, MCT])      

