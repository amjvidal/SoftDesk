from flask import Blueprint, render_template

login_routes = Blueprint('login',__name__)

""" Rotas de login
    - / - Get - Retorna a página de login
    - / - Post - Verifica o login do usuário
"""
@login_routes.route('/', methods=['GET','POST'])
def login():
    """ Retorna a página de login """
    
    return render_template('login.html')