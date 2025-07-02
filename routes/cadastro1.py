from flask import Blueprint, render_template

cadastro_routes = Blueprint('cadastro',__name__)

""" Rotas de home
    - /cadastro- Get - Retorna a página de cadastro
    - /cadastro- Post - Cadastra o usuário
"""
@cadastro_routes.route('/cadastro', methods=['GET','POST'])
def cadastro():
    """ Retorna a página de cadastro """
    
    return render_template('cadastro1.html')