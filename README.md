````markdown
# Django Project Setup & Commands

This guide will help you set up and run your Django project in a local development environment.

---

## 🧱 Project Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-django-project.git
cd your-django-project
````

### 2. Create and Activate Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate it (Linux/macOS)
source venv/bin/activate

# Activate it (Windows)
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run Commands

### Start the Development Server

```bash
python manage.py runserver
# or specify a port
python manage.py runserver 8080
```

### Make Migrations

```bash
python manage.py makemigrations
```

### Apply Migrations

```bash
python manage.py migrate
```

### Create a Superuser

```bash
python manage.py createsuperuser
```

### Open Django Shell

```bash
python manage.py shell
```

### Run Tests

```bash
python manage.py test
```

### Collect Static Files (for production)

```bash
python manage.py collectstatic
```

### Check for Common Issues

```bash
python manage.py check
```

---

## 🔒 Deactivate Virtual Environment

```bash
deactivate
```

---

## 🛠 Notes

* Be sure to configure your `.env` file (if using environment variables).
* Static/media root settings may need to be configured for production.

---

```
