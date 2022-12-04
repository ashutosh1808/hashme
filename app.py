from flask import Flask,render_template,request
from hashlib import *

app=Flask(__name__)
@app.route("/")
def home():
	return render_template("index.html")


@app.route("/hash",methods=['POST'])
def hash():
	data=request.form["data"]
	new_data,hashed_data="",""
	new_data=sha256(data.encode())
	hashed_data=new_data.hexdigest()
	msg="Hashed value: "+str(hashed_data) 
	return render_template("index.html",msg=msg)

if __name__=="__main__":
	app.run(debug=True,use_reloader=True)