from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect this database to provided Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)


class ImageFile(db.Model):
    """Creates Image instance"""

    __tablename__ = "images"

    def to_dict(self):
        """serialize to dict"""

        return {"id": self.id,
                "title": self.title,
                "keyword1": self.keyword1,
                "keyword2": self.keyword2,
                "keyword3": self.keyword3,
                "s3_url": self.s3_url}

    id = db.Column(
        db.String,
        primary_key=True,
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
        nullable=True,
        default=None
    )

    image_length = db.Column(
        db.Integer,
        nullable=True,
        default=None
    )

    s3_url = db.Column(
    db.String,
    nullable=False
    )

    @classmethod
    def create(cls, exif_data, input_data):
        image = ImageFile(
                    make=exif_data['Make'],
                    model=exif_data['Model'],
                    date_time=exif_data['DateTime'],
                        image_width=exif_data.get('ImageWidth'),
                        image_length= exif_data.get('ImageLength'),
                        s3_url=input_data['s3_url'],
                        id=input_data['id'],
                        title=input_data['title'],
                        keyword1=input_data['keyword1'],
                        keyword2=input_data['keyword2'],
                        keyword3=input_data['keyword3']
                        )
        print(image)

        return image







    # { date_time=exif_data['dateTime']}

    # exposure =
    # white_balance =
    # focal_length =


