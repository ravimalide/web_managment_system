import configparser

from flask import Flask, render_template

################
version = "0.1"
################

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')
config.set('systemSettings', 'version', version)

@app.route('/')
def index():
    return render_template('index.html', config=config)

@app.route('/error/<string:e>')
def error(e):
    return render_template('error.html', error=e)


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=False)