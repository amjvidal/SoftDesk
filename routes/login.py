from flask import Blueprint, render_template, request

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
        print("Dados recebidos no formulário:")
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")
    
    return render_template('login.html', inputs=inputs)