from flask import Blueprint, render_template, request, url_for, redirect

# Cria um Blueprint chamado 'cadastro'.

cadastro_routes = Blueprint('cadastro',__name__)

"""
Rotas de Cadastro

- /cadastro (GET): Retorna a página de seleção de tipo de cadastro (aluno/outros).
- /cadastro (POST): Redireciona o usuário para a página de registro específica
  baseado na escolha feita no formulário ('aluno' ou 'outros'),
  ou retorna à página de login se a ação for 'voltar'.
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