import flask
from flask import Flask
import datetime

app = Flask(__name__)


@app.route('/')
def get_subject():
    subject = ""
    cur_date = datetime.datetime.today()
    start = datetime.datetime(2021, 11, 14)

    with open("static/timetable.csv", "r") as f:
        j = (cur_date - start).days
        for i in range(j):
            f.readline()

        line = f.readline().split(",")[1]
        if "No revision" in line:
            subject = "Nothing"
        else:
            subject = line


    return flask.render_template("index.html", date = cur_date.strftime("%e/%m/%Y"), subject = subject)


if __name__ == '__main__':
    app.run()