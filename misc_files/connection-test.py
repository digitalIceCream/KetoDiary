#!/usr/bin/python3

"""
Author:             John-Philipp Vogt
Date:               2023-11-09
Synopsis:           Testing psycopg2 library
Filename:           MacroTracker.py
"""

import os
import urllib.parse as up
import psycopg2

up.uses_netloc.append("postgres")
url = up.urlparse("postgres://gbstolcl:K0unF2FsD6ob_zjea6mpHpO54xl3uUDm@hattie.db.elephantsql.com/gbstolcl")
conn = psycopg2.connect(database=url.path[1:],
user=url.username,
password=url.password,
host=url.hostname,
port=url.port
)
