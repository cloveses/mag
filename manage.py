from flask import Flask, render_template, request, session
from flask_pony import Pony

app = Flask(__name__)
app.secret_key = 'lkdjkjf&*^%&(*(*))(775$%^^**(*_+&**&GBHJB'
app.config.from_object('settings.Config')

pony = Pony(app)

from db import common

pony.connect()



@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()