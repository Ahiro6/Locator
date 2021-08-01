from flask_sqlalchemy import SQLAlchemy

class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    lat_ = db.Column(db.Integer)
    lon_ = db.Column(db.Integer)
    place_ = db.Column(db.Integer)

    def __init__(self, email_, lat_, lon_, place_):
        self.email_ = email_
        self.lat_ = lat_
        self.lon_ = lon_
        self.place_ = place_

