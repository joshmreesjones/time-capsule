from bottle import route, static_file, template
from server import HOMEPAGE_NAME, STATIC_FILES_PATH

# Route for homepage
@route("/")
@route("/home") # TODO put default home route in config.yml
def serve_home():
	return static_file(HOMEPAGE_NAME, STATIC_FILES_PATH)

# Route for sample static page
@route("/static")
def serve_static_sample():
	# Get sample page as string
	static_content = open("static/static.html", "r").read()
	# Insert content into shell
	return template("shell", title="Sample static page", content=static_content)

# Route for sample dynamic page
@route("/dynamic")
def serve_dynamic_sample():
	# do things
	return "dynamic"

# Route for static files
@route("/<filename:path>")
def serve_static(filename):
	return static_file(filename, STATIC_FILES_PATH)
