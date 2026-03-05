from fastapi import APIRouter, HTTPException, Depends
from api.schemas.appointment_schema import AppointmentRequest
from api.services.appointment_service import *
from api.core.dependencies import get_current_user

router = APIRouter()


@router.get("/")
def get_all(user=Depends(get_current_user)):
    return get_appointments()


@router.post("/")
def book(data: AppointmentRequest, user=Depends(get_current_user)):

    try:
        appointment = create_appointment(data.dict())

        return {
            "message": "Appointment booked",
            "id": appointment.id
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))