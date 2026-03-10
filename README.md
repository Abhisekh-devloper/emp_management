🚀 Smart Employee Management System with Workforce Productivity Analytics

A Smart Employee Management System built using Python Django Framework with PostgreSQL as the database.
This web application helps organizations efficiently manage employees, track attendance, assign work, and analyze workforce productivity.
The system provides separate dashboards for Admin and Employees, making management and communication easier inside the organization.

🧠 Project Overview

The Smart Employee Management System is designed to simplify HR operations and employee workflow management. It allows administrators to manage employee data, publish notices, track attendance, and monitor work assignments while enabling employees to view tasks, submit requests, and stay updated with organizational information.

This project demonstrates the implementation of:
Django Web Framework
PostgreSQL Database
User Authentication System
Admin & Employee Role Management
Attendance & Task Tracking
Workforce Productivity Analytics

✨ Key Features
🔐 Authentication System
Admin Login
Employee Login
Employee Registration
Secure Authentication System

👨‍💼 Admin Features

Add Employees
Manage Employee Records
Publish Notices
Manage Attendance
Monitor Employee Work Assignments
View Employee Requests
Workforce Productivity Overview

👩‍💻 Employee Features

View Assigned Work
Submit Requests
View Notices
Track Attendance
Manage Work Updates

🛠️ Tech Stack
Technology	Usage
Python	Backend Programming
Django	Web Framework
PostgreSQL	Database
HTML	Structure
CSS / Tailwind / Bootstrap	UI Design
JavaScript	Interactivity

⚙️ Installation Guide

Follow these steps to run the project locally.

1️⃣ Install Python

Download and install Python from:

https://www.python.org/downloads/

2️⃣ Install Django
pip install django
3️⃣ Install Pipenv (Virtual Environment)
pip install pipenv
4️⃣ Clone the Repository
git clone https://github.com/Abhisekh-devloper/emp_management.git
5️⃣ Navigate to Project Directory
cd emp_management
6️⃣ Activate Virtual Environment
pipenv shell
7️⃣ Configure PostgreSQL Database

Update the database credentials in:

settings.py

Example:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
8️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate
9️⃣ Start the Development Server
python manage.py runserver
🎉 Open in Browser
http://127.0.0.1:8000/

Your project will now be running.

📷 Project Screenshots

🔑 Login
![Login](https://github.com/Abhisekh-devloper/emp_management/blob/main/screenshots/Login.png?raw=true "Login")

📝 Signup
![Signup](https://github.com/Abhisekh-devloper/emp_management/blob/main/screenshots/signup.png?raw=true "Signup")

📊 Dashboard
![Dashboard](https://github.com/Abhisekh-devloper/emp_management/blob/main/screenshots/Dashboard.png "Dashboard")

🧾 Assign Work
![Assign Work](https://github.com/Abhisekh-devloper/emp_management/blob/main/screenshots/assign_work.png?raw=true "Assign Work")

📢 Notice
![Notice](https://github.com/Abhisekh-devloper/emp_management/blob/main/screenshots/Notice.png?raw=true "Notice")

📩 Request
![Request](https://github.com/Abhisekh-devloper/emp_management/blob/main/screenshots/Make%20Request.png?raw=true "Request")

⚙️ Admin Dashboard
![Admin (Manage Employee)](https://github.com/Abhisekh-devloper/emp_management/blob/main/screenshots/admin%20dashboard.png?raw=true "Admin (Manage Employee)")


📊 Future Improvements

Employee Performance Analytics
Productivity Graphs
Task Deadline Tracking
Email Notification System
REST API Integration
Mobile Responsive Dashboard
Role-Based Access Control

🤝 Contributing

Contributions are welcome!

If you would like to improve this project:

Fork the repository
Create a new branch
Commit your changes
Submit a Pull Request


👨‍💻 Developer

Abhisekh Mohanty
🎓 B.Tech – Computer Science & Engineering

GitHub:
https://github.com/Abhisekh-devloper