# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask
import os
import sys 
WHO = os.environ['WHO']


app = Flask(__name__)

@app.route('/')
def hello_world():        
    file1 = open('/opt/app-root/secure/myapp.sec', 'r') 
    Lines = file1.readlines() 
  
    count = 0
    # Strips the newline character 
    op = ""
    for line in Lines: 
        op += "Secret Line{}: {}".format(count, line.strip())
        
    if WHO:
        if op:
            return op
        else:
            return WHO
    else:
        return 'Hello World!!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    

