from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
# This is a simple Flask application that returns "Hello, Flask!" when accessed at the root URL.   
