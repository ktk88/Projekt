
print('Питон')
import sqlite3
con = sqlite3.connect("movies.db")
t = "INSERT INTO movies(name,year,rating,genre) VALUES ('Speed',2012,8.0,'action')"
cur = con.cursor()
cur.execute(t)
con.commit()
cur.close()
con.close()     