import os

from flask import Flask, redirect, session, render_template, request, jsonify
# from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.exceptions import Unauthorized
# AUTH_KEY = "username"

app = Flask(__name__)

# toolbar = DebugToolbarExtension(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
#     "DATABASE_URL", "postgresql:///flask_notes")
# app.config['SQLALCHEMY_ECHO'] = True
# app.config['SECRET_KEY'] = "i-have-a-secret"
# connect_db(app)
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True


#TODO: update requirements with flask
@app.post('/upload')
def view_upload():
    """Show and handle form"""
    file = request.files
    breakpoint()

    return jsonify("index.html")

@app.get('/')
def view_home():
    """Show and handle form"""


    return render_template("index.html")
