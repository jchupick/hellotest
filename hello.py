from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from root'
  
@app.route('/greet')
def say_hello():
    return 'Hello from greet directory'
