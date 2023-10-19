from flask import Flask, render_template, url_for
import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    # Obtenir la date actuelle
    today = datetime.date.today()
    return render_template("index.html", today=today)


@app.route('/men')
def men():
    products=[
        {
            "model": "t-shirt noir",
            "path_img_preview": "images/products/men/tshirts/tshirt_001/tmm001p001.jpg"
        },
        {
            "model": "t-shirt blanc",
            "path_img_preview": "images/products/men/tshirts/tshirt_002/tmm002p001.jpg"
        }
    ]
              
    return render_template("men.html", title="Men", nbProducts=2, products=products)


@app.route('/women')
def women():
    return render_template("women.html", title="Women")

@app.route('/about_us')
def about_us():
    return render_template("about_us.html", title="About Us")

@app.route('/lookbook')
def lookbook():
    return render_template("lookbook.html", title="Lookbook")


@app.route('/contact')
def contact():
    return render_template("contact.html", title="Contact")

@app.route('/login')
def login():
    return render_template("login.html", title="Login")

@app.route('/basket')
def basket():
    return render_template("basket.html", title="Panier")