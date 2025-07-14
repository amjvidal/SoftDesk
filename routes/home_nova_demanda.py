from flask import Blueprint, render_template, request, redirect, url_for

home_nova_demanda_routes = Blueprint('homeNovaDemanda', __name__)

@home_nova_demanda_routes.route('/homeNovaDemanda')
def homeCriarDemanda():
    return render_template('home_criar_demanda.html')