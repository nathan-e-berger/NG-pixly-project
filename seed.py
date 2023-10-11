import os
os.environ["DATABASE_URL"] = 'postgresql:///pixly'

from app import app
from models import db, Image

db.drop_all()
db.create_all()

IMAGE_DATA_1 = {
    "title": "titleTEST",
    "keyword1": "keyword1",
    "keyword2": "keyword2",
    "keyword3": "keyword3",
    "make": "makeTEST",
    "model":"modelTEST",
    "image_length": 1200,
    "image_width": 800,
}

image01 = Image(**IMAGE_DATA_1)

db.session.add(image01)
db.session.commit()