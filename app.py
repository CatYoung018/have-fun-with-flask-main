from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Heya! I’m going to crush Flask! #SkillcrushingIt."

# Run the flask server
if __name__ == "__main__":
    app.run()