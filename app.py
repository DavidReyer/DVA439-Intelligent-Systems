import json
import os

from flask import Flask, render_template

app = Flask(__name__)

global edu_tree


@app.before_first_request
def before_first_request():
    global edu_tree
    filename = os.path.join(app.root_path, 'decision_tree_edu.json')
    if filename:
        with open(filename, 'r', encoding="UTF-8") as f:
            edu_tree = json.load(f)


@app.route('/edu/', methods=['GET', 'POST'])
def edu_form():
    return render_template("edu_form.html", edu_tree=edu_tree)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4200)
