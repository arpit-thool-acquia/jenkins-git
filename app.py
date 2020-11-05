from flask import Flask, request, render_template, jsonify, redirect, url_for
from controller import Controller
from database import Database
import json
import sys

#some change
#application config
app = Flask(__name__)
app.config.update(dict(SECRET_KEY='mysecretkey'))
db = Database()
controller = Controller()
#db.dropHistory()

road_type = ""
road_length = 0.0

# Display form
@app.route('/')
def my_form():
	return render_template('input-form.html')

# On receiving input, Process and Display Result
@app.route('/', methods=['POST'])
def my_form_post():
	global road_type
	global road_length
	#Accept User Input
	road_type = request.form['road_type']
	road_length = request.form['road_length']

	#Send data to controller
	output = controller.process(road_type,road_length)
	#db.addHistory(output)


	if(type(output) == str):
		return redirect(url_for('error_page'))
	#Render Result page
	return render_template("result.html", data = output)

@app.route('/history')
def userHistory():
	data = db.fetchHistory()
	return render_template("history.html", data = data)

@app.route('/error')
def error_page():
	return "Invalid Road Length"

if __name__ == '__main__':
	app.run(debug=True)
