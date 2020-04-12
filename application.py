from flask import Flask, render_template, Response
import pymongo
from pymongo import MongoClient

# Setting up Mongodb 
cluster = MongoClient("---azure.mongodb---") 
db = cluster["heartbyte"]
collection = db["record"]

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug = True)  