# Internship Application Management System

A web-based application built using Python Flask and MySQL to manage internship applications and provide separate access for Applicants and HR Managers.

## 📌 Project Overview

The Internship Application Management System is developed to simplify the process of managing internship applications. It allows applicants to register and log in, while HR Managers can access a separate dashboard to manage application-related activities.

This project is being developed step by step as part of my internship, with new features added as each task is completed.

## 🚀 Features

- **User Registration:** Allows new applicants to create an account.
- **User Authentication:** Verifies user credentials during login.
- **Database Integration:** Connects the application to a MySQL database.
- **Role-Based Access:** Supports separate roles for Applicants and HR Managers.
- **Session Management:** Maintains user login sessions.
- **Applicant Dashboard:** Provides an interface for applicants.
- **HR Dashboard:** Provides a separate interface for HR Managers.
- **Custom Error Page:** Displays a custom 404 page for unavailable routes.
- **Modular Code Structure:** Organizes the application into controllers, templates, and static files.

*Note: Features are being implemented incrementally, so the available functionality may change as development continues.*

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Backend Framework:** Flask
- **Database:** MySQL
- **Database Driver:** PyMySQL
- **ORM / Database Library:** Flask-SQLAlchemy (installed; usage depends on the current implementation)
- **Environment Variables:** python-dotenv
- **Frontend:** HTML, CSS
- **Version Control:** Git and GitHub

## 📂 Project Structure

```text
Internship-Application-Management/
│
├── app.py
├── .env
├── requirements.txt
│
├── controllers/
│   ├── applicant_controller.py
│   ├── hr_controller.py
│   └── db_controller.py
│
├── templates/
│   ├── login.html
│   ├── applicant_dashboard.html
│   └── hr_dashboard.html
│
├── static/
│   └── css/
│       └── login.css
│
└── README.md
```

*The structure above is a general example. Keep only the files and folders that actually exist in your repository.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ShreyasSwasti/-Internship-Application-Management.git
```

### 2. Navigate to the Project Folder

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
python -m pip install -r requirements.txt
```

### 5. Configure the Database

- Install and start MySQL.
- Create a database named `internship_db`.
- Configure your database connection details using environment variables in the `.env` file.

Example configuration:

```env
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=internship_db
```

Use the variable names expected by your existing database controller. Do not upload real database passwords or other secrets to GitHub.

### 6. Run the Application

```bash
python app.py
```

Open the application in your browser at:

```text
http://127.0.0.1:5001
```

The port may differ depending on your application configuration.

## 🗄️ Database

The project uses MySQL to store user information and support authentication.

The database is named `internship_db`. Database operations are handled through the application's database controller and related modules.

## 🔒 Security Considerations

- Store database credentials in environment variables.
- Keep the `.env` file out of version control.
- Validate user input before processing it.
- Use secure password hashing rather than storing plain-text passwords.
- Apply role-based authorization to protect applicant and HR routes.

## 📈 Development Progress

The project is being developed incrementally. Current work includes:

- Flask application setup
- Database connectivity
- User registration and authentication
- Session handling
- Role-based dashboards
- Custom error handling
- Ongoing improvements to applicant and HR functionality

## 🎯 Future Improvements

- Internship application submission and tracking
- HR application review and status updates
- Search and filter functionality
- Improved form validation and error handling
- Enhanced dashboard UI
- Automated testing and deployment

## 👨‍💻 Author

**Shreyas Swasti**

- GitHub: [ShreyasSwasti](https://github.com/ShreyasSwasti)

---

This project is developed as part of my internship to gain practical experience in Python web development, database integration, authentication, and version control.
