# bank managment


## Table of Contents

- [Service-Oriented Architecture (SOA)](#service-oriented-architecture-soa)
- [Technologies Used](#technologies-used)
-[Additional Features](#Additional-Features)
- [Installation](#installation)
- [Assumptions](#Assumptions)

## Service-Oriented Architecture (SOA)

This project is built using Service-Oriented Architecture (SOA), an architectural pattern that structures the application as a collection of services. Each service is designed to perform a specific business functionality and can communicate with other services through well-defined APIs.

### Key Characteristics of SOA:

- **Modularity:** Services are independent modules, making it easier to develop, test, and deploy.
- **Loose Coupling:** Services communicate through standardized interfaces, reducing dependencies between components.
- **Reusability:** Services can be reused across different parts of the application or in other projects.

### Technologies Used

- [Django](https://www.djangoproject.com/): A high-level Python web framework.
- [Django REST Framework](https://www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs.
- **Vue.js**: A progressive JavaScript framework used for building user interfaces. In this project, Vue.js is used to create dynamic and interactive components for the web application for user's Loan Payment.
- Swagger: Used for API documentation.

## Additional Features

- **Throttling:** Implemented throttling to limit the number of requests to the API, enhancing the security and performance of the application.
- **Atomic Transactions:** Used Django's `@transaction.atomic` decorator to ensure that database transactions are atomic, providing data integrity and consistency.
- **Logging:** Integrated logging throughout the application to track important events and errors, aiding in debugging and monitoring.


## Installation
Follow these steps to set up and run the project locally.

## Prerequisites

Make sure you have the following prerequisites installed on your machine:

- [Python](https://www.python.org/) (version 3.8.10)
- Node.js - You can download it from [Node.js official website](https://nodejs.org/).
- npm - Comes with Node.js, but you can check if it's installed by running `npm -v` in your terminal.


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

## Assumptions

In the development of this bank loan management application, the following assumptions have been made:

1. **Loan Providers:**
   - The total budget provided by loan providers is the maximum amount that can be loaned out to customers.
   - Loan providers do not have individual limits on how much they can contribute to the total loan fund.

2. **Loan Customers:**
   - The loan amount requested by a customer cannot exceed the available funds from loan providers.
   - Each loan should be within the range of loan conficration

3. **Bank Personnel:**
   - Bank personnel are responsible for setting the maximum and minimum loan amounts, interest rates, and loan durations.
   - Interest rates are fixed for the entire duration of the loan.
   - Bank Personnel is the one required to approve loan Applications, Fund, and Loan Payments

4. **Interest Calculation:**
   - The application uses simple interest calculation for all loans.
