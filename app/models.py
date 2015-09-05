from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    baby = db.relationship('Baby', backref='author', lazy='dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.nickname)
        
class Baby(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	babyname = db.Column(db.String(64), index=True, unique=True)
	birthdate = db.Column(db.String(64), index=True, unique=True)
	gender = db.Column(db.String(64), index=True, unique=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	milestones = db.relationship('Milestones', backref='author', lazy='dynamic')
	
	def __repr__(self):
		return '<Baby %r>' % (self.id)
		

class Milestones(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	milestonedate = db.Column(db.String(64), index=True, unique=True)
	title = db.Column(db.String(64), index=True, unique=True)
	details = db.Column(db.String(120), index=True, unique=True)
	baby_id = db.Column(db.Integer, db.ForeignKey('baby.id'))
	
	def __repr__(self):
		return '<Baby %r>' % (self.title)