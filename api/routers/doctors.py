from fastapi import APIRouter, HTTPException, Depends
from api.schemas.doctor_schema import DoctorRequest
from api.services.doctor_service import *
from api.core.dependencies import get_current_user, require_role

router = APIRouter()


# GET ALL DOCTORS
@router.get("/")
def get_all(user=Depends(get_current_user)):
    return get_doctors()


# GET SINGLE DOCTOR
@router.get("/{id}")
def get_one(id: int, user=Depends(get_current_user)):

    doctor = get_doctor_by_id(id)

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return doctor


# CREATE DOCTOR (ADMIN ONLY)
@router.post("/")
def create(data: DoctorRequest, user=Depends(require_role("ADMIN"))):

    doctor = create_doctor(data.dict())

    return {
        "message": "Doctor created",
        "id": doctor.id
    }