from flask import render_template, flash, redirect, session, url_for, request, g, json
from json import dumps
from flask import make_response
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .forms import LoginForm
from .models import User, Baby, Milestones
from datetime import datetime
from flask import request, jsonify

global milestone_date, title, details, eventdata
global baby_id

milestone_date="0-0-0"
title = "xxx"
details = "xxx"
eventdata = [{"date":"0-0-0","badge":"false","title":"xxx","body": "xxx","classname":"yellow-event"}]
baby_id=1000

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated():
        g.user.last_seen = datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()


@app.route('/')
@app.route('/index')
def index() :
	if g.user is not None and g.user.is_authenticated():
		user = g.user
		nickname = user.nickname.upper()
		return render_template('album_index.html',
                           nickname=nickname)
	return render_template("index.html")
	
	
@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
    	user = g.user
    	nickname = user.nickname.upper()
        return render_template('album_index.html',
                          		nickname=nickname)
                           
    form = LoginForm()
    if form.validate_on_submit():
        
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
                        	
@app.route('/album_index')
@login_required
def album_index() :
	user = g.user
	nickname = user.nickname.upper()
	return render_template("album_index.html", nickname=nickname)
	

@app.route('/album')
@login_required
def album() :
	return render_template("album.html")	
			
@app.route('/start_album', methods=['POST'])
@login_required
def start_album() :
	data = str(request.get_json())
	words = data.split("\n")
	global milestone_date, title, details, eventdata, baby_id
	
	if len(words)>1 :
		user=g.user
		baby = user.baby.all()
			
		date_object = datetime.strptime(words[1], '%m/%d/%Y').date()
		milestone_date = str(date_object)
		baby = Baby(babyname=words[0], birthdate=milestone_date, gender=words[2], author = g.user)
		db.session.add(baby)
		db.session.commit()
		
		
	baby_id = baby.id	
	return baby_id
	
	
@app.route('/baby_names')
@login_required
def baby_names() :
	lst = {'id':[],'baby_names':[]}
	user=g.user
	baby = user.baby.all()
	for p in baby:
		lst['id'].append(p.id)
		lst["baby_names"].append(str(p.babyname).upper())
	return jsonify(result = lst)
	


@app.route('/view_milestone<id>', methods=['POST', 'GET'])
@login_required
def view_milestone(id) :
	global baby_id
	baby_id = id
	return render_template("album_users.html")
	
@app.route('/schedule_with_id')
@login_required
def schedule_with_id():
	global title, details, eventdata
	global baby_id
	user=g.user
	baby = user.baby.all()
	for p in baby :
		if p.id == int(baby_id) :
			if p.gender.lower()== "female" :
				x = "GIRL"
			else :
				x = "BOY"	
			details = "BABY " + x + " " + p.babyname.upper()+" WAS BORN"
			eventdata = [{"date":p.birthdate,"badge":"true","title":"BIRTHDAY","body": details,"classname":"yellow-event"}]
			milestones = p.milestones.all()
			for m in milestones :
				eventdata.append({"date":m.milestonedate,"badge":"true","title":m.title,"body": m.details,"classname":"yellow-event"})
	return make_response(dumps(eventdata))
	
@app.route('/add_milestone_new', methods=['POST'])
@login_required
def add_milestone_new() :
	data = str(request.get_json())
	words = data.split("\n")
	global milestone_date, title, details
	global baby_id
	user=g.user
	baby = user.baby.all()
	for p in baby:
		if p.id == int(baby_id):
			if len(words)>1 :
				date_object = datetime.strptime(words[0], '%m/%d/%Y').date()
				milestone_date = str(date_object)
				milestone = Milestones(milestonedate=milestone_date, title=words[1], details=words[2], author = p)
				db.session.add(milestone)
				db.session.commit()
				title = words[1]
				details = words[2]
	return data
	
		
@app.route('/add_milestone', methods=['POST'])
@login_required
def add_milestone() :
	data = str(request.get_json())
	words = data.split("\n")
	global milestone_date, title, details
	global baby_id
	user=g.user
	baby = user.baby.all()
	for p in baby:
		if p.id == baby_id:
			if len(words)>1 :
				date_object = datetime.strptime(words[0], '%m/%d/%Y').date()
				milestone_date = str(date_object)
				milestone = Milestones(milestonedate=milestone_date, title=words[1], details=words[2], author = p)
				db.session.add(milestone)
				db.session.commit()
				title = words[1]
				details = words[2]
	return data
	
	
@app.route('/schedule')
@login_required
def schedule():
	global title, details, eventdata, baby_id
	user=g.user
	baby = user.baby.all()
	for p in baby :
			if p.gender.lower()== "female" :
				x = "GIRL"
			else :
				x = "BOY"	
			details = "BABY " + x + " " + p.babyname.upper()+" WAS BORN"
			eventdata = [{"date":p.birthdate,"badge":"true","title":"BIRTHDAY","body": details,"classname":"yellow-event"}]
			milestones = p.milestones.all()
			for m in milestones :
				eventdata.append({"date":m.milestonedate,"badge":"true","title":m.title,"body": m.details,"classname":"yellow-event"})
	return make_response(dumps(eventdata))
	
@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()

    login_user(user)
    return redirect(request.args.get('next') or url_for('index'))
  


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

	