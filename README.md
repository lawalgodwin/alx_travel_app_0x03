# Project Directory Structure
├── README.md # Project description ├── Success status.png # Success status image └── alx_travel_app # Main project folder ├── README.md # App-specific README ├── alx_travel_app # Project-specific settings and configurations │ ├── init.py # Marks this directory as a Python package │ ├── pycache # Python bytecode cache │ │ ├── init.cpython-312.pyc │ │ ├── celery.cpython-312.pyc │ │ ├── settings.cpython-312.pyc │ │ ├── urls.cpython-312.pyc │ │ └── wsgi.cpython-312.pyc │ ├── asgi.py # ASGI application configuration │ ├── celery.py # Celery configuration │ ├── requirement.txt # Old requirements file (might be deprecated) │ ├── requirements.txt # Dependencies file │ ├── settings.py # Project settings │ ├── urls.py # URL routing │ └── wsgi.py # WSGI application configuration ├── db.sqlite3 # SQLite database file ├── docker-compose.yaml # Docker configuration file ├── listings # Listings app │ ├── init.py # Marks this directory as a Python package │ ├── pycache # Python bytecode cache │ │ ├── init.cpython-312.pyc │ │ ├── admin.cpython-312.pyc │ │ ├── apps.cpython-312.pyc │ │ ├── models.cpython-312.pyc │ │ ├── serializers.cpython-312.pyc │ │ ├── signals.cpython-312.pyc │ │ ├── tasks.cpython-312.pyc │ │ ├── urls.cpython-312.pyc │ │ └── views.cpython-312.pyc │ ├── admin.py # Admin configurations for Listings │ ├── apps.py # App configuration │ ├── management # Custom management commands │ │ ├── init.py │ │ ├── pycache # Python bytecode cache │ │ │ └── init.cpython-312.pyc │ │ └── commands # Custom commands │ │ ├── init.py │ │ ├── pycache │ │ │ ├── init.cpython-312.pyc │ │ │ ├── celery_worker.cpython-312.pyc │ │ │ └── seed.cpython-312.pyc │ │ ├── celery_worker.py │ │ └── seed.py │ ├── migrations # Database migration files │ │ ├── 0001_initial.py │ │ ├── 0002_remove_booking_total_price.py │ │ ├── 0003_alter_payment_status.py │ │ ├── 0004_alter_payment_amount.py │ │ ├── init.py │ │ └── pycache # Python bytecode cache for migrations │ │ ├── 0001_initial.cpython-312.pyc │ │ ├── 0002_remove_booking_total_price.cpython-312.pyc │ │ ├── 0003_alter_payment_status.cpython-312.pyc │ │ ├── 0004_alter_payment_amount.cpython-312.pyc │ │ └── init.cpython-312.pyc │ ├── models.py # Models for Listings │ ├── serializers.py # Serializer classes for Listings │ ├── signals.py # Signals for Listings app │ ├── tasks.py # Celery tasks │ ├── tests.py # Tests for Listings app │ ├── urls.py # URL routing for Listings │ └── views.py # Views for Listings ├── manage.py # Django management script └── requirements.txt # Main dependencies file

## Prerequisites

- Python 3.x
- Redis running on port *6379*
- Docker (optional for containerization)

## Getting Started
    ```bash
        # create aand activate a virtual environment
        python3 -m venv venv && source venv/bin/activate
    ```
    ```bash
        # clone the repo and cd into the repo
        git clone https://github.com/lawalgodwin/alx_travel_app_0x03.git && cd alx_travel_app_0x03
    ```
    ```bash
        # Navigate into the project Directory
        cd alx_travel_app && pip install -r requirements.txt && ./manage.py makemigrations && ./manage.py migrate
    ```
## How to run the project
    ```bash
        # in the same project directory, run the command below to start the api
        ./manage.py runserver 0.0.0.0:8000
    ```
## start the background worker
    ```bash
        # in the same project directory but from another terminer, start the celery worker
        watchfiles --filter python 'celery -A alx_travel_app worker -l info'
    ```
    ```bash
        # in the same project directory but from another terminer, start flower(GUI for monitoring celery workers and background tasks)
        celery -A alx_travel_app flower --port=55555
    ```

## Accessing the app

- The api is accessible on the host on port *8000*
- Celery flower runs on the host on port *55555*