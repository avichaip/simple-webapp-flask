Vimport os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>BLA BLA BLA</h1>"

@app.route('/AVI')
def hello():
    return 'MAORIKCHIK'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
