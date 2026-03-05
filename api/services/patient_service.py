from patients.models import Patient


def get_all_patients():
    patients = Patient.objects.all()
    return list(patients.values())


def get_patient_by_id(patient_id):
    return Patient.objects.filter(id=patient_id).first()


def create_patient(data):
    return Patient.objects.create(**data)


def update_patient(patient, data):
    patient.name = data["name"]
    patient.age = data["age"]
    patient.disease = data["disease"]
    patient.save()
    return patient


def delete_patient(patient):
    patient.delete()