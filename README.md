# Medical App Backend

REST API backend for a medical application built with Django and Django REST Framework.

## Requirements

- Python 3.x
- Django 5.x
- Django REST Framework
- drf-spectacular (API documentation)

## Installation

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## API Endpoints

All endpoints are prefixed with `/api/`.

### Patients

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/patients/` | List all patients |
| POST | `/api/patients/` | Create a new patient |
| GET | `/api/patients/{id}/` | Retrieve a patient |
| PUT | `/api/patients/{id}/` | Update a patient |
| PATCH | `/api/patients/{id}/` | Partially update a patient |
| DELETE | `/api/patients/{id}/` | Delete a patient |
| GET | `/api/patients/{id}/medical-history/` | Get medical history of a patient |

### Insurances

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/insurances/` | List all insurances |
| POST | `/api/insurances/` | Create a new insurance |
| GET | `/api/insurances/{id}/` | Retrieve an insurance |
| PUT | `/api/insurances/{id}/` | Update an insurance |
| PATCH | `/api/insurances/{id}/` | Partially update an insurance |
| DELETE | `/api/insurances/{id}/` | Delete an insurance |

### Medical Records

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/medical-records/` | List all medical records |
| POST | `/api/medical-records/` | Create a new medical record |
| GET | `/api/medical-records/{id}/` | Retrieve a medical record |
| PUT | `/api/medical-records/{id}/` | Update a medical record |
| PATCH | `/api/medical-records/{id}/` | Partially update a medical record |
| DELETE | `/api/medical-records/{id}/` | Delete a medical record |

### Medicals (Doctors)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/medicals/` | List all medicals |
| POST | `/api/medicals/` | Create a new medical |
| GET | `/api/medicals/{id}/` | Retrieve a medical |
| PUT | `/api/medicals/{id}/` | Update a medical |
| PATCH | `/api/medicals/{id}/` | Partially update a medical |
| DELETE | `/api/medicals/{id}/` | Delete a medical |
| POST | `/api/medicals/{id}/toggle-vacation/` | Toggle vacation status |

### Departments

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/departments/` | List all departments |
| POST | `/api/departments/` | Create a new department |
| GET | `/api/departments/{id}/` | Retrieve a department |
| PUT | `/api/departments/{id}/` | Update a department |
| PATCH | `/api/departments/{id}/` | Partially update a department |
| DELETE | `/api/departments/{id}/` | Delete a department |

### Medical Availabilities

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/medical-availabilities/` | List all medical availabilities |
| POST | `/api/medical-availabilities/` | Create a new medical availability |
| GET | `/api/medical-availabilities/{id}/` | Retrieve a medical availability |
| PUT | `/api/medical-availabilities/{id}/` | Update a medical availability |
| PATCH | `/api/medical-availabilities/{id}/` | Partially update a medical availability |
| DELETE | `/api/medical-availabilities/{id}/` | Delete a medical availability |

### Medical Notes

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/medical-notes/` | List all medical notes |
| POST | `/api/medical-notes/` | Create a new medical note |
| GET | `/api/medical-notes/{id}/` | Retrieve a medical note |
| PUT | `/api/medical-notes/{id}/` | Update a medical note |
| PATCH | `/api/medical-notes/{id}/` | Partially update a medical note |
| DELETE | `/api/medical-notes/{id}/` | Delete a medical note |

## API Documentation

Interactive API documentation is available at:

- Swagger UI: `/api/docs/`
- ReDoc: `/api/redoc/`

## Project Structure

```
medical-app-backend/
├── medicalapp/          # Project settings and main URL configuration
├── patients/            # Patients app (Patient, Insurance, MedicalRecord)
├── medicals/            # Medicals app (Medical, Department, MedicalAvailability, MedicalNote)
├── bookings/            # Bookings app (Appointment, MedicalNote for appointments)
├── docs/                # API documentation
├── manage.py
└── requirements.txt
```
