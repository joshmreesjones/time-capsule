from bottle import *

app = Bottle()

@app.route("/static/<filepath:path>")
def serve_static(filepath):
	return static_file(filepath, root="/home/josh/cs/content-manager/static")

@app.error(404)
def error404(error):
	return "Sorry, error 404."

@app.route("/download/oneline")
def download_oneline():
	return static_file("one-line.py", root=".", download="one-line.py")

@app.route("/restricted")
def restricted():
	abort(401, "Sorry, access denied.")

@app.route("/wrong")
def redirect_wrong():
	redirect("/right")

@app.route("/right")
def right():
	return "Rightio!"

@app.route("/my_ip")
def show_ip():
	ip = request.environ.get("REMOTE_ADDR")
	return template("Your IP is: {{ip}}", ip = ip)

@app.route("/hello")
@app.route("/hello/<name>")
@view("hello_template")
def hello(name = "World"):
	#return template("hello_template", name = name)
	return dict(name = name)

print(TEMPLATE_PATH)

#@app.route("/")
#def serve_homepage():
#	return static_file("index.html", root="static")

run(app, host="localhost", port=8080 reloader=True)
