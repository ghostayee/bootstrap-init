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
    return render_template("new-arrivals.html")


@app.route("/thrifted")
def thrifted():
    return render_template("thrifted.html")


@app.route("/brand-new")
def brand_new():
    return render_template("brand-new.html")


@app.route("/collections")
def collections():
    return render_template("collections.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
