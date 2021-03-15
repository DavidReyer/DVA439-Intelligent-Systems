import json

from flask import Flask, request, render_template, g

app = Flask(__name__)


@app.route('/edu/', methods=['GET', 'POST'])
def request():
    return render_template("edu_form.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4200)
