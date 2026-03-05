# 🏥 Hospital Management System API

A backend **Hospital Management System** built using **FastAPI** for API logic and **Django ORM** for database models.

This project provides APIs for managing **patients, doctors, and appointments** with **JWT authentication** and **role-based access control**.

---

# 🚀 Features

* 🔐 **JWT Authentication**
* 👥 **Role-Based Access Control**
* 🧑‍⚕️ Doctor Management
* 🧑 Patient Management
* 📅 Appointment Booking
* 📄 Pagination & Filtering
* 📝 Request Logging
* 🧱 Clean Architecture (Routers / Services / Schemas)

---

# 🛠 Tech Stack

* **FastAPI** – API Framework
* **Django ORM** – Database Models
* **PostgreSQL** – Database
* **JWT** – Authentication
* **Loguru** – Logging

---

# 📂 Project Structure

```
hospital-management-system
│
├── api
│   ├── routers        # API routes
│   ├── schemas        # Pydantic request/response models
│   ├── services       # Business logic
│   └── core           # Security, dependencies, logging
│
├── patients           # Django app (models)
├── hospital           # Django project settings
│
├── logs               # API logs
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🔑 Authentication

This API uses **JWT authentication**.

### Register

```
POST /auth/register
```

Example request:

```json
{
 "username": "admin",
 "password": "1234",
 "role": "ADMIN"
}
```

### Login

```
POST /auth/login
```

Response:

```json
{
 "access_token": "JWT_TOKEN",
 "token_type": "bearer"
}
```

Use this token in requests:

```
Authorization: Bearer YOUR_TOKEN
```

---

# 👥 User Roles

| Role   | Description                                           |
| ------ | ----------------------------------------------------- |
| ADMIN  | Full access to manage doctors, patients, appointments |
| DOCTOR | Can view patients and appointments                    |
| STAFF  | Can register patients and create appointments         |

---

# 📡 API Endpoints

### Auth

```
POST /auth/register
POST /auth/login
```

### Patients

```
GET /patients
GET /patients/{id}
POST /patients
PUT /patients/{id}
DELETE /patients/{id}
```

Supports:

```
GET /patients?page=1&limit=10
GET /patients?disease=fever
```

### Doctors

```
GET /doctors
GET /doctors/{id}
POST /doctors
```

### Appointments

```
GET /appointments
POST /appointments
```

---

# ⚙️ Setup & Installation

### 1️⃣ Clone repository

```
git clone https://github.com/Mittapelly-Abhishek/hospital-management-api.git
cd hospital-management-api
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
```

Activate:

**Windows**

```
venv\Scripts\activate
```

**Mac/Linux**

```
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Create `.env` file

Example (do not commit this file to GitHub; replace the values with your own local credentials):

```
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your_secret_key
```

---

### 5️⃣ Run migrations

```
python manage.py migrate
```

---

### 6️⃣ Start API server

```
uvicorn api.main:app --reload
```

API docs available at:

```
http://127.0.0.1:8000/docs
```

---

# 🧪 Logging

All API requests are logged in:

```
logs/app.log
```

Example log:

```
GET /patients Status:200 Time:0.02s
POST /auth/login Status:200 Time:0.01s
```

⭐ If you like this project, please consider giving it a star on GitHub!