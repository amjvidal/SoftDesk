from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from firebase import criar_demanda, logout

# Cria um Blueprint para as rotas de criação de novas demandas.

home_nova_demanda_routes = Blueprint('homeNovaDemanda', __name__)

@home_nova_demanda_routes.route('/homeNovaDemanda', methods=['GET', 'POST'])
def homeCriarDemanda():

    """
    Esta função gerencia a página onde os usuários podem criar novas demandas.
    Ela lida com a submissão do formulário de criação de demanda e o logout.
    """
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        categoria = request.form.get('categoria')
        descricao = request.form.get('descricao')

        user_id = session.get('user', {}).get('localId')

        if not user_id:
            flash("Usuário não autenticado.", "error")
            return redirect(url_for('login.login'))
        
        if request.method == 'POST' and request.form.get('acao') == 'logout':
            logout()  # limpa a sessão
            return redirect(url_for('login.login'))

        try:
            criar_demanda(user_id, titulo, categoria, descricao)
            flash("Demanda criada com sucesso!", "success")
            return redirect(url_for('home.home'))
        except Exception as e:
            flash(str(e), "error")

    return render_template('home_criar_demanda.html')
