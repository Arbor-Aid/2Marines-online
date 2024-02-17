# Arbor-Aid




Python version 3.10

For the Python/Django Backend

1. **Django**: The core framework for your backend.

   - `django`
2. **Requests**: Used for making HTTP requests to external APIs, like the GPT API.

   - `requests`
3. **Python-dotenv**: To manage your environment variables securely, particularly for loading the GPT API key from a `.env` file.

   - `python-dotenv`
4. **Djangorestframework** (optional): If you're planning to build RESTful APIs with Django.

   - `djangorestframework`

### General Python Packages

- **Flask** (if considering an alternative to Django for any microservice or lightweight API needs)
  - `flask`

### For Handling Database Connections

- If you're using SQLite (comes with Django), no additional package is needed.
- For other databases (e.g., PostgreSQL, MySQL), you may need:
  - `psycopg2` (for PostgreSQL)
  - `mysqlclient` or `PyMySQL` (for MySQL)

### Development Tools

- **Pip** for package management (comes with Python).
- **Venv** for creating virtual environments (comes with Python 3.3 and later).

### For the Flutter Frontend

Since Flutter dependencies are managed differently (through the `pubspec.yaml` file rather than a `requirements.txt` file or similar), here's a reminder of a tool you might use:

- **flutter_dotenv**: For managing environment variables in Flutter, if you choose to pass environment variables such as API keys into your Flutter app.
  - This would be included in your `pubspec.yaml` under dependencies as:
    ```yaml
    flutter_dotenv: ^5.0.2
    ```

### Installation Commands

For the Python/Django backend, after setting up your virtual environment, you can install these dependencies using `pip`. For example:

```bash
pip install django requests python-dotenv djangorestframework
```

If you opt to use PostgreSQL or MySQL, remember to install the appropriate database adapter as well:

```bash
pip install psycopg2  # For PostgreSQL
# or
pip install mysqlclient  # For MySQL
```

For the Flutter frontend, you add your dependencies to `pubspec.yaml` and run:

```bash
flutter pub get
```

This setup should cover the basics of what you've mentioned for your project. If there are any more specific libraries or tools you find yourself needing as you progress, you'll be able to add them similarly.

Getting Started

These instructions will get your copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- Flutter (for frontend development)
- Python 3 and Django (for backend development)
- Any other dependency your project needs

### Installing

A step-by-step series of commands that tell you how to get a development environment running.

#### Frontend

1. Install Flutter:

   For macOS:

   ```bash
   brew install --cask flutter
   ```

   For other operating systems, please refer to the [official Flutter installation guide](https://flutter.dev/docs/get-started/install).
2. Navigate to the frontend directory:

   ```bash
   cd path/to/frontend
   ```
3. Get Flutter dependencies:

   ```bash
   flutter pub get
   ```
4. Run the Flutter app (make sure an emulator is running or a device is connected):

   ```bash
   flutter run
   ```

#### Backend

1. Ensure Python 3 is installed on your system. You can download it from [python.org](https://www.python.org/downloads/) or install it using your operating system's package manager.
2. Install django depends

```bash
    pip install django djangorestframework
```

3. Navigate to the backend directory:

   ```bash
   cd path/to/backend
   ```
4. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
5. Install Django and other dependencies:

   ```bash
   pip install -r requirements.txt
   ```
6. Run Django migrations to set up your database:

   ```bash
   python manage.py migrate
   ```
7. Start the Django development server:

   ```bash
   python manage.py runserver
   ```
