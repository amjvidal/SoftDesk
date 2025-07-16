from flask import Blueprint, render_template, session, redirect, url_for, request
from firebase import get_demandas_do_usuario, logout

home_demandas_routes = Blueprint('homeDemandas', __name__)

@home_demandas_routes.route('/homeMinhasDemandas', methods=['GET', 'POST'])
def homeMinhasDemandas():
    user = session.get('user')
    if not user:
        return redirect(url_for('login.login'))
    
    if request.method == 'POST' and request.form.get('acao') == 'logout':
        logout()  # limpa a sessão
        return redirect(url_for('login.login'))

    user_id = user['localId']
    demandas = get_demandas_do_usuario(user_id)

    return render_template('home_minhas_demandas.html', demandas=demandas)
