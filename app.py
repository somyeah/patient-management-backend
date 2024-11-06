from flask import Flask
from flask_restful import Api
from config import Config
from datamodel import db
from patientmgmt import PatientData, PatientList

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

db.init_app(app)

with app.app_context():
    db.create_all()

api.add_resource(PatientList, '/api/patients')
api.add_resource(PatientData, '/api/patients/<int:patient_id>')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)