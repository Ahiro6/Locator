from geocode import GeoCode
from flask import Flask, render_template, request, redirect
from map import Mapping
from geocode import GeoCode
from email_access import EmailAccess
from flask_sqlalchemy import SQLAlchemy

emailaccess = EmailAccess()
geo = GeoCode()
map = Mapping()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:adi0103@localhost/YourMaps'
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://suscxlapqrexdd:6abf1e14173029f66aa4f794dc2c2b81284a110125a73a73d8651514bac36961@ec2-3-226-134-153.compute-1.amazonaws.com:5432/d5pi6d3pfdj29v=require'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "coordinates"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    lat_ = db.Column(db.Integer)
    lon_ = db.Column(db.Integer)
    place_ = db.Column(db.String(120))

    def __init__(self, email_, lat_, lon_, place_):
        self.email_ = email_
        self.lat_ = lat_
        self.lon_ = lon_
        self.place_ = place_


def insert(email, lat, lon, place):
        data = Data(email, lat, lon, place)
        db.session.add(data)
        db.session.commit()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/", methods=['POST'])
def home_post():
    if request.method == 'POST':
        email = request.form['email']
        place = request.form['place']
        msg = None

        if db.session.query(Data).filter(Data.email_==email).count() == 0:
            geo.locate(place)
            insert(email, geo.location.latitude, geo.location.longitude, place)
            map.createMarker(geo, place)
            emailaccess.send_email(email, geo.location.longitude, geo.location.latitude, db.session.query(Data.place_).scalar(), db.session.query(Data.place_).filter(Data.place_ == place).count())
            msg = "Success! You will have your email shortly."  

        else:
            msg = "This email is already taken..."
            

    return render_template("home.html", text=msg)

if __name__ == "__main__":
    app.run(debug=True)