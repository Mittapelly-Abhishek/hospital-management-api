from patients.models import Doctor


def create_doctor(data):
    return Doctor.objects.create(**data)


def get_doctors():
    return list(Doctor.objects.all().values())


def get_doctor_by_id(doctor_id):
    return Doctor.objects.filter(id=doctor_id).first()