import sqlite3
with sqlite3.connect('dtbs.db') as conn:
    cursor = conn.cursor()
    script = """Drop table IF EXISTS Roster; 
                Create table Roster (name text, species text, age int);
                Insert into Roster VALUES 
                ('Benjamin Sisko', 'Human', 40), 
                ('Jadzia Dax', 'Trill', 300),
                ('Kira Nerys', 'Bajoran', 29)"""
    a = cursor.executescript(script)
    s = """Update Roster Set name = 'Ezri Dax' where age = 300"""
    cursor.executescript(s)
    b = """SELECT name, age from Roster Where species = 'Bajoran'"""
    cursor.executescript(b)
