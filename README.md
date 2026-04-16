# contact-management-python
Contact Management System using Python
📇 Contact Management System (Python + SQL Workbench)
A simple yet powerful Contact Management System built using Python and MySQL (SQL Workbench).
This project allows users to Add, Update, Delete, and Search contacts with fields for Name, Phone, and Email.

🚀 Features
➕ Add Contact – Save new contacts with name, phone, and email.

✏️ Update Contact – Modify existing contact details.

❌ Delete Contact – Remove unwanted contacts from the database.

🔍 Search Contact – Find contacts quickly by name, phone, or email.

🗄️ Database Integration – Uses MySQL Workbench for persistent storage.

🛠️ Tech Stack
Python 3.x

MySQL / SQL Workbench

mysql-connector-python (for database connectivity)

📂 Project Structure
Code
contact-management-system/
│── main.py              # Entry point of the application
│── db_config.py         # Database connection setup
│── contact_manager.py   # Core logic for add, update, delete, search
│── requirements.txt     # Dependencies
│── README.md            # Project documentation
⚙️ Setup Instructions
Clone the repository

bash
git clone https://github.com/your-username/contact-management-system.git
cd contact-management-system
Install dependencies

bash
pip install -r requirements.txt
Configure Database

Open SQL Workbench.

Create a database:

sql
CREATE DATABASE contacts_db;
Create a table:

sql
USE contacts_db;

CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    email VARCHAR(100) NOT NULL
);
Update db_config.py with your MySQL credentials:

python
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "your_password",
    "database": "contacts_db"
}
Run the application

bash
python main.py
🖥️ Example Usage
text
1. Add Contact
   Enter Name: John Doe
   Enter Phone: 9876543210
   Enter Email: john@example.com

2. Search Contact
   Enter Name: John Doe
   Result: John Doe | 9876543210 | john@example.com


