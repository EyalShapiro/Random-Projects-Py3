# Learn English Server

This is a Django-based project for managing and serving content related to learning English.

## Features

- User authentication and management
- Content types management
- Static files handling
- Database migrations and management
- Administrative tasks via `manage.py`

## Requirements

- Python 3.x
- Django 4.x or higher
- Virtual environment (recommended)

## Installation

1. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Make sure the [`requirements.txt`](./requirements.txt) file is located in the root directory of the project. You can find it [here](./requirements.txt).

3. Apply migrations:
   ```bash
   python manage.py migrate
   ```

## Usage

To start the development server:

```bash
python manage.py runserver
```

To create a superuser for the admin panel:

```bash
python manage.py createsuperuser
```

## Available Commands

Run `python manage.py help` to see all available commands.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
