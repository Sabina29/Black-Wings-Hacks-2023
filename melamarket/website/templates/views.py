from flask import Blueprint

views= Blueprint('views', __name__)

@views.route('/explore')
def explore():
    return "<h1>Test</h1>"

