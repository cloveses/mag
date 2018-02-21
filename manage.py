from flask import Flask, render_template, request, session
app = Flask(__name__)
app.secret_key = 'lkdjkjf&*^%&(*(*))(775$%^^**(*_+&**&GBHJB'

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()