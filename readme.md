IAM Role Management System (RBAC)

 📌 Project Description

This project implements an Identity and Access Management (IAM) system using Role-Based Access Control (RBAC).  
Users are authenticated using a username and password, and access to different pages is granted based on their assigned roles such as admin and user.

The system ensures that roles are verified before loading protected pages, which is a core concept used in real-world enterprise security systems.

This project demonstrates a complete frontend + backend + database workflow.

---

 🛠 Tools Used

- Programming Language: Python  
- Backend Framework: Flask  
- Frontend: HTML, CSS  
- Database:MySQL  
- Database Connector:mysql-connector-python  
- Version Control: Git & GitHub  
- IDE: Visual Studio Code  

---

▶️ How to Run the Project

 1️⃣ Clone or Download the Repository

```bash
git clone https://github.com/your-username/hh8-minor-project-2.git
Or download the ZIP file and extract it.

2️⃣ Project Folder Structure
hh8-minor-project-2
│
├── app.py
├── database.sql
├── requirements.txt
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   └── admin.html
│
└── static/
    └── style.css
3️⃣ Create Database and Tables
Open MySQL Command Line or MySQL Workbench and run:

SOURCE path_to_project/database.sql;
This will:

Create the database iam_rbac

Create tables for users, roles, and user-role mapping

Insert sample roles and users

4️⃣ Install Required Python Libraries
Open terminal inside the project folder and run:

pip install -r requirements.txt
5️⃣ Update Database Credentials
Open app.py and update your MySQL password:

password="YOUR_MYSQL_PASSWORD"
6️⃣ Run the Application
python app.py
You should see:

Running on http://127.0.0.1:5000/
7️⃣ Open the Application in Browser
Open any browser and go to:

http://127.0.0.1:5000
🔑 Sample Login Credentials
Username	Password	Role
admin1	1234	Admin
user1	1234	User
Admin users can access the Admin Panel

Normal users will be denied access to admin-only pages

🎯 What I Learned
-Basics of Identity and Access Management (IAM)

-Implementing Role-Based Access Control (RBAC)

-Connecting Flask with MySQL

-Secure authentication and authorization

-Restricting access to pages based on user roles

-Structuring a full-stack web application

-Understanding real-world access control systems

