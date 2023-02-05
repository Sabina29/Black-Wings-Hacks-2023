from flask import Blueprint

auth= Blueprint('auth', __name__)

@auth.route("/explore")

def explore():
    pass