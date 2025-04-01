# File Manager Backend API

This repository contains the backend API for a secure and efficient file management web application. Built with Django REST Framework, this API provides a robust foundation for users to store, organize, and manage their files online. It prioritizes security, scalability, and ease of integration with frontend applications.

## Key Features

- **Secure User Authentication:**
  - User registration and login functionalities.
  - JWT (JSON Web Token) based authentication for secure API access.
- **Comprehensive File Management:**
  - Effortless file uploading with type validation.
  - Listing and retrieval of user-specific files.
  - Secure file deletion.
- **User Storage Tracking:**
  - Monitors and manages storage space used by each user.
  - Automatic updates to user storage upon file operations.
- **File Metadata Management:**
  - Stores essential file information such as filename, size, upload timestamp, and file type.
- **Dashboard Analytics:**
  - Provides a dashboard API endpoint offering insights into user file activity:
    - Total files uploaded.
    - Total storage utilized.
    - Recent file uploads.
    - File type distribution.
- **RESTful API Design:**
  - Clean and well-documented API endpoints using Django REST Framework.
  - JSON request/response format for easy integration.
- **Robust Validation:**
  - File type validation to ensure only allowed file types are uploaded.
  - Password validation during user registration.

## Tech Stack

- **Backend Framework:** [Django](https://www.djangoproject.com/) - A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **API Framework:** [Django REST Framework](https://www.django-rest-framework.org/) - A powerful and flexible toolkit for building Web APIs.
- **Authentication:** [Django REST Framework Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) - JSON Web Token authentication for REST APIs.
- **Database:** [PostgreSQL](https://www.postgresql.org/) - A powerful, open-source relational database system known for its reliability and features.
- **Python Version:** 3.12+

## Project Structure

```
filemanager-backend/
├── filemanager/                 # Main Django Project Directory
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py               # Project-wide settings
│   ├── urls.py                   # Main URL routing
│   └── wsgi.py
│
├── accounts/                     # User Authentication App
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                 # Custom User Model
│   ├── serializers.py            # User Serializers
│   ├── urls.py                   # Authentication URL routes
│   └── views.py                  # Authentication Views
│
├── files/                        # File Management App
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                 # File Model
│   ├── serializers.py            # File Serializers
│   ├── urls.py                   # File-related URL routes
│   └── views.py                  # File Management Views
│
├── media/                        # User uploaded files
│   ├── profile_pics/             # Profile pictures for users
│   └── user_files/               # Files uploaded by users
│
├── requirements.txt              # Project Dependencies
├── manage.py                     # Django Management Script
├── .env                          # Environment Variables (for sensitive configurations)
```

- **`filemanager/`**: Core Django project settings, URL configurations, and WSGI/ASGI setup.
- **`accounts/`**: Django app responsible for user authentication, registration, and profile management. Contains models, serializers, and views related to user accounts.
- **`files/`**: Django app handling file management functionalities – uploading, listing, deleting files, and providing dashboard analytics.
- **`media/`**: Default directory for storing user-uploaded media files. Organized into `profile_pics` and `user_files`.
- **`requirements.txt`**: Lists Python package dependencies required to run the project.
- **`manage.py`**: Django's command-line utility for administrative tasks.
- **`.env`**: Stores environment-specific variables (like database credentials, secret keys) – **ensure this file is not committed to version control!**

## Setup Instructions

To run this project locally, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/lokeshkarra/filehub-server.git
    cd filehub-server
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Database:**

    ```bash
    # Create PostgreSQL Database
    psql -U postgres
    CREATE DATABASE filemanager;
    CREATE USER filemanageruser WITH PASSWORD 'your_secure_password';
    GRANT ALL PRIVILEGES ON DATABASE filemanager TO filemanageruser;
    ```

5.  **Set up environment variables:**

    - Create a `.env` file in the root directory of the project.
    - Add the following environment variables to your `.env` file, replacing the placeholders with your actual values:

      ```env
      DJANGO_SECRET_KEY=your_secret_key_here
      DJANGO_DEBUG=True  # Set to False in production
      DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

      DB_NAME=filemanager_db
      DB_USER=your_db_user
      DB_PASSWORD=your_db_password
      DB_HOST=localhost
      DB_PORT=5432
      ```

    - **Note:** For production, ensure `DJANGO_DEBUG=False` and use a strong, unique `DJANGO_SECRET_KEY`. Securely manage your database credentials.

6.  - Ensure you have PostgreSQL installed and running.
    - Create a PostgreSQL database with the name specified in your `.env` file (`DB_NAME`).

7.  **Run migrations:**

    ```bash
    python manage.py makemigrations accounts
    python manage.py makemigrations files
    python manage.py migrate
    ```

8.  **Create a superuser (admin account):**

    ```bash
    python manage.py createsuperuser
    ```

9.  **Start the development server:**

    ```bash
    python manage.py runserver
    ```

    The API will be accessible at `http://localhost:8000/api/`.

## API Endpoints

Here are the main API endpoints:

- **Authentication:**

  - `POST /api/auth/register/`: User registration.
  - `POST /api/auth/login/`: User login (returns JWT access and refresh tokens).
  - `GET /api/auth/profile/`: Get user profile (requires authentication).
  - `PUT /api/auth/profile/`: Update user profile (requires authentication).

- **Files:**

  - `POST /api/files/`: Upload a new file (requires authentication, `multipart/form-data`).
  - `GET /api/files/`: List all files for the authenticated user (requires authentication).
  - `GET /api/files/{id}/`: Retrieve details of a specific file (requires authentication).
  - `DELETE /api/files/{id}/`: Delete a specific file (requires authentication).
  - `GET /api/files/dashboard/`: Get file dashboard statistics (requires authentication).
  - `GET /api/files/{id}/download/`: Download a specific file (requires authentication).

- **API Documentation:**
  - `/api/schema/swagger-ui/`: Swagger UI for API documentation (automatically generated).
  - `/api/schema/redoc/`: ReDoc for API documentation (automatically generated).

## Running Tests

To run the backend tests:

```bash
python manage.py test
```

Ensure all tests pass to confirm the API is functioning as expected.

## Contributing

Contributions are welcome! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Implement your changes and write tests.
4.  Ensure all tests pass.
5.  Submit a pull request with a clear description of your changes.

## License

[Apache 2.0](https://github.com/lokeshkarra/filehub-server?tab=Apache-2.0-1-ov-file)

## Contact

**Lokeshwar Reddy Karra**  
📧 [Email](mailto:lokeshwarreddy.karra@gmail.com)

---
