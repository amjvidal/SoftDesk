from flask import Blueprint, render_template, request, session, flash, redirect, url_for

# Cria um Blueprint para as rotas de edição de perfis 'outros' (não alunos).
editarOutros_routes = Blueprint('editarOutros',__name__)

"""
Rotas de Edição para Outros Usuários

- /editarOutros (GET): Retorna a página para edição de perfis que não são de alunos.
- /editarOutros (POST): Processa os dados enviados pelo formulário de edição (atualmente não implementado).
"""
@editarOutros_routes.route('/editarOutros', methods=['GET','POST'])
def login():
    return render_template('editar_aluno.html')