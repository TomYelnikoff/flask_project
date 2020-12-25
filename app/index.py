from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_alex():
    return "Hello Alex!"
app.run(host="0.0.0.0", port=5000)