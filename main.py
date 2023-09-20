from flask import Flask, render_template
import os


app = Flask(__name__)
app.secret_key = os.getenv('relearn_flask_key')


@app.route('/')
def main():
	return render_template('./index.html')


if __name__ == '__main__':
	app.run()


