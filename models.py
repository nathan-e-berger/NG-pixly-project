from flask_sqlalchemy import SQLAlchemy

# pip install Flask-SQLAlchemy
db = SQLAlchemy()

class Image(db.Model):
    """Creates Image instance"""

    __tablename__ = "images"

    id = db.Column(
        db.Serial,
        primary_key=True,
        unique=True
    )

    title = db.Column(
        db.String,
        nullable=False
    )
    keyword1 = db.Column(
        db.String,
        nullable=False
    )
    keyword2 = db.Column(
        db.String,
        nullable=False
    )
    keyword3 = db.Column(
        db.String,
        nullable=False
    )
# TODO: can add defaults, then switch to nullable=false

    make = db.Column(
        db.String,
        nullble=True
    )

    model = db.Column(
        db.String,
        nullabe=True
    )

    date_time = db.Column(
        db.String,
        nullable=True
    )

    image_width = db.Column(
        db.Integer,
        nullable=False
    )

    image_length = db.Column(
        db.Integer,
        nullable=False
    )

    # exposure =
    # white_balance =

    # focal_length =


