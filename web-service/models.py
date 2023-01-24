from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2456@localhost/db_Boweldisease'
app.config['SECRET_KEY'] = 'XXXX'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Access(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    patient = db.relationship('Patient',backref=db.backref('patients', lazy=True))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    doctor = db.relationship('Doctor',backref=db.backref('doctors', lazy=True))

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    surname = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(256))

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    surname = db.Column(db.String(80))
    tcno = db.Column(db.String(120), unique=True)

class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imageurl = db.Column(db.Text)
    result = db.Column(db.String(80))

    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    patient = db.relationship('Patient',backref=db.backref('posts', lazy=True))

db.create_all()
