from flask import Blueprint, render_template, request

registroOutro_routes = Blueprint('registroOutro',__name__)

""" Rotas de registro outro
    - /cadastro- Get - Retorna a página de registro de outro
    - /cadastro- Post - Registra outro
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
        print("Dados recebidos no formulário:")
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")
    
    return render_template('registro_outros.html', inputs=inputs)