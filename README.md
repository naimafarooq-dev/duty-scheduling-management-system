# Duty Scheduling Management System

A web-based **Duty Scheduling Management System** built with Django to simplify employee management, event-based duty assignment, scheduling, and reporting.

The system is designed to help organizations manage employees and their assigned duties through a centralized dashboard, reducing manual scheduling work and improving organization of duty records.

## Features

* **User Authentication**

  * Secure login and logout
  * Role-based access
  * User account management

* **Employee Management**

  * Add and manage employees
  * Maintain employee information
  * Track active employees

* **Duty Scheduling**

  * Assign duties to employees
  * Manage event-based duty assignments
  * View and organize duty schedules
  * Support for automated monthly duty scheduling

* **Event Management**

  * Create and manage events
  * Associate employees with events and duties
  * Identify weekend events

* **NFD Queue Management**

  * Maintain the NFD queue
  * Manage employees according to scheduling requirements

* **Dashboard**

  * Centralized management dashboard
  * Overview of employees, events, and duties
  * Easy navigation between scheduling functions

* **Reports**

  * Generate duty reports
  * Export scheduling information
  * PDF-based reporting support

* **Django Admin**

  * Administrative interface for managing system data
  * Database and user management through Django Admin

## Technology Stack

| Technology   | Purpose                      |
| ------------ | ---------------------------- |
| Python       | Backend programming          |
| Django       | Web framework                |
| MySQL        | Database                     |
| HTML5        | Frontend structure           |
| CSS          | Interface styling            |
| JavaScript   | Frontend functionality       |
| ReportLab    | PDF report generation        |
| Poetry       | Python dependency management |
| Git & GitHub | Version control              |

## Project Structure

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

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/naimafarooq-dev/duty-scheduling-management-system.git
cd duty-scheduling-management-system
```

### 2. Install Dependencies

This project uses **Poetry** for dependency management.

```bash
poetry install
```

Activate the Poetry environment:

```bash
poetry shell
```

Alternatively, commands can be executed directly with:

```bash
poetry run
```

### 3. Configure Environment Variables

Create a `.env` file or configure environment variables for your local environment.

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

> Never commit passwords, secret keys, database credentials, or `.env` files to GitHub.

### 4. Apply Migrations

```bash
poetry run python manage.py migrate
```

### 5. Create a Superuser

```bash
poetry run python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
poetry run python manage.py runserver
```

Open the application at:

```text
http://127.0.0.1:8000/
```

## Database

The application uses **MySQL** as its database backend.

For local development, configure the database through environment variables rather than hardcoding credentials in the Django settings.

For production deployments, use a managed MySQL service and configure the corresponding environment variables securely.

## Main Modules

### Authentication

Handles user login, logout, authentication, and access control.

### Employee Management

Provides functionality for maintaining employee records and their active status.

### Event Management

Handles events that require employee duty assignments.

### Duty Assignment

Provides scheduling functionality for assigning employees to specific duties and events.

### Reporting

Generates reports containing duty and scheduling information.

## Security

The project follows basic security practices including:

* Environment-based configuration for sensitive settings
* Django authentication
* Role-based access control
* CSRF protection provided by Django
* Sensitive files excluded through `.gitignore`

**Production deployments should always use a strong secret key, `DEBUG=False`, secure database credentials, and properly configured allowed hosts and trusted origins.**

## Deployment

The project is structured for deployment using a cloud-hosted MySQL database and a Python-compatible web hosting platform.

Production configuration should be supplied through environment variables rather than committed to the repository.

