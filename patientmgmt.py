from flask import request
from flask_restful import Resource
from datamodel import db, Patient

class PatientList(Resource):
    def get(self):
        patients = Patient.query.all()
        return [{"patient_id": p.patient_id, "patient_name": p.patient_name, "status": p.status} for p in patients], 200

    def post(self):
        data = request.get_json()
        patient_data = Patient(
            patient_name=data["patient_name"], 
            date_of_birth=data["date_of_birth"], 
            address=data["address"],
            status=data["status"]
        )
        db.session.add(patient_data)
        db.session.commit()
        return {"message": "Patient data successfully added", "patient_id": patient_data.patient_id}, 201

class PatientData(Resource):
    def get(self, patient_id):
        patient = Patient.query.get_or_404(patient_id)
        patient.date_of_birth = str(patient.date_of_birth)
        return {
            "id": patient.patient_id,
            "name": patient.patient_name,
            "date_of_birth": patient.date_of_birth,
            "address": patient.address,
            "status": patient.status
        }, 200

    def put(self, patient_id):
        data = request.get_json()
        patient = Patient.query.get_or_404(patient_id)
        patient.name = data["patient_name"]
        patient.date_of_birth = data["date_of_birth"]
        patient.address = data["address"]
        patient.status = data["status"]
        db.session.commit()
        return {"message": "Patient data successfully edited"}, 200

    def delete(self, patient_id):
        patient = Patient.query.get_or_404(patient_id)
        db.session.delete(patient)
        db.session.commit()
        return {"message": "Patient data successfully deleted"}, 200