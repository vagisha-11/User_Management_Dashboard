
# User Management Dashboard

Welcome to the User Management Dashboard project! This project is designed to manage user data through a web dashboard using Django.






## Features and Usage

1. User Model:

  -  Created a Django model named "User" with fields such as     Name, Username, and Email.

2. Display User Data:

- Fetches user data from the admin database and displays it in a table on the dashboard.

3. Add User:

- Click the "Add User" button to open a modal for new user input.
- Fill out the form and submit to add the user to the database which would in turn automatically update the backend database with new user data .

4. Edit & Delete Functionality:

- Use the "Edit" button to open a modal with pre-filled user data for editing.
- Make changes and save to update the user record.
- Use the "Delete" button to remove a user from the database.
- Save changes to update the corresponding user record in the backend database.

5. Admin Database Consistency:
- Ensures changes made through the dashboard are reflected in the admin database.
## Technologies Used



Django (Backend Framework)

HTML/CSS (Frontend)

JavaScript (For modal and form handling)
## Run Locally


1. Clone the repository:


2. Install dependencies using 'pip install -r requirements.txt'

3. Run migrations using 'python manage.py migrate'

4. Start the development server using 'python manage.py runserver'
## Authors

- [Vagisha Shrivastava](https://github.com/vagisha-11)

