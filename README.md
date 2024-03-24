# bank managment


## Table of Contents

- [Service-Oriented Architecture (SOA)](#service-oriented-architecture-soa)
- [Technologies Used](#technologies-used)
- [Installation](#installation)

## Service-Oriented Architecture (SOA)

This project is built using Service-Oriented Architecture (SOA), an architectural pattern that structures the application as a collection of services. Each service is designed to perform a specific business functionality and can communicate with other services through well-defined APIs.

### Key Characteristics of SOA:

- **Modularity:** Services are independent modules, making it easier to develop, test, and deploy.
- **Loose Coupling:** Services communicate through standardized interfaces, reducing dependencies between components.
- **Reusability:** Services can be reused across different parts of the application or in other projects.

### Technologies Used

- [Django](https://www.djangoproject.com/): A high-level Python web framework.
- [Django REST Framework](https://www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs.
- Swagger: Used for API documentation.

## Installation
Follow these steps to set up and run the project locally.

## Prerequisites

Make sure you have the following prerequisites installed on your machine:

- [Python](https://www.python.org/) (version 3.8.10)


## Clone the Repository

```bash
git clone https://github.com/rowanmekawy/bank_managment
cd your-repo
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Apply Migrations
python manage.py migrate

## Run the Development Server
python manage.py runserver