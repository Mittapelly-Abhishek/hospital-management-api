from pydantic import BaseModel
from datetime import date, time


class AppointmentRequest(BaseModel):
    patient_id: int
    doctor_id: int
    date: date
    time: time