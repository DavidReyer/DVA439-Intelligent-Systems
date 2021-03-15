import json
import os

from flask import Flask, render_template

app = Flask(__name__)

edu_tree = {}
edu_dataset_link = '../decision_tree_edu.json'

gpa_tree = {}
gpa_dataset_link = '../decision_tree.json'


def before_first_request(dataset_link):
    filename = os.path.join(app.root_path, dataset_link)
    if filename:
        with open(filename, 'r', encoding="UTF-8") as f:
            tree = json.load(f)
            return tree


@app.before_first_request
def edu_tree_request():
    global edu_tree
    edu_tree = before_first_request(edu_dataset_link)


@app.before_first_request
def gpa_tree_request():
    global gpa_tree
    gpa_tree = before_first_request(gpa_dataset_link)


@app.route('/gpa/', methods=['GET', 'POST'])
def gpa_form():
    return render_template("edu_form.html", edu_tree=gpa_tree, title='GPA')


@app.route('/edu/', methods=['GET', 'POST'])
def edu_form():
    return render_template("edu_form.html", edu_tree=edu_tree, title='Course')


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4200)
