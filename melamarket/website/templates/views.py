from flask import Blueprint

views= Blueprint('views', __name__)

@views.route('/')
def explore():
    return "<h1>Explore Page</h1>"

