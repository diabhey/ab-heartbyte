from flask import Flask
app = Flask(__name__)

@app.route("/")
def hb():
    return "Welcome to HeartByte.io"

if __name__ == '__main__':
    app.run(debug=True)    