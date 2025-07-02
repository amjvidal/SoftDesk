from flask import Blueprint, render_template

registroAluno_routes = Blueprint('registroAluno',__name__)

""" Rotas de registro aluno
    - /cadastro- Get - Retorna a página de registro de aluno
    - /cadastro- Post - Registra o aluno
"""
@registroAluno_routes.route('/registroAluno', methods=['GET','POST'])
def registroAluno():
    """ Retorna a página de registro de Alunos """
    
    return render_template('registro_aluno.html')