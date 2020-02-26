from flask import Flask
app = Flask(__name__)

@app.route("/")
def hb():
    return "HeartByte.io"

if __name__ == '__main__':
    app.run(debug=True)    
