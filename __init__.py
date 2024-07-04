from flask import Flask, render_template
from logging import FileHandler,WARNING
import requests

app = Flask(__name__, template_folder="templates")

file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects/<string:id>")
def get_projects(id):
    projects_url = "https://api.npoint.io/fcf6645a3b174e443338"
    response = requests.get(projects_url)
    all_projects = response.json()
    for proj in all_projects:
        if proj["id"] == int(id):
            project = proj
            break
    return render_template("projects.html", project=project)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)