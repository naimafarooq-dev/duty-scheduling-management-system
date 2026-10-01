# Duty Scheduling Management System

A web-based **Duty Scheduling Management System** developed with **Python and Django** to streamline employee management, event-based duty assignment, monthly scheduling, NFD queue management, and reporting.

The system provides a centralized platform where authorized users can manage employees, events, duties, and scheduling records through a web-based dashboard. It also includes **Django Admin** for administrative management of users and application data.

The application is deployed on **Vercel** and connected to a production **MySQL database hosted on Railway**.

---

## Live Application

### Web Application

https://duty-scheduling-management-system.vercel.app

### Django Admin

https://duty-scheduling-management-system.vercel.app/admin/

> The web application and Django Admin use the same production MySQL database hosted on Railway.

---

# Features

## User Authentication

The system provides secure authentication and session management through Django.

* User login and logout
* HR number-based login
* Password authentication
* Session-based authentication
* Role-based access control
* Separate access for authorized scheduling users and regular users

---

## Employee Management

The employee management functionality allows authorized users to maintain employee records used throughout the scheduling process.

* Add employee records
* Maintain employee information
* Track active employees
* Use active employees for duty assignment
* Manage employee-related scheduling information

---

## Duty Scheduling

The system supports both manual and automated duty scheduling.

* Manual duty assignment
* Event-based duty assignment
* View assigned duties
* Edit assigned duties
* Delete assigned duties
* Automated monthly duty scheduling
* Scheduling based on available employee records
* Application-specific scheduling rules

---

## Event Management

Events represent activities that require employee duty assignments.

* Create and manage events
* Associate events with duty assignments
* Retrieve event information for scheduling
* Identify weekend events
* Organize duties according to events

---

## NFD Queue Management

The system includes an NFD queue as part of the scheduling workflow.

* Generate NFD records
* Maintain the NFD queue
* Manage employees within the queue
* Delete NFD records
* Support scheduling decisions through queue management

---

## Dashboard

The system provides a centralized dashboard for authorized scheduling users.

The dashboard provides access to:

* Employee information
* Events
* Duty assignments
* Automated scheduling
* NFD queue
* Reports
* Scheduling management functions

Regular users have access to functionality according to their assigned permissions.

---

## Reporting

The system provides reporting functionality for duty and scheduling information.

Supported formats include:

* **PDF**
* **Microsoft Word**

PDF reports are generated using **ReportLab**, while Word documents are generated using **python-docx**.

---

## Django Admin

The project includes Django's built-in administrative interface.

Authorized superusers can use Django Admin to manage:

* Users
* Employee records
* Events
* Duty records
* NFD records
* Other registered application data

Django Admin is part of the same deployed Django application and uses the same production database.

---

# How the System Works

The system follows a centralized workflow for authentication, employee management, event management, duty assignment, scheduling, and reporting.

```text
                         User
                           │
                           ▼
                    ┌─────────────┐
                    │    Login    │
                    └──────┬──────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │  Authentication │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │  Role-Based     │
                  │ Access Control  │
                  └────────┬────────┘
                           │
             ┌─────────────┴─────────────┐
             │                           │
             ▼                           ▼
    ┌─────────────────┐        ┌─────────────────┐
    │ Employee/User   │        │    Suprident    │
    │    Dashboard    │        │    Dashboard    │
    └─────────────────┘        └────────┬────────┘
                                        │
                       ┌────────────────┼────────────────┐
                       │                │                │
                       ▼                ▼                ▼
                 ┌──────────┐     ┌──────────┐    ┌───────────┐
                 │  Events  │     │  Duties  │    │ NFD Queue │
                 └────┬─────┘     └────┬─────┘    └───────────┘
                      │                │
                      └────────┬───────┘
                               ▼
                     ┌─────────────────┐
                     │ Duty Scheduling │
                     └────────┬────────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
                    ▼                   ▼
             ┌──────────────┐    ┌──────────────┐
             │    Manual    │    │   Automatic  │
             │   Assignment │    │   Scheduling │
             └──────┬───────┘    └──────┬───────┘
                    │                   │
                    └─────────┬─────────┘
                              ▼
                     ┌─────────────────┐
                     │  Duty Records   │
                     └────────┬────────┘
                              │
                              ▼
                     ┌─────────────────┐
                     │    Reports      │
                     │   PDF / Word    │
                     └─────────────────┘
```

## Workflow

### 1. Login

Users access the system through the login page using their HR number and password.

Django authentication verifies the credentials and creates an authenticated session.

### 2. Role-Based Access

After authentication, the system determines the user's permissions and provides access to the appropriate dashboard and functionality.

Authorized scheduling users can perform scheduling operations, while regular users receive access according to their assigned permissions.

### 3. Employee Management

Employee records are maintained within the system.

Active employees are made available to the duty scheduling functionality when creating assignments.

### 4. Event Management

Events represent activities that require employee duty assignments.

Event information is stored in the database and used to organize duty assignments.

Weekend events can also be identified during the scheduling process.

### 5. Duty Assignment

Authorized users can manually assign employees to specific events and duties.

The system also supports automated monthly duty scheduling using employee and event information together with the application's scheduling rules.

### 6. NFD Queue

The NFD queue forms part of the scheduling workflow.

Employees can be organized within the queue according to the requirements of the scheduling process.

### 7. Duty Records

When a duty assignment is created, the information is stored in the MySQL database.

Duty records can subsequently be:

* Viewed
* Edited
* Deleted
* Included in generated reports

### 8. Reporting

Stored scheduling information can be converted into formal reports.

The system supports:

* PDF report generation using **ReportLab**
* Word document generation using **python-docx**

### 9. Administrative Management

System administrators can access Django Admin to manage users and registered application models.

The custom dashboard is intended for day-to-day scheduling operations, while Django Admin provides administrative control over the application's data.

---

# Technology Stack

| Technology        | Purpose                                         |
| ----------------- | ----------------------------------------------- |
| **Python**        | Backend programming language                    |
| **Django 5.2**    | Web framework and backend architecture          |
| **MySQL**         | Relational database                             |
| **PyMySQL**       | MySQL database connectivity                     |
| **HTML5**         | Frontend structure                              |
| **CSS3**          | Custom interface styling                        |
| **JavaScript**    | Client-side functionality and interactions      |
| **Bootstrap 5.3** | Responsive layout and utility classes           |
| **ReportLab**     | PDF report generation                           |
| **python-docx**   | Microsoft Word report generation                |
| **Poetry**        | Python dependency and project management        |
| **Vercel**        | Cloud hosting for the Django application        |
| **Railway**       | Cloud hosting for the production MySQL database |
| **Git**           | Version control                                 |
| **GitHub**        | Source code repository                          |

---

# Frontend

The frontend is built using standard web technologies:

* **HTML5**
* **CSS3**
* **JavaScript**
* **Bootstrap 5.3**

Bootstrap is used for responsive layout and utility classes, while custom CSS is used for the application's login page and dashboard interfaces.

The project does **not** use React, Next.js, Vue, or another frontend framework.

The frontend communicates with the Django backend through Django templates, forms, URLs, and server-side views.

---

# Backend

The backend is developed using **Python and Django**.

Django is responsible for:

* URL routing
* User authentication
* Session management
* Database models
* Forms
* Views
* Role-based access
* CSRF protection
* Django Admin
* Application logic
* Duty scheduling functionality
* Report generation

The project separates authentication, dashboard functionality, forms, models, URLs, and scheduling-related services into dedicated modules.

---

# Database

The application uses **MySQL** as its relational database.

## Local Development

During local development, the application can connect to a local MySQL database through environment variables.

Example:

```env
DB_NAME=my_django_db
DB_USER=root
DB_PASSWORD=your-password
DB_HOST=127.0.0.1
DB_PORT=3306
```

## Production Database

The production database is hosted on **Railway**.

The deployed Django application on Vercel connects to the Railway MySQL database using environment variables.

```text
                 Vercel
                   │
                   │ MySQL Connection
                   ▼
             Railway MySQL
                   │
                   ▼
          Production Database
```

The production database contains Django's built-in authentication and session tables together with the application's custom tables.

### Main Database Tables

```text
auth_user
auth_group
auth_permission
auth_user_groups
auth_user_user_permissions

django_admin_log
django_content_type
django_migrations
django_session

core_event
core_eventdutyrecord
core_nfdqueue
core_user
```

The existing application database was migrated to Railway before connecting the deployed Django application.

The database connection was tested to verify that the deployed application could:

* Connect to the production database
* Access existing users
* Access application tables
* Authenticate users
* Read application records
* Write application records

Both the custom web application and Django Admin use the same production database.

---

# Deployment Architecture

The production system uses two primary cloud services:

```text
                         Internet
                            │
                            ▼
                ┌─────────────────────┐
                │       Vercel        │
                │                     │
                │   Django Web App    │
                │                     │
                │ • Login             │
                │ • Dashboard         │
                │ • Employee Mgmt     │
                │ • Scheduling        │
                │ • Events            │
                │ • NFD Queue         │
                │ • Reports           │
                │ • Django Admin      │
                └──────────┬──────────┘
                           │
                           │ MySQL
                           ▼
                ┌─────────────────────┐
                │      Railway        │
                │                     │
                │   MySQL Database    │
                │                     │
                │ • Users             │
                │ • Employees         │
                │ • Events            │
                │ • Duties            │
                │ • NFD Records       │
                └─────────────────────┘
```

## Vercel

**Vercel** hosts the Django web application.

The deployed application provides:

* Login
* User dashboards
* Employee management
* Event management
* Duty scheduling
* NFD queue management
* Report generation
* Django Admin

## Railway

**Railway** hosts the production MySQL database.

The database is maintained separately from the Vercel application.

The Django application connects to Railway using securely configured environment variables.

This architecture separates the application layer from the database layer.

---

# Environment Variables

Sensitive configuration is supplied through environment variables rather than being hardcoded in the source code.

## Local Environment

Example:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=my_django_db
DB_USER=root
DB_PASSWORD=your-password
DB_HOST=127.0.0.1
DB_PORT=3306
```

## Production Environment

The production deployment uses environment variables such as:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=False

DB_NAME=railway
DB_USER=root
DB_PASSWORD=your-railway-password
DB_HOST=your-railway-host
DB_PORT=your-railway-port

CSRF_TRUSTED_ORIGINS=your-trusted-origins
```

Actual production credentials are intentionally excluded from the repository.

> **Security Notice:** Never commit passwords, database credentials, Django secret keys, `.env` files, or other sensitive configuration to GitHub.

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/naimafarooq-dev/duty-scheduling-management-system.git
cd duty-scheduling-management-system
```

## 2. Install Dependencies

This project uses **Poetry** for dependency management.

```bash
poetry install
```

The environment can then be used through:

```bash
poetry run
```

## 3. Configure Environment Variables

Configure the required local environment variables.

Example:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=my_django_db
DB_USER=root
DB_PASSWORD=your-password
DB_HOST=127.0.0.1
DB_PORT=3306
```

## 4. Apply Database Migrations

```bash
poetry run python manage.py migrate
```

## 5. Create a Superuser

```bash
poetry run python manage.py createsuperuser
```

## 6. Run the Development Server

```bash
poetry run python manage.py runserver
```

Application:

```text
http://127.0.0.1:8000/
```

Django Admin:

```text
http://127.0.0.1:8000/admin/
```

---

# Project Structure

```text
duty-scheduling-management-system/
│
├── core/
│   ├── migrations/
│   ├── services/
│   │   └── event_service.py
│   ├── templates/
│   │   └── core/
│   ├── admin.py
│   ├── apps.py
│   ├── decorators.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── views_auth.py
│   └── views_super.py
│
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── static/
│   └── core/
│       └── logo.png
│
├── manage.py
├── pyproject.toml
├── poetry.lock
├── .gitignore
└── README.md
```

---

# Main Application Modules

## Authentication

Responsible for:

* User login
* User logout
* Password authentication
* Session management
* Role-based access

## Employee Management

Responsible for:

* Employee records
* Employee information
* Active employee tracking
* Employee availability for scheduling

## Event Management

Responsible for:

* Event creation
* Event management
* Event retrieval
* Weekend event identification
* Event-based duty scheduling

## Duty Assignment

Responsible for:

* Manual duty assignment
* Automated monthly scheduling
* Duty editing
* Duty deletion
* Event-based assignments

## NFD Queue

Responsible for:

* NFD queue generation
* Employee queue management
* NFD record deletion
* Scheduling-related queue operations

## Reporting

Responsible for:

* Duty report generation
* PDF generation
* Word document generation
* Scheduling record export

---

# Security

The project follows basic application security practices, including:

* Environment-based configuration
* Django authentication
* Role-based access control
* CSRF protection
* Environment-based database credentials
* Sensitive files excluded through `.gitignore`
* Production `DEBUG=False`
* Configured allowed hosts
* Configured CSRF trusted origins

Production deployments should always use:

* A strong Django secret key
* `DEBUG=False`
* Secure database credentials
* Properly configured allowed hosts
* Properly configured CSRF trusted origins

Sensitive credentials should never be stored directly in the source code.

---

# Project Context

This project was developed as a **Duty Scheduling Management System for National Logistics Corporation (NLC)**.

The system demonstrates how an organization can manage:

* Employees
* Events
* Duty assignments
* Monthly schedules
* NFD queues
* Duty records
* Reports
* Administrative data

The project focuses on demonstrating the development of a centralized, database-driven web application for managing an organizational scheduling workflow.

---

# Demonstration Data Disclaimer

> ## Important: Demonstration Data Only
>
> The employee names, HR numbers, employee records, duty assignments, events, NFD records, and other employee-related information included in the demonstration system are **sample data created solely for demonstration and testing purposes**.
>
> **No actual NLC employee database or real NLC employee records have been added to this project.**
>
> The example employees and records are included only to demonstrate how the system works, including:
>
> * Adding and managing employees
> * Creating events
> * Assigning employees to duties
> * Generating monthly schedules
> * Managing the NFD queue
> * Viewing duty records
> * Generating reports
> * Demonstrating Django Admin functionality
>
> The sample data **does not represent official NLC employee records, operational records, or confidential organizational information**.
>
> This project should therefore **not be considered an official NLC employee database or a representation of actual NLC personnel records**.

---

# Data Privacy

No real employee passwords, database passwords, Django secret keys, or other sensitive authentication credentials are intentionally included in the public GitHub repository.

Sensitive organizational information should always be handled securely and should not be committed to source control.

The demonstration data is used only to illustrate the functionality and workflow of the application.

---

# Project Purpose

The primary purpose of this project is to demonstrate the development and deployment of a complete **Django-based organizational duty scheduling system**.

The project combines:

* Web application development
* User authentication
* Role-based access control
* Employee management
* Event management
* Manual duty scheduling
* Automated monthly scheduling
* NFD queue management
* MySQL database integration
* PDF reporting
* Word document generation
* Django Admin
* Cloud application deployment
* Cloud database deployment

The project demonstrates how a manual scheduling workflow can be transformed into a centralized, database-driven web application.

---

## Live Application

### Web Application

 https://duty-scheduling-management-system-h6x4iu6kl.vercel.app

### Django Admin

(https://duty-scheduling-management-system-h6x4iu6kl.vercel.app/admin/login/?next=%2Fadmin%2F)

> The web application and Django Admin use the same production MySQL database hosted on Railway.

---

# Deployment

The application is deployed using:

* **Vercel** for the Django web application
* **Railway** for the production MySQL database

The architecture separates the web application from the database while allowing both the custom dashboard and Django Admin to operate on the same production data.

---

# License

This project was developed as a software engineering project to demonstrate web application development, database integration, authentication, scheduling, reporting, and cloud deployment using Django.

The project is provided for educational and demonstration purposes.
