import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("create table lang (name, first_appeared)")

cur.execute("insert into lang values (?, ?)",("C",1972))

lang_list = [
    ("Fortran", 1957),
    ("Python", 1991),
    ("Go", 2009)
]

cur.executemany("insert into lang values (?, ?)", lang_list)

cur.execute("select * from lang where first_appeared=:year", {"year":1972})
print(cur.fetchall())

conn.close()