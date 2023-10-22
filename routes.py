from flask import Flask, render_template, url_for
import datetime

app = Flask(__name__)



    
    # BEFORE ADDING DATABASE FEATURE : 
products=[
    {
        "model_name": "B&W - T-shirt Noir",
        "path_img": "",
        "model_number": "1",
        "type": "tshirt",
        "gender": "men",
        "sku": "BWM01"
    },
    {
        "model_name": "WATCHING OVER YOU - T-shirt OKKGG x Mr. Bertola",
        "path_img": "",
        "model_number": "2",
        "type": "tshirt",
        "gender": "men",
        "sku": "ALEW01"
    },
    {
        "model_name": "TEAMMATES - T-shirt collectif",
        "path_img": "",
        "model_number": "3",
        "type": "tshirt",
        "gender": "men",
        "sku": "TEAMM01"
    },
    {
        "model_name": "Femme à moustache - T-shirt x Marilyn",
        "path_img": "",
        "model_number": "4",
        "type": "tshirt",
        "gender": "men",
        "sku": "MOUSM01"
    },
    {
        "model_name": "Moustache Rose - T-shirt basique",
        "path_img": "",
        "model_number": "5",
        "type": "tshirt",
        "gender": "men",
        "sku": "PINKM01"
    }
]

@app.route('/')
@app.route('/index')
def index():
    # Obtenir la date actuelle
    today = datetime.date.today()
    return render_template("index.html", today=today)


@app.route('/men')
def men():


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

@app.route('/product/<model>', methods=['GET'])
def animals(model):
    
    # BEFORE ADDING DATABASE & SQL REQUEST
    # WILL BE CHANGE LATER

    for i, product in enumerate(products):
        if product["sku"] == model:
            # L'index i correspond au dictionnaire avec la valeur recherchée
            print("L'index du dictionnaire correspondant est :", i)
            break  # Vous pouvez arrêter la recherche si vous avez trouvé une correspondance
    else:
        # Ce bloc est exécuté si la boucle s'exécute jusqu'à la fin sans correspondance
        print("Aucune correspondance trouvée.")
        i = "404"

    print(i)
    if i != "404":
        print("We found the product")
        print(f"i = {i}")
        model=products[i]
    else:
        print("Can't find the product")
        model=False
    return render_template('product.html', title='Product Details', model=model)


@app.route('/test')
def test():
    return render_template("test.html")

@app.route('/payment')
def payment():
    return render_template("payment.html")