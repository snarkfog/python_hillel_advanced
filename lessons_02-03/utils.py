import datetime
import random
import string
import requests
from flask import render_template


# Homework 3. Generate random password function
def generate_password(length, special, digits):
    gen_pass = string.ascii_letters
    if special:
        gen_pass += string.punctuation
    if digits:
        gen_pass += string.digits
    html_password = "".join(random.choices(gen_pass, k=length))
    return render_template("gen_pass.html", password=html_password)


# Homework 3. Bitcoin rate function
def bitcoin_request(currency):
    r = requests.get("https://bitpay.com/api/rates")
    for key in r.json():
        if key["code"] == currency:
            return render_template("bitcoin_rate.html", name=key["name"], code=key["rate"], rate=currency)


def get_current_time():
    return datetime.datetime.now()
