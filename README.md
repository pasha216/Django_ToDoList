# Django ToDoList

Django ToDoList is a simple and effective todo list web application built with Django. It helps you manage, update, and organize your daily tasks from an intuitive web interface.

---

## Features

- Add, edit, and delete tasks
- Mark tasks as completed or pending
- Simple, clean interface
- Persistent storage using SQLite (default)

---

## Demo

Try the app live here:  
[https://django-todolist-bjxt.onrender.com](https://django-todolist-bjxt.onrender.com)

---

## Getting Started

### Prerequisites

- Python 3.8 or later
- pip (Python package manager)
- (Optional) Virtual environment tool (`venv`, `virtualenv`)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/M-Alhbyb/Django_ToDoList.git
   cd Django_ToDoList
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

5. Visit `http://127.0.0.1:8000/` in your browser.

---

## Project Structure

```
.
├── todolist/        # Main application code
├── db.sqlite3       # SQLite database for development
├── manage.py        # Django management script
├── requirements.txt # Python dependency list
├── Procfile         # For deploying (e.g. on Heroku/Render)
├── runtime.txt      # Python runtime version (for deployment)
├── LICENSE          # GPL-2.0 License
└── README.md
```

---

## License

This project is licensed under the GNU General Public License v2.0. See the [LICENSE](LICENSE) file for details.

---

**Author:** [M-Alhbyb](https://github.com/M-Alhbyb)
