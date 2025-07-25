from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from firebase import loginfb

login_routes = Blueprint('login',__name__)

""" Rotas de login
    - / - Get - Retorna a página de login
    - / - Post - Verifica o login do usuário
"""
@login_routes.route('/', methods=['GET','POST'])
def login():
    """ Retorna a página de login """
    inputs = [
    {'id': 'email', 'type': 'email', 'placeholder': 'Email', 'name': 'email'},
    {'id': 'senha', 'type': 'password', 'placeholder': 'Senha', 'name': 'senha'},
    ]
    
    if request.method == 'POST':
        dados = {campo['name']: request.form.get(campo['name']) for campo in inputs}

        resultado = loginfb(dados['email'], dados['senha'])

        if resultado['success']:
            session['user'] = resultado['user']
            flash(resultado['message'], 'success')
            return redirect(url_for('home.home'))
        else:
            flash(resultado['message'], 'error')
    
    return render_template('login.html', inputs=inputs)