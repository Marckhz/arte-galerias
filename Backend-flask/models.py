import sqlite3 as sql


def insertUser(username, password, email):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("INSERT INTO users( username, password) VALUES(?,?)", (username, password, email))
	con.commit()
	con.close()


def retrieveUsers():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT username, password, email FROM users")
	users = cur.fetchall()
	return users


