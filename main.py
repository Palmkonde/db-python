import sqlite3
import os

db_folder = "db"

if not os.path.exists(db_folder):
    os.makedirs(db_folder)

con = sqlite3.connect(f"{db_folder}/db-demo.db")

"""
mobile_Phone
    - model
    - country 
    - OS

Games
    - name
    - publish year
    - downloaded
    - OS
"""
# Create
con.execute("CREATE TABLE mobile_phone (id INTEGER PRIMARY KEY, model TEXT, country TEXT, OS TEXT)")
con.execute("CREATE TABLE mobile_game (id INTEGER PRIMARY KEY, name TEXT, publish_year SMALLINT, downloaded INT, OS TEXT)")



