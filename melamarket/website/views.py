from flask import Blueprint

views= Blueprint('views', __name__)

@views.route('/explore')
def explore():
    return "<h1>Explore Page</h1>"


@views.route('/your-posts')
def yourposts():
    return "<h1>Your Posts</h1>"
