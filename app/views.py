from flask import Flask, render_template, request, url_for, json
from app import app
from flask import jsonify

import os


@app.route('/')
@app.route('/index')
def index() :
	return render_template("index.html")
	
@app.route('/album_index')
def album_index() :
	return render_template("album_index.html")
	
@app.route('/album')
def album() :
	return render_template("album.html")	

	
@app.route('/start_album', methods=['POST'])
def start_album() :
	data = str(request.get_json())
	words = data.split("\n")
	print words
	return data
	
@app.route('/add_milestone', methods=['POST'])
def add_milestone() :
	data = str(request.get_json())
	words = data.split("\n")
	print words
	return data
	

@app.route('/schedule')
def schedule():
	eventData = "[       {          \"date\":\"2015-09-04\",          \"badge\":\"true\",          \"title\":\"Birthday\",          \"body\": \"<p>Baby was born<\/p>\",          \"footer\": \"At Hudson\'s place\",          \"classname\": \"yellow-event\"      },{          \"date\":\"2015-11-20\",          \"badge\":\"true\",          \"title\":\"Tomorrow\",          \"body\": \"<p>Four days to the birthday party<\/p>\",          \"footer\": \"At Hudson\'s place\",          \"classname\": \"yellow-event\"      }    ,{          \"date\":\"2015-11-25\",          \"badge\":\"true\",          \"title\":\"Tomorrow\",          \"body\": \"<p>Four days to the birthday party<\/p>\",          \"footer\": \"At Hudson\'s place\",          \"classname\": \"yellow-event\"      }    	] "
	return eventData
	
	
	