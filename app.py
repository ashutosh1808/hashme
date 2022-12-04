from flask import Flask,render_template,request
from hashlib import *


app=Flask(__name__)
@app.route("/")
def home():
	return render_template("index.html")


@app.route()



if __name__=="__main__":
	app.run(debug=True,use_reloader=True)