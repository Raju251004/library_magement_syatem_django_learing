# Library Management System

A simple library website made with Django. You can view books on the website and manage book records from the Django admin page.

## What you need

- Windows
- Python 3.10 or later
- Git

## 1. Download the project

Open PowerShell and run:

```powershell
git clone https://github.com/Raju251004/library_magement_syatem_django_learing.git
cd library_magement_syatem_django_learing
```

## 2. Create and activate a virtual environment

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell does not allow activation, run this command once in the same PowerShell window, then activate the environment again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## 3. Install the required packages

```powershell
python -m pip install -r requirements.txt
```

## 4. Set up the environment file

Copy the example file:

```powershell
Copy-Item .env.example .env
```

Open `.env` in Notepad:

```powershell
notepad .env
```

For local use, keep `DJANGO_DEBUG=True` and `DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost`. Replace the `DJANGO_SECRET_KEY` example value with a random secret key. To generate one, run:

```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the printed key into `.env` after `DJANGO_SECRET_KEY=`. Do not share or commit your `.env` file.

## 5. Set up the database

```powershell
python manage.py migrate
```

This project uses SQLite, so Django creates the database file for you.

## 6. Start the website

```powershell
python manage.py runserver
```

Open these links in your browser:

- Books page: <http://127.0.0.1:8000/home/>
- Admin page: <http://127.0.0.1:8000/admin/>

To stop the server, press `Ctrl+C` in PowerShell.

## Optional: create an admin login

To add or edit books through the admin page, create an admin account:

```powershell
python manage.py createsuperuser
```

Follow the prompts, then sign in at <http://127.0.0.1:8000/admin/>.
