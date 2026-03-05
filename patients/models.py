from django.db import models

# Create your models here.


from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    disease = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    date = models.DateField()
    time = models.TimeField(default="09:00")

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"


from django.db import models

class User(models.Model):

    ROLE_CHOICES = [
        ("ADMIN", "Admin"),
        ("DOCTOR", "Doctor"),
        ("STAFF", "Staff"),
    ]

    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username