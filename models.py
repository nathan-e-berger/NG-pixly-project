from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect this database to provided Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)
    

class Image(db.Model):
    """Creates Image instance"""

    __tablename__ = "images"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
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
        nullable=True
    )

    model = db.Column(
        db.String,
        nullable=True
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


