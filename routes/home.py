from flask import Blueprint, render_template
from firebase import get_todas_demandas

home_routes = Blueprint('home', __name__)

@home_routes.route('/home')
def home():
    demandas = get_todas_demandas()
    return render_template('home.html', demandas=demandas)
