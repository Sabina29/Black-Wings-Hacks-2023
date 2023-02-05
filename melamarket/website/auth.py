from flask import Blueprint

auth= Blueprint('auth', __name__)

@auth.route('/explore')
def explore():
    return "<p>Your Feed</p>"

@auth.route('/your-posts')
def yourPosts():
    return "<p>Your Posts</p>"