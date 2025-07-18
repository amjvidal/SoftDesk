from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from firebase import db, atualizarAluno, salvarFotoPerfilLocal

# Cria um Blueprint para as rotas de edição de perfil de aluno.

editarAluno_routes = Blueprint('editarAluno', __name__)

@editarAluno_routes.route('/editarAluno', methods=['GET', 'POST'])
def editarAluno():

    """
    Esta função gerencia a página de edição de perfil para usuários do tipo 'aluno'.
    Ela permite que o aluno visualize seus dados atuais e os atualize, incluindo a foto de perfil.
    Obtém o ID do usuário da sessão. Se não houver, redireciona para o login.
    """
    user_id = session.get('user', {}).get('localId')

    if not user_id:
        flash("Você precisa estar logado para editar seu perfil.", "error")
        return redirect(url_for('login.login'))

    inputs = [
        {'id': 'nome', 'type': 'text', 'placeholder': 'Nome', 'name': 'nome'},
        {'id': 'email', 'type': 'email', 'placeholder': 'Email', 'name': 'email'},
        {'id': 'senha', 'type': 'password', 'placeholder': 'Senha', 'name': 'senha'},
        {'id': 'matricula', 'type': 'text', 'placeholder': 'Matrícula', 'name': 'matricula'},
        {'id': 'linkedin', 'type': 'text', 'placeholder': 'LinkedIn', 'name': 'linkedin'},
        {'id': 'bio', 'type': 'textarea', 'placeholder': 'Fale um pouco sobre você', 'name': 'bio'}
    ]

    if request.method == 'POST':
        dados = {campo['name']: request.form.get(campo['name']) for campo in inputs if campo['type'] != 'password'}

        foto = request.files.get('foto')
        if foto and foto.filename != '':
            try:
                url_foto = salvarFotoPerfilLocal(user_id, foto)
                dados['foto_url'] = url_foto
            except Exception as e:
                print("Erro ao salvar foto:", e)
                flash("Erro ao salvar a imagem.", "error")

        try:
            atualizarAluno(user_id, dados)
            flash("Dados atualizados com sucesso!", "success")
        except Exception as e:
            flash(str(e), "error")

    # GET (sempre renderiza a página com os dados atuais)
    user_data = db.child("usuarios").child(user_id).get().val()
    foto_url = user_data.get('foto_url', '')

    for campo in inputs:
        campo['value'] = user_data.get(campo['name'], '')

    return render_template('editar_aluno.html', inputs=inputs, foto_url=foto_url)
