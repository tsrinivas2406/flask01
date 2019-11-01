from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Srinivas Tumma , You finally deployed a Flask Application on a Azure Web App Instance. Congratulations !"
