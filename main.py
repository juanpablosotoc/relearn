from flask import Flask
import os


app = Flask(__name__)
app.secret_key = os.getenv('relearn_flask_key')


@app.route('/')
def main():
	return 'hello'


if __name__ == '__main__':
	app.run()


