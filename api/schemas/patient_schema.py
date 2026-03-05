from pydantic import BaseModel


class PatientRequest(BaseModel):
    name: str
    age: int
    disease: str


class PatientResponse(BaseModel):
    id: int
    name: str
    age: int
    disease: str