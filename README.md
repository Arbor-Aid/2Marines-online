# Arbor-Aid

Python version 3.10

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
2. Navigate to the backend directory:

   ```bash
   cd path/to/backend
   ```
3. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install Django and other dependencies:

   ```bash
   pip install -r requirements.txt
   ```
5. Run Django migrations to set up your database:

   ```bash
   python manage.py migrate
   ```
6. Start the Django development server:

   ```bash
   python manage.py runserver
   ```
