from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstap = Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/add-task', methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
    	print "A task was added"
    	return redirect( url_for("index") )
    else: 
        return render_template("add-task.html")

app.run()