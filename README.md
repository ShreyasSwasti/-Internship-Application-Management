# 💼 Internship Application Management System

A web-based Internship Application Management System built using **Python Flask and MySQL**. The application is designed to simplify the internship recruitment process by allowing applicants to register, apply for internships, and track their applications while HR managers manage internship opportunities and applications.

## 🚀 Project Overview

The Internship Application Management System aims to provide a centralized platform for managing internship recruitment.

The project is being developed incrementally, with a focus on backend development, database management, authentication, security, and user-friendly interfaces.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web framework |
| MySQL | Database management |
| PyMySQL | Database connectivity |
| HTML5 | Frontend structure |
| CSS3 | Styling |
| Werkzeug | Password hashing and security |
| Git & GitHub | Version control |

## ✨ Features

### Implemented Features

- Flask application setup.
- MySQL database connectivity.
- Applicant registration.
- User login and logout.
- Session management.
- Role-based authentication.
- Separate Applicant and HR dashboards.
- Password hashing using Werkzeug.
- Password verification during login.
- Input validation for registration and login.
- Custom 404 error page.

### Planned Features

- Internship posting and management.
- Applicants can browse available internships.
- Online internship application submission.
- Resume upload functionality.
- Application status tracking.
- HR application review system.
- Accept or reject internship applications.
- Administrator dashboard.
- User management.
- Improved security and validation.
- Responsive user interface.

## 📁 Project Structure

```text
Internship-Application-Management/
│
├── controllers/
│   ├── auth_controller.py
│   ├── db_controller.py
│   ├── applicant_controller.py
│   └── hr_controller.py
│
├── models/
│   └── user_model.py
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── applicant_dashboard.html
│   ├── hr_dashboard.html
│   └── 404.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

*Note: The folder structure may change as development continues.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ShreyasSwasti/-Internship-Application-Management.git
```

### 2. Navigate to the Project Directory

```bash
cd -Internship-Application-Management
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure MySQL Database

Create a MySQL database:

```sql
CREATE DATABASE internship_db;
```

Configure your database credentials using environment variables. Do not upload database passwords or secret keys to GitHub.

### 6. Run the Application

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5001
```

## 🔐 Security

Security improvements being implemented include:

- Password hashing using Werkzeug's `generate_password_hash()`.
- Password verification using `check_password_hash()`.
- Parameterized SQL queries.
- Input validation.
- Session management.
- Role-based access control.

## 🎯 Project Goals

The main goal of this project is to develop a practical internship recruitment platform while improving my understanding of:

- Python Flask development.
- Backend application architecture.
- Relational database management.
- Authentication and authorization.
- Web application security.
- Real-world software development practices.

## 👨‍💻 Developer

**Shreyas Swasti**

- GitHub: [@ShreyasSwasti](https://github.com/ShreyasSwasti)

## 📌 Project Status

**Currently under development.**

New features, improvements, and security enhancements are being added progressively.

---

⭐ If you find this project interesting, feel free to explore the repository and share suggestions!
