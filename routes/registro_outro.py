from flask import Blueprint, render_template, request, flash, redirect, url_for
from firebase import cadastroDocente

#Cria um Blueprint para as rotas de registro de "outros" usuários (e.g., docentes).

registroOutro_routes = Blueprint('registroOutro',__name__)

"""
Rotas de Registro para Outros Usuários

- [cite_start]/registroOutro (GET): Retorna a página do formulário de registro para usuários que não são alunos[cite: 6].
- [cite_start]/registroOutro (POST): Processa os dados enviados pelo formulário para registrar um novo usuário do tipo "outro" (ex: docente)[cite: 6].
"""
@registroOutro_routes.route('/registroOutro', methods=['GET','POST'])
def registroOutro():
    """ Retorna a página de registro de outros """
    inputs = [
    {'id': 'nome', 'type': 'text', 'placeholder': 'Nome Completo *', 'name': 'nome'},
    {'id': 'email', 'type': 'email', 'placeholder': 'Email (discente) *', 'name': 'email'},
    {'id': 'cpf', 'type': 'text', 'placeholder': '000.000.000-00', 'name': 'cpf'},
    {'id': 'ocupacao', 'type': 'text', 'placeholder': 'Ocupação *', 'name': 'ocupacao'},
    {'id': 'senha', 'type': 'password', 'placeholder': 'Senha *', 'name': 'senha'},
    {'id': 'confirmaSenha', 'type': 'password', 'placeholder': 'Confirme sua senha *', 'name': 'confirmaSenha'},
    {'id': 'bio', 'type': 'textarea', 'placeholder': 'Fale sobre você', 'name': 'bio'},
]
    
    if request.method == 'POST':
        dados = {campo['name']: request.form.get(campo['name']) for campo in inputs}

        if dados['senha'] != dados['confirmaSenha']:
            flash("As senhas não coincidem.", "error")
            return render_template('registro_outros.html', inputs=inputs)

        try:
            cadastroDocente(
                nome=dados['nome'],
                email=dados['email'],
                password=dados['senha'],
                cpf=dados['cpf'],
                ocupacao=dados['ocupacao'],
                bio=dados['bio']
            )
            flash("Cadastro realizado com sucesso! Verifique seu e-mail.", "success")
            return redirect(url_for('login.login'))
        except Exception as e:
            flash(f"Erro ao cadastrar: {str(e)}", "error")
    
    return render_template('registro_outros.html', inputs=inputs)