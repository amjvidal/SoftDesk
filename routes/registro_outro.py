from flask import Blueprint, render_template

registroOutro_routes = Blueprint('registroOutro',__name__)

""" Rotas de registro outro
    - /cadastro- Get - Retorna a página de registro de outro
    - /cadastro- Post - Registra outro
"""
@registroOutro_routes.route('/registroOutro', methods=['GET','POST'])
def registroOutro():
    """ Retorna a página de registro de outros """
    
    return render_template('registro_outros.html')