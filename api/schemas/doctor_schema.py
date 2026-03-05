from pydantic import BaseModel

class DoctorRequest(BaseModel):
    name: str
    specialization: str