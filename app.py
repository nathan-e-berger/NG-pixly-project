from utils import upload_file
# import os
# from PIL import Image
# from PIL.ExifTags import TAGS, Base, GPS
# from models import db, connect_db, Image


# from flask import Flask, redirect, session, render_template, request, jsonify
# # from flask_debugtoolbar import DebugToolbarExtension
# from werkzeug.exceptions import Unauthorized
# # AUTH_KEY = "username"
import os

import boto3
from botocore.exceptions import ClientError

from flask import Flask, render_template, redirect, session, request
from models import connect_db, db, Image

from PIL import Image, ExifTags
from PIL.ExifTags import TAGS, GPS, IFD, Base

import tempfile

app = Flask(__name__)

# toolbar = DebugToolbarExtension(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///pixly")
app.config['SQLALCHEMY_ECHO'] = True
# app.config['SECRET_KEY'] = "i-have-a-secret"
connect_db(app)
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True

#TODO: update requirements with flask
#
@app.post('/upload')
def view_upload():
    file = request.files["file"]
    id = request.form.get("id")
    title = request.form.get("title")
    keyword = request.form.get("keyword")

    file_name = f"{id}.jpg"
    bucket_name = "r33-pixly"
    exif_data = {}

    s3_url = f'https://{bucket_name}.s3.amazonaws.com/{file_name}'

    with tempfile.NamedTemporaryFile(delete=True) as tmp_file:
        file_content = file.read()
        tmp_file.write(file_content)
        upload_file(tmp_file.name, bucket_name, file_name)

        img = Image.open(tmp_file)
        exif = (img.getexif())

        if exif:
            for tag, value in exif.items():
                # exif_data[Base(tag).name] = value
                if tag in ExifTags.TAGS:
                    tag_name = ExifTags.TAGS[tag]
                    exif_data[tag_name] = value
    # GPSTAGS = {i.value: i.name for i in GPS}
    print(exif_data)

    return render_template("index.html")


@app.get('/')
def view_home():
    """Show and handle form"""


    return render_template("index.html")

# { date_time=exif_data['dateTime']}