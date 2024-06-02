from flask import Flask,request
import json 

app = Flask(__name__)

@app.get('/')
def home():
    return "Hello from flask"

# create  another API that redirects you to a test

@app.get('/test')
def test():
    me={'name': 'Amber Patton'}
    return json.dumps(me)

@app.route('/server')
def server():
    server=request.environ.get('SERVER_SOFTWARE')
    return server

@app.get('/api/about')
def about():
    return "Hello from the about"

app.run(debug=True)