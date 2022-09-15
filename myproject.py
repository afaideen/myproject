
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    str = "Assalamualaikum. Anda berjaya dunia akhirat...Dengan izin Tuhan Yang Esa dan Maha Berkuasa..."
    return str
    # return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')