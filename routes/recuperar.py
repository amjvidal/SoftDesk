from flask import Blueprint, render_template

recuperar_routes = Blueprint('recuperar',__name__)

""" Rotas de home
    - /cadastro- Get - Retorna a página de recuperar senha
    - /cadastro- Post - Firebase faz a magica
"""
@recuperar_routes.route('/recuperar', methods=['GET','POST'])
def recuperar():
    """ Retorna a página de recuperar senha """
    
    return render_template('recuperar_senha.html')