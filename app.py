import json
import traceback
import os

from process_edu_input import process_input
from flask import Flask, request, render_template, g

app = Flask(__name__)

global edu_tree


@app.before_first_request
def before_first_request():
    global edu_tree
    print("Loading JSON Outline Deutschland")
    filename = os.path.join(app.root_path, 'decision_tree_edu.json')
    if filename:
        with open(filename, 'r', encoding="UTF-8") as f:
            edu_tree = json.load(f)


@app.route('/edu/', methods=['GET', 'POST'])
def edu_form():
    return render_template("edu_form.html")


@app.route('/result_edu/', methods=['GET', 'POST'])
def edu_result():
    global edu_tree
    request_dict = {}
    try:
        request_dict = dict(request.form)
    except Exception:
        print(Exception)

    answer = process_input(edu_tree, request_dict)

    return render_template("result.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4200)
