from flask import Flask, render_template, request, session
from pony.orm import db_session, ObjectNotFound, commit, select
from db.mypony import pony
# from db.models import Person
from db.persondl import test

app = Flask(__name__)
app.secret_key = 'lkdjkjf&*^%&(*(*))(775$%^^**(*_+&**&GBHJB'
app.config.from_object('settings.Config')
pony.init_app(app)
pony.connect()


@app.route('/')
@db_session
def hello_world():
    # p1 = Person(name='John', age=20)
    test()
    # for p in select(p for p in Person):
    #     print(p.name)
    return 'Hello World!'

if __name__ == '__main__':
    app.run()