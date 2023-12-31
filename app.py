from utils import upload_file

import os
import shortuuid
import boto3
from botocore.exceptions import ClientError
from flask_cors import CORS
from flask import Flask, render_template, redirect, session, request, jsonify
from models import connect_db, db, ImageFile

from PIL import Image, ExifTags
from PIL.ExifTags import TAGS, GPS, IFD, Base

import tempfile

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///pixly")
app.config['SQLALCHEMY_ECHO'] = True
connect_db(app)
CORS(app)

@app.post('/upload')
def view_upload():
    """ 
    Creates new image and uploads to s3 : 
            body : { title, keyword1, keyword2, keyword3, [file] }
    returns : 
        { id, title, keyword1, keyword2, keyword3, s3_url }
    """

    file = request.files["file"]
    id = shortuuid.uuid()
    title = request.form.get("title")
    keyword1 = request.form.get("keyword1")
    keyword2 = request.form.get("keyword2")
    keyword3 = request.form.get("keyword3")

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
                if tag in ExifTags.TAGS:
                    tag_name = ExifTags.TAGS[tag]
                    exif_data[tag_name] = value
    # TODO: GPSTAGS = {i.value: i.name for i in GPS}

    input_data = {      
                        's3_url':s3_url,
                        'id':id,
                        'title':title,
                        'keyword1':keyword1,
                        'keyword2':keyword2,
                        'keyword3':keyword3
                        }

    image = ImageFile.create(exif_data, input_data)

    db.session.add(image)
    db.session.commit()

    image = image.to_dict()

    return jsonify(image=image)


@app.get('/')
def view_home():
    """Return a list of all images or matching the search query"""

    if not request.args:
        images = [ image.to_dict() for image in ImageFile.query.all()]
    else:
        title = request.args.get('title')
        images = ImageFile.query.filter(ImageFile.title.like(f"%{title}%")).all()
        images = [image.to_dict() for image in images]

    return jsonify(images=images)