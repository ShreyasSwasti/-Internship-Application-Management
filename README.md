# Internship Application Management System

A Flask-based web application for managing internship applications, applicant registration, authentication, and role-based access for Applicants and HR Managers.

## 📌 Project Overview

The **Internship Application Management System** is a web-based application developed using **Python Flask and MySQL**.

The system is being developed incrementally through multiple tasks. The current implementation provides:

* Applicant registration
* MySQL database integration
* User authentication
* Session management
* Role-based access control
* Applicant dashboard
* HR Manager dashboard
* Protected routes
* Logout functionality

The project is designed to provide a structured foundation for managing internship applications and users.

---

## 🚀 Features

### Task 1 – Project Setup

* Flask application setup
* Project folder structure
* Flask Blueprints
* HTML templates
* Static files
* MySQL configuration
* Environment variable configuration

### Task 2 – Database Integration

* MySQL database connection
* Flask-SQLAlchemy integration
* Database helper functions
* Fetch operations
* Insert operations
* Update operations
* Delete operations
* Database connection testing

### Task 3 – Applicant Registration

* Applicant registration form
* Name, email, password and qualification fields
* Email validation
* Password validation
* Duplicate email handling
* Applicant data stored in MySQL
* Default `Applicant` role assignment

### Task 4 – Authentication & Role-Based Access

* User login
* Email and password verification
* Flask session management
* Applicant dashboard
* HR Manager dashboard
* Role-based redirection
* Protected dashboard routes
* Logout functionality
* Login page styling

---

## 🛠️ Technologies Used

| Technology       | Purpose                   |
| ---------------- | ------------------------- |
| Python           | Backend programming       |
| Flask            | Web application framework |
| Flask-SQLAlchemy | Database ORM              |
| SQLAlchemy       | Database interaction      |
| PyMySQL          | MySQL connectivity        |
| MySQL            | Relational database       |
| HTML             | Web page structure        |
| CSS              | Web page styling          |
| Jinja2           | Template rendering        |
| python-dotenv    | Environment configuration |
| Git              | Version control           |
| GitHub           | Source code management    |

---

## 📂 Project Structure

```text
Internship-Application-Management/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
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

---

## 🔐 Authentication Flow

The current authentication process follows this flow:

```text
                    User
                      │
                      ▼
                    Login
                      │
                      ▼
          Validate Email & Password
                      │
                      ▼
             Create Flask Session
                      │
                      ▼
                Check User Role
                 ┌────┴────┐
                 │         │
                 ▼         ▼
             Applicant   HR Manager
                 │         │
                 ▼         ▼
          Applicant     HR Dashboard
          Dashboard
```

---

## 👥 User Roles

### 👤 Applicant

Applicants can:

* Register a new account
* Login using their credentials
* Access the Applicant Dashboard
* Maintain an authenticated session
* Logout

### 👨‍💼 HR Manager

HR Managers can:

* Login using their credentials
* Access the HR Dashboard
* Maintain an authenticated session
* Logout

### 🔒 Role-Based Protection

The application checks the user's role before allowing access to protected dashboards.

An Applicant cannot directly access the HR Manager dashboard without the required HR Manager role.

---

## 🗄️ Database

The application currently uses a MySQL database named:

```text
internship_db
```

### Users Table

The `users` table contains the following fields:

| Field           | Description             |
| --------------- | ----------------------- |
| `id`            | Unique user ID          |
| `name`          | User's name             |
| `email`         | Unique email address    |
| `password`      | User password           |
| `qualification` | Applicant qualification |
| `role`          | User role               |

Example roles:

```text
Applicant
HR Manager
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

### 2. Open the Project Directory

```bash
cd Internship-Application-Management
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Database

Create the MySQL database:

```sql
CREATE DATABASE internship_db;
```

Configure the required database credentials in the `.env` file.

Example:

```text
DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=internship_db
```

> ⚠️ Do not commit the `.env` file to GitHub because it may contain database credentials.

### 5. Run the Application

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5001
```

---

## 🧪 Testing

The following functionality has been tested during development:

* ✅ Applicant registration
* ✅ Applicant data storage
* ✅ Duplicate email validation
* ✅ Applicant login
* ✅ Applicant dashboard
* ✅ HR Manager login
* ✅ HR Manager dashboard
* ✅ Role-based redirection
* ✅ Protected dashboard routes
* ✅ Logout functionality
* ✅ MySQL database connectivity

---

## 📈 Development Progress

| Task                                        | Status      |
| ------------------------------------------- | ----------- |
| Task 1 – Project Setup                      | ✅ Completed |
| Task 2 – Database Integration               | ✅ Completed |
| Task 3 – Applicant Registration             | ✅ Completed |
| Task 4 – Authentication & Role-Based Access | ✅ Completed |
| Task 5 – Internship/Application Management  | ⏳ Pending   |

---

## 🔮 Future Improvements

Planned improvements include:

* Password hashing
* Forgot password functionality
* Password reset
* CSRF protection
* Improved session security
* Login rate limiting
* Internship management
* Internship application submission
* Application status tracking
* HR application management
* Applicant profile management
* Improved dashboard UI
* Admin functionality

---

## 👨‍💻 Development

This project is being developed as part of an internship project using **Python, Flask, MySQL, HTML, CSS and related web technologies**.

The application is being developed incrementally, with each task adding new functionality to the system.

---

### 📌 Current Version

**Task 4 – Authentication & Role-Based Access Completed**
 working on it 
 
