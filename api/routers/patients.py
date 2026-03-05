from fastapi import APIRouter, HTTPException, Depends, Query
from api.schemas.patient_schema import PatientRequest
from api.services.patient_service import *
from patients.models import Patient
from api.core.dependencies import get_current_user, require_role

router = APIRouter()


# =========================
# GET ALL PATIENTS
# Pagination + Filtering
# =========================
@router.get("/")
def get_patients(
    disease: str | None = None,
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=50),
    user=Depends(get_current_user)
):

    query = Patient.objects.all()

    # Filtering
    if disease:
        query = query.filter(disease__icontains=disease)

    total = query.count()

    # Pagination
    start = (page - 1) * limit
    end = start + limit

    patients = query[start:end]

    return {
        "page": page,
        "limit": limit,
        "total": total,
        "data": list(patients.values())
    }


# =========================
# GET SINGLE PATIENT
# Any logged-in user
# =========================
@router.get("/{id}")
def get_patient(
    id: int,
    user=Depends(get_current_user)
):

    patient = get_patient_by_id(id)

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    return {
        "id": patient.id,
        "name": patient.name,
        "age": patient.age,
        "disease": patient.disease
    }


# =========================
# CREATE PATIENT
# ADMIN ONLY
# =========================
@router.post("/")
def create(
    data: PatientRequest,
    user=Depends(require_role("ADMIN"))
):

    patient = create_patient(data.dict())

    return {
        "message": "Patient created",
        "id": patient.id
    }


# =========================
# UPDATE PATIENT
# ADMIN ONLY
# =========================
@router.put("/{id}")
def update(
    id: int,
    data: PatientRequest,
    user=Depends(require_role("ADMIN"))
):

    patient = get_patient_by_id(id)

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    update_patient(patient, data.dict())

    return {"message": "Patient updated"}


# =========================
# DELETE PATIENT
# ADMIN ONLY
# =========================
@router.delete("/{id}")
def delete(
    id: int,
    user=Depends(require_role("ADMIN"))
):

    patient = get_patient_by_id(id)

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    delete_patient(patient)

    return {"message": "Patient deleted"}