# Job Application Form Web App

This web application is built using Django and HTML. It allows users to fill out a job application form and submit their details. Upon submission, the app sends a confirmation email to the user and stores the data in an SQL database.

## Features

- **Job Application Form**: Users can fill out a form with their first name, last name, email, start date, and current occupation.
- **Email Confirmation**: Upon form submission, the app sends a congratulatory email to the user using Django's email functionality.
- **Data Storage**: User data is stored in an SQL database managed by Django.
- **Success Message**: After submission, users receive a success message on the web page.
- **Admin Interface**: Admins can log in at `/admin/` to view, edit, delete, and search user data. Admins can also filter data by date and occupation.
- **Navigation Bar**: The app includes an About page and a Contact page. Users can send messages via the Contact page, which also uses Django to send emails.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, Bootstrap, Jinja2
- **Database**: SQL (managed by Django)
- **Email**: Django's `django.core.mail` library

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   
2. Navigate to the project directory:
   ```bash
   cd job-application-form
   
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   
4. Run the Django development server:
   ```bash
   python manage.py runserver

## Usage
1. Open your web browser and go to http://localhost:8000/.
2. Fill out the job application form and submit it.
3. Check your email for a confirmation message.
4. Admins can log in at http://localhost:8000/admin/ to manage user data.
5. You can also go to http://localhost:8000/contact/ to contact us with sending an email.

## Admin Interface
- **URL**: `/admin/`
- **Features**:
  - View, edit, and delete user data.
  - Search user data by first name and email address.
  - Filter user data by date and occupation.

## Navigation
- **About Page**: Contains information about the app.
- **Contact Page**: Users can send messages via email.

## Dependencies
- python
- Django
- Bootstrap
- Jinja2

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For any inquiries, please contact us via the Contact page on the app.

Feel free to customize this `README.md` file further to suit your needs! If you have any other questions or need additional help, just let me know. 😊