# Web-based To-Do List Application

Simple To-Do List application built with **Flask**, **SQLite** and **Bootstrap**.
Supports adding tasks, marking them as complete, and deleting tasks. Designed as a **sample project** for DevOps / Linux SysAdmin purposes.

---

## Features

- Add new tasks
- List all tasks
- Mark tasks as complete ✅
- Delete tasks ❌
- Web-based interface with Bootstrap styling
- SQLite database (easy to migrate to other DBs)
- Dockerized for easy deployment
- Unit tests with pytest

---

## Tech Stack

- **Backend**: Python 3, Flask, SQLAlchemy
- **Frontend**: HTML, CSS, Jinja2 Templates, Bootstrap
- **Database**: SQLite
- **Containerization**: Docker
- **Testing**: Pytest

## Project Structure
```
todo-app/
|── app.py  # Flask application entry point
|── models.py   # Database models
|── routes.py   # Route definitions
|── requirements.py
|── templates/
|   |── base.html
|   └── index.html
|── static/
|   └── style.css
└──tests/
    └── test_app.py
```

## Installation & Running Locally

1. Clone the repo
```
git clone https://github.com/nauximus/todo-app.git
cd todo-app
```
2. Create a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```
3. Install dependencies:
```
pip instal -r requirements.txt
```
4. Run the app:
```
python app.py
```
5. Open http://127.0.0.1:5000 in your browser.

---

## Docker Usage
1. Build Docker image:
```
docker build -t todo-app .
```
2. Run container:
```
docker un -p 5000:5000 todo-app
```

## Screenshots
~

## CI/CD Pipeline
- GitHub Actions workflow run tests on every push.
- Docker image is automatically built and pushed to DockerHub
- Ready for deployment to any Docker-compatible environment.

## License
