from flask import Blueprint, render_template, session, redirect, url_for
from firebase import get_demandas_do_usuario

home_demandas_routes = Blueprint('homeDemandas', __name__)

@home_demandas_routes.route('/homeMinhasDemandas')
def homeMinhasDemandas():
    user = session.get('user')
    if not user:
        return redirect(url_for('login.login'))

    user_id = user['localId']
    demandas = get_demandas_do_usuario(user_id)

    return render_template('home_minhas_demandas.html', demandas=demandas)
