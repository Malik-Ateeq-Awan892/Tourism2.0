import sqlite3

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def save_db(self):
        con =sqlite3.connect("check.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE CHECKING(name, id)")
        con.close()

    def get_data(self):
        con =sqlite3.connect("check.db")
        cur = con.cursor()
        res = cur.execute("SELECT name FROM sqlite_master")
        res = res.fetchone()
        print(res)
        con.close()

        
"""
con =sqlite3.connect("check.db")
cur = con.cursor()
cur.execute("CREATE TABLE CHECKING(name, id)")
res = cur.execute("SELECT name FROM sqlite_master")
res = res.fetchone()
print(res)
con.close()
"""