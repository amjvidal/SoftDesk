from flask import Blueprint, render_template, session, redirect, url_for, request
from firebase import get_demandas_do_usuario, logout

# Cria um Blueprint para as rotas relacionadas às demandas do usuário.

home_demandas_routes = Blueprint('homeDemandas', __name__)

@home_demandas_routes.route('/homeMinhasDemandas', methods=['GET', 'POST'])
def homeMinhasDemandas():

    """
    Esta função exibe a página com as demandas criadas pelo usuário logado.
    Ela também lida com a funcionalidade de logout.
    Verifica se o usuário está logado. Se não estiver, redireciona para a página de login.
    """
    user = session.get('user')
    if not user:
        return redirect(url_for('login.login'))
    
    if request.method == 'POST' and request.form.get('acao') == 'logout':
        logout()  # limpa a sessão
        return redirect(url_for('login.login'))

    user_id = user['localId']
    demandas = get_demandas_do_usuario(user_id)

    return render_template('home_minhas_demandas.html', demandas=demandas)
