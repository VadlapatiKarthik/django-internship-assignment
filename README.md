# Django Developer Internship Assignment – V. Karthik Rao 

##  Overview

This project is a Django-based REST API system to manage **Clients** and **Projects**.

Each Project is assigned to:
- A specific Client (ForeignKey)
- One or more Users (ManyToMany)

##  Tech Stack

- Django 5.2
- Django REST Framework
- MySQL (backend database)
- Postman (API testing)

---

##  Features

- Create & manage Clients
- Create & manage Projects
- Assign Projects to Users
- RESTful endpoints with DRF ModelViewSets
- Tested using Postman

---

##  Endpoints

| Method | Endpoint               | Description            |
|--------|------------------------|------------------------|
| GET    | `/api/clients/`        | List all clients       |
| POST   | `/api/clients/`        | Create a new client    |
| GET    | `/api/projects/`       | List all projects      |
| POST   | `/api/projects/`       | Create a new project   |

---

##  Setup Instructions

1. Clone the repo and install dependencies:
   ```bash
   pip install django djangorestframework mysqlclient

