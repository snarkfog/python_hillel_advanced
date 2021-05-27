# import datetime
# import random
# import string
import string
from flask import Flask, jsonify  # request, Response
import csv
from faker import Faker
from webargs.flaskparser import use_kwargs
from webargs import fields, validate
from utils import generate_password, get_current_time, bitcoin_request

app = Flask(__name__)


@app.errorhandler(422)
@app.errorhandler(400)
def handle_error(err):
    headers = err.data.get("headers", None)
    messages = err.data.get("messages", ["Invalid request."])
    if headers:
        return jsonify({"errors": messages}), err.code, headers
    else:
        return jsonify({"errors": messages}), err.code


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/hello")
def hello():
    return "<p>Hello!!!</p>"


@app.route("/now")
def now():
    return str(get_current_time())


# Homework 3. Generate random password function
@app.route("/random")
@use_kwargs({
    "length": fields.Int(
        required=False,
        missing=10,
        validate=[validate.Range(min=1, max=100)]
    ),
    "specials": fields.Int(
        required=False,
        missing=0,
        validate=[validate.Range(min=0, max=1)]
    ),
    "digits": fields.Int(
        required=False,
        missing=0,
        validate=[validate.Range(min=0, max=1)]
    )
},
    location="query"
)
def get_random(length, specials, digits):
    return generate_password(length, specials, digits)


# Homework 3. Bitcoin rate function
@app.route("/bitcoin_rate")
@use_kwargs({
    "currency": fields.Str(
        required=False,
        missing="USD",
        validate=[validate.ContainsOnly(string.ascii_uppercase)]
    )
},
    location="query"
)
def get_bitcoin_rate(currency):
    return bitcoin_request(currency)


# Homework 2. Reading CSV file function
@app.route("/avr_data")
def avr_data():
    height_lst, weight_lst = [], []
    with open("hw.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            height_lst.append(float(row[' "Height(Inches)"']))
            weight_lst.append(float(row[' "Weight(Pounds)"']))
    height_avr = sum(height_lst) / len(height_lst)
    weight_avr = sum(weight_lst) / len(weight_lst)
    return "Average height = {}, average weight = {}".format(round(height_avr, 5), round(weight_avr, 5))


# Homework 2. Reading requirements.txt file function
@app.route("/requirements")
def requirements():
    with open("D:/Python/PycharmProjects/python_hillel_advanced/requirements.txt", "r") as txt_file:
        file_content = txt_file.read()
    return file_content


# Homework 2. Reading random_students file function
@app.route("/random_students")
def random_students():
    fake_students = Faker(["uk_UA"])
    return "".join(fake_students.name() + ". " for _ in range(10))


app.run(debug=True, port=5001)
