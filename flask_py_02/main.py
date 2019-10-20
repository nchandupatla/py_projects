from flask import Flask, escape, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)

mail_setting = {
"MAIL_SERVER" : "smtp.gmail.com",
"MAIL_PORT" : 465,
"MAIL_USE_TLS" : False,
"MAIL_USE_SSL" : True,
"MAIL_USERNAME" : "",
"MAIL_PASSWORD" : ""
}

app.config.update(mail_setting)
mail = Mail(app)

@app.route("/")
def index():
    msg = Message("Hello",
                  sender=",
                  recipients=[""])
    mail.send(msg)
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'