from flask import Blueprint, render_template, redirect, request, url_for
from firebase import get_todas_demandas, logout

# Cria um Blueprint para as rotas da página inicial.

home_routes = Blueprint('home', __name__)

@home_routes.route('/home', methods=['GET', 'POST'])
def home():
    """
    Esta função gerencia a exibição da página inicial, onde todas as demandas são listadas.
    Também lida com a funcionalidade de logout.
    Se a requisição for POST e a ação do formulário for 'logout', o usuário é deslogado
    e redirecionado para a página de login.
    """
    if request.method == 'POST' and request.form.get('acao') == 'logout':
        logout()  # limpa a sessão
        return redirect(url_for('login.login'))
    
    demandas = get_todas_demandas()
    return render_template('home.html', demandas=demandas)
