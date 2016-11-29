import sqlite3
from bottle import debug, get, os, post, request, route, run, static_file, template

STATIC_FILES_PATH = "static"
TEMPLATES_PATH    = "views"
DB_FILENAME       = "cms.db"

@route("/feed")
def show_feed():
	# Connect to the database
	connection = sqlite3.connect(DB_FILENAME)
	cursor = connection.cursor()

	# Create articles table if it doesn't exist
	cursor.execute("CREATE TABLE IF NOT EXISTS articles (title, author, content)")

	# Get all articles
	cursor.execute("SELECT * FROM articles")
	articles = cursor.fetchall()

	# Close the database
	connection.commit()
	connection.close()

	return template(TEMPLATES_PATH + "/feed.tpl", articles=articles)

@get("/submit")
def show_submit():
	return static_file("submit.html", STATIC_FILES_PATH)

@post("/submit")
def process_submit():
	# Create new or connect to existing database
	connection = sqlite3.connect(DB_FILENAME)
	cursor = connection.cursor()

	# Create articles table if it doesn't exist
	cursor.execute("CREATE TABLE IF NOT EXISTS articles (title, author, content)")

	# Get form data
	title = request.POST.get("title")
	author = request.POST.get("author")
	content = request.POST.get("content")

	# Add form data into database
	cursor.execute("INSERT INTO articles VALUES (?,?,?)", (title, author, content))

	# Close the database
	connection.commit()
	connection.close()

	return static_file("confirm_submit.html", STATIC_FILES_PATH)

@route("/<filename:path>")
def serve_static(filename):
	return static_file(filename, STATIC_FILES_PATH)

if __name__ == "__main__":
	debug(True)
	run(reloader = True)
