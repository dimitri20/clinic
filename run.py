from flask import Flask, url_for, render_template
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)