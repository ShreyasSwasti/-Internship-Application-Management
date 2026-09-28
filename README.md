# Internship Application Management System

A Flask-based web application for managing internship applications, user registration, authentication, and role-based access for Applicants and HR Managers.

## 📌 Project Overview

The Internship Application Management System is developed using Python Flask and MySQL.

The project is being developed incrementally through multiple tasks. The current implementation includes applicant registration, database integration, user authentication, session management, and role-based dashboards.

## 🚀 Features

### Task 1 – Project Setup

* Flask application setup
* Project folder structure
* Flask Blueprints
* HTML templates
* Static files
* MySQL database configuration

### Task 2 – Database Integration

* MySQL database connection
* Flask-SQLAlchemy integration
* Database helper functions
* Fetch, insert, update and delete operations
* Database connection testing

### Task 3 – Applicant Registration

* Applicant registration form
* Name, email, password and qualification fields
* Email validation
* Password validation
* Duplicate email handling
* Applicant data stored in MySQL
* Default user role set to `Applicant`

### Task 4 – Authentication and Role-Based Access

* Login functionality
* Email and password verification
* Flask session management
* Applicant dashboard
* HR Manager dashboard
* Role-based redirection
* Protected dashboard routes
* Logout functionality
* Login page styling

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **Flask-SQLAlchemy**
* **SQLAlchemy**
* **PyMySQL**
* **MySQL**
* **HTML**
* **CSS**
* **Jinja2**
* **python-dotenv**
* **Git & GitHub**

## 📂 Project Structure

```text
Internship-Application-Management/
│
├── app.py
├── requirements.txt
├── README.md
│
├── controllers/
│   ├── auth_controller.py
│   ├── applicant_controller.py
│   ├── hr_controller.py
│   ├── db_controller.py
│   └── main_controller.py
│
├── models/
│   ├── __init__.py
│   ├── user_model.py
│   └── db_helpers.py
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── hr_dashboard.html
│   └── internships.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── database/
    └── schema.sql
```

## 🔐 Authentication Flow

The current authentication flow works as follows:

```text
User
  ↓
Login
  ↓
Validate Email & Password
  ↓
Create Flask Session
  ↓
Check User Role
  ↓
 ┌──────────────────┐
 │                  │
Applicant        HR Manager
 │                  │
 ↓                  ↓
Applicant        HR Dashboard
Dashboard
```

## 👥 User Roles

### Applicant

Applicants can:

* Register an account
* Login
* Access the Applicant Dashboard
* Logout

### HR Manager

HR Managers can:

* Login
* Access the HR Dashboard
* Logout

The application uses role-based access checks to prevent Applicants from directly accessing the HR dashboard.

## 🗄️ Database

The project uses a MySQL database named:

```text
internship_db
```

The `users` table currently contains fields including:

```text
id
name
email
password
qualification
role
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project directory

```bash
cd Internship-Application-Management
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and configure the required database settings.

> Do not upload the `.env` file to GitHub because it may contain sensitive credentials.

### 5. Run the Flask application

```bash
python app.py
```

The application runs on:

```text
http://localhost:5001
```

## 🧪 Current Testing

The following functionality has been tested:

* Applicant registration
* Database storage
* Applicant login
* Applicant dashboard
* HR Manager login
* HR Manager dashboard
* Role-based redirection
* Logout
* Protected dashboard access

## 📈 Development Progress

| Task                                        | Status      |
| ------------------------------------------- | ----------- |
| Task 1 – Project Setup                      | ✅ Completed |
| Task 2 – Database Integration               | ✅ Completed |
| Task 3 – Applicant Registration             | ✅ Completed |
| Task 4 – Authentication & Role-Based Access | ✅ Completed |
| Task 5                                      | ⏳ Pending   |

## 🔮 Future Improvements

Possible future improvements include:

* Password hashing
* Forgot password and password reset
* CSRF protection
* Stronger session security
* Login rate limiting
* Internship management
* Application submission and tracking
* HR application management
* Improved dashboard UI

## 👨‍💻 Development

This project is being developed as part of an internship project using Flask, MySQL and related web technologies.

---

**Current Version:** Task 4 Completed
