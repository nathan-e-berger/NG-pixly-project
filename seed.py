import os
os.environ["DATABASE_URL"] = 'postgresql:///pixly'

from app import app
from models import db, ImageFile

db.drop_all()
db.create_all()

IMAGE_DATA_1 = {
    "id":"i4SUVYhG6dathPqdFv76n4",
    "title": "titleTEST",
    "keyword1": "keyword1",
    "keyword2": "keyword2",
    "keyword3": "keyword3",
    "make": "makeTEST",
    "model":"modelTEST",
    "image_length": 1200,
    "image_width": 800,
    "s3_url":'i4SUVYhG6dathPqdFv76n4.jpg',
    "date_time":"2008:07:31 10:38:11",
}

image01 = ImageFile(**IMAGE_DATA_1)

db.session.add(image01)
db.session.commit()