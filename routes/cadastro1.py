from flask import Blueprint, render_template, request, url_for, redirect

cadastro_routes = Blueprint('cadastro',__name__)

""" Rotas de home
    - /cadastro- Get - Retorna a página de cadastro
    - /cadastro- Post - Leva o usuario para as paginas de registro
"""
@cadastro_routes.route('/cadastro', methods=['GET','POST'])
def cadastro():
    """ Retorna a página de cadastro """
    acao = request.form.get('acao')
    
    if acao == 'aluno':
        return redirect(url_for('registroAluno.registroAluno'))
    elif acao == 'outros':
        return redirect(url_for('registroOutro.registroOutro'))
    elif acao == 'voltar':
        return redirect(url_for('login.login'))
        
    return render_template('cadastro1.html')