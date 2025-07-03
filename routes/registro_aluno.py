from flask import Blueprint, render_template, request

registroAluno_routes = Blueprint('registroAluno',__name__)

""" Rotas de registro aluno
    - /cadastro- Get - Retorna a página de registro de aluno
    - /cadastro- Post - Registra o aluno
"""
@registroAluno_routes.route('/registroAluno', methods=['GET','POST'])
def registroAluno():
    """ Retorna a página de registro de Alunos """
    inputs = [
    {'id': 'nome_completo', 'type': 'text', 'placeholder': 'Nome Completo *', 'name': 'nome_completo'},
    {'id': 'email', 'type': 'email', 'placeholder': 'Email (discente) *', 'name': 'email'},
    {'id': 'matricula', 'type': 'text', 'placeholder': 'Matrícula *', 'name': 'matricula'},
    {'id': 'cpf', 'type': 'text', 'placeholder': '000.000.000-00', 'name': 'cpf'},
    {'id': 'senha', 'type': 'password', 'placeholder': 'Senha *', 'name': 'senha'},
    {'id': 'confirmaSenha', 'type': 'password', 'placeholder': 'Confirme sua senha *', 'name': 'confirmaSenha'},
    {'id': 'bio', 'type': 'textarea', 'placeholder': 'Fale sobre você', 'name': 'bio'},
]
    if request.method == 'POST':
        dados = {campo['name']: request.form.get(campo['name']) for campo in inputs}
        print("Dados recebidos no formulário:")
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")
            
    return render_template('registro_aluno.html', inputs=inputs)