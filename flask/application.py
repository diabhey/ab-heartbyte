from flask import Flask, render_template, Response
import pymongo
from pymongo import MongoClient

# Setting up Mongodb
cluster = MongoClient("---azure.mongodb---")
db = cluster["heartbyte"]
collection = db["record"]

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
