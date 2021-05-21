import datetime
# import random
# import string
from flask import Flask     # request
import csv
from faker import Faker

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/hello")
def hello():
    return "<p>Hello!!!</p>"


@app.route("/now")
def now():
    return str(datetime.datetime.now())


"""
@app.route("/random")
def get_random():
    # print(request.args)
    # print(request.args["var"])
    length = int(request.args["length"])
    return "".join(random.choices(string.ascii_lowercase, k=length))
"""


# Reading CSV file function
@app.route("/avr_data")
def avr_data():
    height_lst, weight_lst = [], []
    with open("hw.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            height_lst.append(float(row[' "Height(Inches)"']))
            weight_lst.append(float(row[' "Weight(Pounds)"']))
    height_avr = sum(height_lst) / len(height_lst)
    weight_avr = sum(weight_lst) / len(weight_lst)
    return "Average height = {}, average weight = {}".format(round(height_avr, 5), round(weight_avr, 5))


# Reading requirements.txt file function
@app.route("/requirements")
def requirements():
    txt_file = open("D:/Python/PycharmProjects/python_hillel_advanced/requirements.txt", "r")
    file_content = txt_file.read()
    txt_file.close()
    return file_content


# Reading random_students file function
@app.route("/random_students")
def random_students():
    fake_students = Faker(["uk_UA"])
    return "".join(fake_students.name() + ". " for _ in range(10))


app.run(debug=True, port=5001)
