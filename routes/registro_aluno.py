from flask import Blueprint, render_template, request, flash, redirect, url_for
from firebase import cadastroAluno

registroAluno_routes = Blueprint('registroAluno',__name__)

""" Rotas de registro aluno
    - /cadastro- Get - Retorna a página de registro de aluno
    - /cadastro- Post - Registra o aluno
"""
@registroAluno_routes.route('/registroAluno', methods=['GET','POST'])
def registroAluno():
    """ Retorna a página de registro de Alunos """
    inputs = [
    {'id': 'nome', 'type': 'text', 'placeholder': 'Nome Completo *', 'name': 'nome'},
    {'id': 'email', 'type': 'email', 'placeholder': 'Email (discente) *', 'name': 'email'},
    {'id': 'matricula', 'type': 'text', 'placeholder': 'Matrícula *', 'name': 'matricula'},
    {'id': 'cpf', 'type': 'text', 'placeholder': '000.000.000-00', 'name': 'cpf'},
    {'id': 'senha', 'type': 'password', 'placeholder': 'Senha *', 'name': 'senha'},
    {'id': 'confirmaSenha', 'type': 'password', 'placeholder': 'Confirme sua senha *', 'name': 'confirmaSenha'},
    {'id': 'bio', 'type': 'textarea', 'placeholder': 'Fale sobre você', 'name': 'bio'},
]
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        cpf = request.form.get('cpf')
        matricula = request.form.get('matricula')
        senha = request.form.get('senha')
        confirma_senha = request.form.get('confirmaSenha')
        bio = request.form.get('bio')

        if senha != confirma_senha:
            flash("As senhas não coincidem.", "error")
            return render_template('registro_aluno.html', inputs=inputs)

        try:
            cadastroAluno(nome, email, senha, cpf, matricula, bio)
            flash("Cadastro realizado com sucesso! Verifique seu e-mail.", "success")
            return redirect(url_for('login.login'))  
        except Exception as e:
            flash(f"Erro ao cadastrar: {str(e)}", "error")
            
    return render_template('registro_aluno.html', inputs=inputs)