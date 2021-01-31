# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask
import os

app = Flask(__name__)
_42 = os.environ.get('42')

@app.route('/')
def hello_world():
    if _42:
        return _42
    else:
        return 'Hello World!!'

@app.route('/health')
def health():
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
