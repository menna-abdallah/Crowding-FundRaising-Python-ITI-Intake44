#  version 2 
#  using sqlit ----------> on progress
# 
# import sqlite3

# def initialize_database():
#     conn = sqlite3.connect('database.db')
#     c = conn.cursor()

#     # Create users table if not exists
#     c.execute('''CREATE TABLE IF NOT EXISTS users (
#                  id INTEGER PRIMARY KEY,
#                  first_name TEXT NOT NULL,
#                  last_name TEXT NOT NULL,
#                  email TEXT NOT NULL UNIQUE,
#                  password TEXT NOT NULL,
#                  mobile TEXT NOT NULL UNIQUE
#                  )''')
#     conn.commit()

#     # Create projects table if not exists
#     c.execute('''CREATE TABLE IF NOT EXISTS projects (
#                  id INTEGER PRIMARY KEY,
#                  title TEXT NOT NULL,
#                  details TEXT NOT NULL,
#                  target_amount INTEGER NOT NULL,
#                  start_time TEXT NOT NULL,
#                  end_time TEXT NOT NULL,
#                  owner_id INTEGER NOT NULL,
#                  FOREIGN KEY (owner_id) REFERENCES users(id)
#                  )''')
#     conn.commit()

#     conn.close()

# def connect_database():
#     return sqlite3.connect('database.db')


