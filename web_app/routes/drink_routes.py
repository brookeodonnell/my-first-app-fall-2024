# this is the "web_app/routes/drinks_routes.py" file...

import requests
from flask import Blueprint, request, render_template

drink_routes = Blueprint("drink_routes", __name__)

@drink_routes.route("/")
@drink_routes.route("/drinks")

def drinks():
    print("DRINKS...")

    url = "https://www.thecocktaildb.com/api/json/v1/1/filter.php?a=Non_Alcoholic"
    response = requests.get(url)
    data = response.json()
    drinks = data['drinks']

    

    return render_template("drinks.html", drinks=drinks)
