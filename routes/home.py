from flask import Blueprint, render_template, redirect, request, url_for
from firebase import get_todas_demandas, logout

home_routes = Blueprint('home', __name__)

@home_routes.route('/home', methods=['GET', 'POST'])
def home():
    
    if request.method == 'POST' and request.form.get('acao') == 'logout':
        logout()  # limpa a sessão
        return redirect(url_for('login.login'))
    
    demandas = get_todas_demandas()
    return render_template('home.html', demandas=demandas)
