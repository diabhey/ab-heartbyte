from flask import Flask, render_template, Response

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)