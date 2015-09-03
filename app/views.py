from flask import Flask, render_template, request
from app import app


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
	
	
	
