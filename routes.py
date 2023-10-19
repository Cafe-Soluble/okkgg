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
    
    # BEFORE ADDING DATABASE FEATURE : 
    products=[
        {
            "model_name": "B&W - T-shirt Noir",
            "path_img": "",
            "model_number": "1",
            "type": "tshirt",
            "gender": "men",
        },
        {
            "model_name": "WATCHING OVER YOU - T-shirt OKKGG x Mr. Bertola",
            "path_img": "",
            "model_number": "2",
            "type": "tshirt",
            "gender": "men",
        },
        {
            "model_name": "TEAMMATES - T-shirt collectif",
            "path_img": "",
            "model_number": "3",
            "type": "tshirt",
            "gender": "men",
        },
        {
            "model_name": "Femme à moustache - T-shirt x Marilyn",
            "path_img": "",
            "model_number": "4",
            "type": "tshirt",
            "gender": "men",
        },
        {
            "model_name": "Moustache Rose - T-shirt basique",
            "path_img": "",
            "model_number": "5",
            "type": "tshirt",
            "gender": "men",
        }
    ]

    for product in products:
        product['path_img'] = 'images/products/'+product['gender']+'/'+product['type']+'/'+product['model_number']+'/'   
        print(product['path_img'])

    return render_template("men.html", title="Men", nbProducts=len(products), products=products)


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