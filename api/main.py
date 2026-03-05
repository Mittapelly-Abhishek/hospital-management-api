import os
import django

# Initialize Django FIRST
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hospital.settings")
django.setup()

import time
from fastapi import FastAPI, Request
from api.routers import patients, auth, appointments, doctors
from api.core.logger import logger


app = FastAPI(
    title="Hospital Management API",
    version="1.0.0"
)


# Register Routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(patients.router, prefix="/patients", tags=["Patients"])
app.include_router(appointments.router, prefix="/appointments", tags=["Appointments"])
app.include_router(doctors.router, prefix="/doctors", tags=["Doctors"])


@app.get("/")
def home():
    return {"message": "Hospital API running"}


# Logging Middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):

    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    logger.info(
        f"{request.method} {request.url.path} "
        f"Status:{response.status_code} "
        f"Time:{process_time:.4f}s"
    )

    return response