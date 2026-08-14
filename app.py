import psycopg2

from flask import Flask, render_template, redirect, request, url_for


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ in "__main__":
    app.run(debug=True)