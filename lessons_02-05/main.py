import string
from flask import Flask, jsonify
import csv
from faker import Faker
from webargs.flaskparser import use_kwargs
from webargs import fields, validate
from utils import generate_password, get_current_time, bitcoin_request
from db import execute_query
from html_formatters import format_records

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


# Homework 2. Reading requirements.txt file function (update)
@app.route("/requirements")
def requirements():
    with open("../requirements.txt", "r") as txt_file:
        file_content = txt_file.read()
    return file_content


# Homework 2. Reading random_students file function (update)
@app.route("/random_students")
def random_students():
    fake_students = Faker(["uk_UA"])
    return ". ".join(fake_students.name() for _ in range(10))


# Homework 4. Unique Names SQL Function
@app.route("/unique_names")
def unique_names():
    query = f"select * from Customers group by FirstName"
    records = execute_query(query)
    return "Quantity of unique names: {}".format(len(records))


# Homework 4. Tracks SQL Function
@app.route("/tracks_count")
def get_tracks_count():
    query = f"select * from Tracks"
    records = execute_query(query)
    return "Quantity of records from the table Tracks: {}".format(len(records))


# Homework 4. Customers Function
@app.route("/customers")
@use_kwargs({
    "city": fields.Str(
        required=False,
    ),
    "country": fields.Str(
        required=False,
    )
},
    location="query"
)
def get_customers(country=None, city=None):
    if country and city:
        query = f"select * from Customers where Country = '{country}' AND City = '{city}'"
    elif country or city:
        query = f"select * from Customers where Country = '{country}' OR City = '{city}'"
    else:
        query = f"select * from Customers"
    records = execute_query(query)
    return format_records(records)


# Homework 4. Sales Function
@app.route("/sales")
def get_sales():
    sales = 0
    query = f"select * from Invoice_Items"
    records = execute_query(query)
    for column in records:
        sales += column[3] * column[4]
    return "Sales amount: {}".format(round(sales, 2))


app.run(debug=True, port=5001)
