import sqlite3

#db for places

def connect_place_db():
    return sqlite3.connect("places.db")

def Create_places_table():
    con = connect_place_db()
    print(con)
    cur = con.cursor()
    # query
    cur.execute(""" CREATE TABLE IF NOT EXISTS places (
                id INTEGER PRIMARYKEY AUTOINCRIMENT,
                name TEXT,
                description TEXT,
                city TEXT,
                rating REAL
                ) """)
    con.commit()
    con.close()

def update_place(place_id, name, description, city, rating):
    con = connect_place_db()
    cur = con.cursor()
    # query
    cur.execute(""" 
                UPDATE places 
                SET name = ?, description = ?, city = ?, rating = ? 
                WHERE id = ? """, (name, description, city, rating, place_id))
    con.commit()
    con.close()

def insert_place(name, description, city, rating):
    con = connect_place_db()
    print(con)
    cur = con.cursor()
    cur.execute(""" 
                INSERT INTO places (name, description, city, rating) 
                VALUES (?, ?, ?, ?)""", (name, description, city, rating))
    con.commit()
    con.close()

def get_place(place_id):
    con = connect_place_db()
    cur = con.cursor()
    cur.execute(" SELECT FROM places WHERE id = ? ", (place_id))
    place_from_db = cur.fetchone()
    con.close()
    return place_from_db


def read_places():
    con = connect_place_db()
    cur = con.cursor()
    cur.execute(" SELECT * FROM places ")
    places = cur.fetchall()
    con.close()
    return places

def delete_place(place_id):
    con = connect_place_db()
    cur = con.cursor()
    cur.execute(" DELETE FROM places WHERE id = ? ", (place_id))
    places = cur.fetchall()
    con.close()
    return places

