from flask import Blueprint, render_template, request, redirect, url_for

home_demandas_routes = Blueprint('homeDemandas', __name__)

@home_demandas_routes.route('/homeMinhasDemandas')
def homeMinhasDemandas():
    return render_template('home_minhas_demandas.html')