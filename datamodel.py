from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Patient(db.Model):
    __tablename__ = 'patient'
    
    patient_id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(500), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), nullable=False)