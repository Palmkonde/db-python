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
# con.execute("CREATE TABLE mobile_phone (id INTEGER PRIMARY KEY, model TEXT, country TEXT, OS TEXT)")
# con.execute("CREATE TABLE mobile_game (id INTEGER PRIMARY KEY, name TEXT, publish_year SMALLINT, downloaded INT, OS TEXT)")

# Insert
# to mobile_phone
con.execute("INSERT INTO mobile_phone (model, country, OS) VALUES ('IPhone 14', 'USA', 'IOS')")
con.execute("INSERT INTO mobile_phone (model, country, OS) VALUES ('Samsung Galaxy S22', 'South Korea', 'Android')")
con.execute("INSERT INTO mobile_phone (model, country, OS) VALUES ('Google Pixel 7', 'USA', 'Android')")
con.execute("INSERT INTO mobile_phone (model, country, OS) VALUES ('Xiaomi 12', 'China', 'Android')")
con.execute("INSERT INTO mobile_phone (model, country, OS) VALUES ('OnePlus 10 Pro', 'China', 'Android')")

# to mobile_game
con.execute("INSERT INTO mobile_game (name, publish_year, downloaded, OS) VALUES ('Angry Birds', 2009, 5000000, 'iOS')")
con.execute("INSERT INTO mobile_game (name, publish_year, downloaded, OS) VALUES ('Candy Crush Saga', 2012, 10000000, 'Android')")
con.execute("INSERT INTO mobile_game (name, publish_year, downloaded, OS) VALUES ('PUBG Mobile', 2018, 100000000, 'Android')")
con.execute("INSERT INTO mobile_game (name, publish_year, downloaded, OS) VALUES ('Clash of Clans', 2012, 50000000, 'iOS')")
con.execute("INSERT INTO mobile_game (name, publish_year, downloaded, OS) VALUES ('Subway Surfers', 2012, 100000000, 'Android')")

con.commit()