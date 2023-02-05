from flask import render_template, session, request, redirect, url_for
from webpage import app, db

@app.route('/')
def home():
    return "This is the homepage"