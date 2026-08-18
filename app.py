from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/shop")
def shop():
    return render_template("shop.html")


@app.route("/new-arrivals")
def new_arrivals():
    return "<h1>New Arrivals page coming soon</h1>"


@app.route("/thrifted")
def thrifted():
    return render_template("thrifted.html")


@app.route("/brand-new")
def brand_new():
    return "<h1>Brand New page coming soon</h1>"


@app.route("/collections")
def collections():
    return "<h1>Collections page coming soon</h1>"


@app.route("/about")
def about():
    return "<h1>About page coming soon</h1>"


@app.route("/contact")
def contact():
    return "<h1>Contact page coming soon</h1>"


if __name__ == "__main__":
    app.run(debug=True)
