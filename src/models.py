from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            
        }
    
class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)
    url= db.Column(db.String(80), unique=False, nullable=False)
    identity_id = db.Column(db.Integer, db.ForeignKey('identity.id'), nullable=True)
    identity = db.relationship('Identity')
    user = db.relationship('User')

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "url": self.url,
            "identity_id": self.identity_id
        }
    
class Identity(db.Model):  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    url = db.Column(db.String(250))
    
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    url = db.Column(db.String(120), unique=True, nullable=False)
    climate = db.Column(db.String(80), unique=False, nullable=False)
    diameter = db.Column(db.String(80), unique=False, nullable=False)
    gravity = db.Column(db.String(80), unique=False, nullable=False)
    population = db.Column(db.String(80), unique=False, nullable=False)
    terrain = db.Column(db.String(80), unique=False, nullable=False)
    orbital_period = db.Column(db.String(80), unique=False, nullable=False)
    rotation_period = db.Column(db.String(80), unique=False, nullable=False)
    identity_id = db.Column(db.Integer, db.ForeignKey('identity.id'), nullable=True)
    identity = db.relationship('Identity')

    def serialize(self):
        return {
            "uid": self.id,
            "name": self.name,
            "url": self.url
        }
    
    def serialize_byId(self):
        return {            
            "name": self.name,
            "climate": self.climate,
            "diameter":self.diameter,
            "gravity":self.gravity,
            "population":self.population,
            "terrain":self.terrain,
            "orbital_period":self.orbital_period,
            "rotation_period":self.rotation_period,
            "id":self.id
        }
    
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    url = db.Column(db.String(120), unique=True, nullable=False)
    eye_color = db.Column(db.String(80), unique=False, nullable=False)
    hair_color = db.Column(db.String(80), unique=False, nullable=False)
    skin_color = db.Column(db.String(80), unique=False, nullable=False)
    height = db.Column(db.String(80), unique=False, nullable=False)
    mass = db.Column(db.String(80), unique=False, nullable=False)
    gender = db.Column(db.String(80), unique=False, nullable=False)
    birth_year = db.Column(db.String(80), unique=False, nullable=False)
    identity_id = db.Column(db.Integer, db.ForeignKey('identity.id'), nullable=True)
    identity = db.relationship('Identity')

    def serialize(self):
        return {
            "uid": self.id,
            "name": self.name,
            "url": self.url
        }
    
    def serialize_byId(self):
        return {            
            "name": self.name,
            "eye_color": self.eye_color,
            "hair_color":self.hair_color,
            "skin_color":self.skin_color,
            "height":self.height,
            "mass":self.mass,
            "gender":self.gender,
            "birth_year":self.birth_year,
            "id":self.id
        }