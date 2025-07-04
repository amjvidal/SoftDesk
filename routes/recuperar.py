from flask import Blueprint, render_template, request, flash, redirect, url_for
from firebase import recoverPassword

recuperar_routes = Blueprint('recuperar',__name__)

""" Rotas de home
    - /cadastro- Get - Retorna a página de recuperar senha
    - /cadastro- Post - Firebase faz a magica
"""
@recuperar_routes.route('/recuperar', methods=['GET','POST'])
def recuperar():
    """ Retorna a página de recuperar senha """
    inputs = [
        {'id': 'email', 'type': 'email', 'placeholder': 'Email', 'name': 'email'},
    ]
    
    if request.method == 'POST':
        dados = {campo['name']: request.form.get(campo['name']) for campo in inputs}
        email = dados.get('email')
        print("Dados recebidos no formulário:")
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")
        
        if email:
            try:
                recoverPassword(email)
                flash('Email para recuperação enviado com sucesso! Verifique sua caixa de entrada.', 'success')
                return redirect(url_for('login.login'))
            except Exception as e:
                print(f"Erro ao enviar email de recuperação: {e}")
                flash('Erro ao enviar email de recuperação. Tente novamente.', 'danger')
        else:
            flash('Por favor, informe um email válido.', 'warning')
    
    return render_template('recuperar_senha.html', inputs=inputs)