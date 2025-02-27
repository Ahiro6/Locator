from email.mime.text import MIMEText
import aiosmtpd
import smtplib

import os

class EmailAccess: 
    def __init__(self):
        self.subject = "Locator: YourMaps"

        self.from_email = os.getenv('EMAIL')
        self.from_password = os.getenv('PASSWORD')

    def send_email(self, email, lon, lat, place, data):
        self.email = email
        self.lon = lon
        self.lat = lat
        self.place = place
        self.data = data

        message = f"Here is your entry! <br> Lon: <strong>{self.lon}</strong>, Lat: <strong>{self.lat} </strong><br> Place: <strong> {self.place} </strong> <br> Data: A total of <strong>{self.data}</strong> people live where you live."
        msg = MIMEText(message, "html")

        msg["Subject"] = self.subject
        msg["From"] = self.from_email
        msg["To"] = self.email

        gmail = smtplib.SMTP("smtp.gmail.com", 587)
        gmail.ehlo();
        gmail.starttls();
        gmail.login(self.from_email, self.from_password)
        gmail.send_message(msg)


    

