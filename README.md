# Project Directory Structure
```
.
├── README.md
├── Success status.png
└── alx_travel_app
    ├── README.md
    ├── alx_travel_app
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-312.pyc
    │   │   ├── celery.cpython-312.pyc
    │   │   ├── settings.cpython-312.pyc
    │   │   ├── urls.cpython-312.pyc
    │   │   └── wsgi.cpython-312.pyc
    │   ├── asgi.py
    │   ├── celery.py
    │   ├── requirement.txt
    │   ├── requirements.txt
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── db.sqlite3
    ├── docker-compose.yaml
    ├── listings
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-312.pyc
    │   │   ├── admin.cpython-312.pyc
    │   │   ├── apps.cpython-312.pyc
    │   │   ├── models.cpython-312.pyc
    │   │   ├── serializers.cpython-312.pyc
    │   │   ├── signals.cpython-312.pyc
    │   │   ├── tasks.cpython-312.pyc
    │   │   ├── urls.cpython-312.pyc
    │   │   └── views.cpython-312.pyc
    │   ├── admin.py
    │   ├── apps.py
    │   ├── management
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   └── __init__.cpython-312.pyc
    │   │   └── commands
    │   │       ├── __init__.py
    │   │       ├── __pycache__
    │   │       │   ├── __init__.cpython-312.pyc
    │   │       │   ├── celery_worker.cpython-312.pyc
    │   │       │   └── seed.cpython-312.pyc
    │   │       ├── celery_worker.py
    │   │       └── seed.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_remove_booking_total_price.py
    │   │   ├── 0003_alter_payment_status.py
    │   │   ├── 0004_alter_payment_amount.py
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       ├── 0001_initial.cpython-312.pyc
    │   │       ├── 0002_remove_booking_total_price.cpython-312.pyc
    │   │       ├── 0003_alter_payment_status.cpython-312.pyc
    │   │       ├── 0004_alter_payment_amount.cpython-312.pyc
    │   │       └── __init__.cpython-312.pyc
    │   ├── models.py
    │   ├── serializers.py
    │   ├── signals.py
    │   ├── tasks.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── manage.py
    └── requirements.txt
```

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