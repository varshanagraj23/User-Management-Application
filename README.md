User Management System
Project Overview
The User Management System is a web-based application built using Django that allows users to create, read, update, and delete (CRUD) user details. The system includes data validation, form handling, and a user-friendly interface enhanced with custom CSS.

Features
CRUD Operations:
Add new users (First Name, Last Name, Phone Number, Email, Address)
View a list of users
Edit user details
Delete users
Data Validation:
Validates phone numbers (minimum 10 digits)
Ensures valid email format
User-Friendly Interface:
Clean and responsive design using custom CSS
Error messages for invalid input
Built-in Navigation:
Easily navigate between user list, add user, and edit user pages
Technologies Used
Backend:
Python (Django Framework)
SQLite (Default Django database)
Frontend:
HTML5
CSS3 (Custom styling)
Django Template Engine
Project Setup
Prerequisites
To run the project, you need to have the following installed:

Python (version 3.x)
Django (version 4.x or higher)
Installation Steps
Clone the Repository: Clone this repository to your local machine:

bash
Copy code
git clone <repository-url>
Navigate to the Project Directory:

bash
Copy code
cd user-management
Create a Virtual Environment: It's recommended to create a virtual environment for the project:

bash
Copy code
python -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate
Install the Required Dependencies: Install the required packages listed in requirements.txt:

bash
Copy code
pip install -r requirements.txt
Migrate the Database: Run the following commands to set up the database:

bash
Copy code
python manage.py migrate
Start the Development Server: Start the Django development server by running:

bash
Copy code
python manage.py runserver
Access the Application: Open your web browser and visit:

arduino
Copy code
http://127.0.0.1:8000/users/
Usage Instructions
Add New User:

Navigate to the "Add New User" page by clicking the button on the user list page.
Fill out the form with the following details:
First Name
Last Name
Phone Number (Minimum 10 digits)
Email (Unique and valid format)
Address
Submit the form to add the user to the database.
View Users:

The user list page displays all stored users.
Each user entry has options to edit or delete the user.
Edit User:

Click on the "Edit" link next to any user to modify their details.
Submit the updated information to save changes.
Delete User:

Click on the "Delete" link next to any user.
Confirm the deletion to remove the user from the system.
Folder Structure
bash
Copy code
user-management/
│
├── users/
│   ├── migrations/         # Database migrations
│   ├── static/
│   │   └── users/          # Static files (CSS, images)
│   ├── templates/
│   │   └── users/          # HTML templates for CRUD operations
│   ├── admin.py            # Admin site configuration
│   ├── apps.py             # App configuration
│   ├── forms.py            # Django forms for user input
│   ├── models.py           # Database models (UserDetail)
│   ├── urls.py             # URL routing for the app
│   ├── views.py            # Views handling the logic for CRUD operations
│
├── manage.py               # Django project management script
├── db.sqlite3              # SQLite database
├── requirements.txt        # List of Python dependencies
└── README.md               # Project README file
Further Enhancements
Authentication: Add user login/logout to protect certain operations (e.g., only authenticated users can create or delete records).
Pagination: Implement pagination to handle large user datasets more efficiently.
Search Functionality: Add a search bar to filter users based on their details.
