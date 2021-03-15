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
        request_dict['gender'] = request.form['gender']
        request_dict['NationalITy'] = request.form['NationalITy']
        request_dict['PlaceofBirth'] = request.form['PlaceofBirth']
        request_dict['StageID'] = request.form['StageID']
        request_dict['GradeID'] = request.form['GradeID']
        request_dict['SectionID'] = request.form['SectionID']
        request_dict['Semester'] = request.form['Semester']
        request_dict['Relation'] = request.form['Relation']
        request_dict['raisedhands'] = request.form['raisedhands']
        request_dict['VisITedResources'] = request.form['VisITedResources']
        request_dict['AnnouncementsView'] = request.form['AnnouncementsView']
        request_dict['Discussion'] = request.form['Discussion']
        request_dict['ParentAnsweringSurvey'] = request.form['ParentAnsweringSurvey']
        request_dict['ParentschoolSatisfaction'] = request.form['ParentschoolSatisfaction']
        request_dict['StudentAbsenceDays'] = request.form['StudentAbsenceDays']
    except Exception:
        print(Exception)

    process_input(edu_tree, request_dict)

    return render_template("edu_form.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4200)
