from patients.models import Appointment, Patient, Doctor


def create_appointment(data):

    try:
        patient = Patient.objects.get(id=data["patient_id"])
    except Patient.DoesNotExist:
        raise Exception("Patient not found")

    try:
        doctor = Doctor.objects.get(id=data["doctor_id"])
    except Doctor.DoesNotExist:
        raise Exception("Doctor not found")

    if Appointment.objects.filter(
        doctor=doctor,
        date=data["date"],
        time=data["time"]
    ).exists():
        raise Exception("Doctor already booked for this slot")

    return Appointment.objects.create(
        patient=patient,
        doctor=doctor,
        date=data["date"],
        time=data["time"]
    )