# 🎉 Have Fun with Flask

A beginner-friendly introduction to Flask web development. This project demonstrates the absolute basics of creating a Flask application, setting up routes, and running a development server.

![Languages](https://img.shields.io/badge/Python-100.0%25-yellow)

## 📋 Project Overview

This is a foundational Flask project designed to introduce the core concepts of Flask web development. Perfect for beginners starting their journey with Python web frameworks, this project covers the essential setup and basic routing.

### Key Features

- **Minimal Flask Setup**: Simple, clean Flask application structure
- **Basic Routing**: Introduction to Flask decorators and routes
- **Development Server**: Using Flask's built-in server
- **Foundation Skills**: Building blocks for more complex applications

## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **Framework**: Flask 3.x

## 📚 Learning Outcomes

This project demonstrates:

- Installing Flask and setting up a Python environment
- Creating a basic Flask application
- Understanding Flask routing with `@app.route()`
- Running Flask's development server
- Working with virtual environments
- Basic Flask application structure

## 🚀 Installation & Setup

### Prerequisites

Check if Python is installed:

**On Mac:**
```bash
python3 --version
```

**On Windows:**
```bash
python --version
```

Ensure you have Python 3.8 or higher installed (3.11 recommended). If you need to install Python on Windows, see [this guide](https://docs.google.com/document/d/14diNu_g6uhouBscRt8zIezolANTRQA6HobKRP4Lgu5Q/copy).

### Step 1: Clone the Repository

```bash
git clone https://github.com/CatYoung018/have-fun-with-flask-main.git
cd have-fun-with-flask-main
```

### Step 2: Create Virtual Environment

**On Mac:**
```bash
python3 -m venv venv
```

**On Windows:**
```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment

**On Mac:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
source venv/Scripts/activate
```

Once activated, you'll see `(venv)` at the beginning of your terminal prompt.

### Step 4: Install Flask

```bash
pip install flask
```

### Step 5: Run the Application

**Without debugger:**
```bash
flask run
```

**With debugger (recommended for development):**
```bash
flask run --debug
```

The app will run at: `http://127.0.0.1:5000/`

### Step 6: View the App

Open your browser and navigate to `http://127.0.0.1:5000/` to see your Flask application in action!

### Stopping the Application

- Press `Ctrl + C` to stop the server
- Run `deactivate` to close the virtual environment

**Note:** When not using the debugger, you'll need to stop and restart the server after making code changes. Remember to hard refresh your browser (`Ctrl + F5` or `Cmd + Shift + R`).

## 📁 Project Structure

```
have-fun-with-flask-main/
├── app.py              # Main Flask application
├── .gitignore          # Git ignore file
├── README.md           # Project documentation
└── venv/               # Virtual environment (after setup)
```

## 🎯 Basic Flask Concepts

### 1. Creating a Flask App
```python
from flask import Flask

app = Flask(__name__)
```

### 2. Defining Routes
```python
@app.route('/')
def home():
    return "Hello, Flask!"
```

### 3. Running the App
```python
if __name__ == '__main__':
    app.run(debug=True)
```

### Example Route Structure
```python
@app.route('/')
def index():
    return "Welcome to Flask!"

@app.route('/about')
def about():
    return "About Page"

@app.route('/user/<name>')
def user(name):
    return f"Hello, {name}!"
```

## 💡 Usage

1. **Start the server**: Run `flask run --debug`
2. **View in browser**: Open `http://127.0.0.1:5000/`
3. **Experiment**: Try adding new routes in `app.py`
4. **See changes**: With debugger on, changes appear automatically after saving

## 🔄 What's Next?

After mastering this basic Flask setup, you can:
1. Add HTML templates with Jinja2
2. Create static files (CSS, JavaScript, images)
3. Work with forms and user input
4. Integrate databases with SQLAlchemy
5. Build full-stack applications

**Recommended Next Projects:**
- Add templates folder and render HTML
- Create a multi-page Flask site
- Integrate an API
- Build a database-driven application

## 🎓 Acknowledgments

This project was created as part of a Skillcrush coding bootcamp, introducing Flask web development from the ground up.

## 📚 Resources

- [Flask Official Documentation](https://flask.palletsprojects.com/)
- [Flask Quickstart Guide](https://flask.palletsprojects.com/en/3.0.x/quickstart/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

## 📝 License

This project is open source and available for educational purposes.

## 📧 Contact

**Cat Young**  
Email: cat@catyoungconsulting.com  
Portfolio: [catyoung018.github.io/Cat-Young-Dev](https://catyoung018.github.io/Cat-Young-Dev/)  
GitHub: [@CatYoung018](https://github.com/CatYoung018)

---

⭐ **If you found this project helpful, please consider giving it a star!**
