import os
from utils import upload_file
from PIL import Image
from PIL.ExifTags import TAGS, Base, GPS


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
#
@app.post('/upload')
def view_upload():
    """Show and handle form
    # process exif data and send to db
    # delete temp file on server after
    """
    file = request.files['file']
    keyword = request.form
    file_name = f"./tmp/{keyword['keyword1']}.jpg"
    file.save(file_name, 100)
    upload_file(file_name, 'r33-pixly')
    im = Image.open(file_name)
    exif = im.getexif()

    # for k, v in exif.items():
    #     print("Tag", Base(k).name, "Value", v)

    GPSTAGS = {i.value: i.name for i in GPS}
    print(GPSTAGS)

    return jsonify("nice pic")

@app.get('/')
def view_home():
    """Show and handle form"""


    return render_template("index.html")
