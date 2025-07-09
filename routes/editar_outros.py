from flask import Blueprint, render_template, request, session, flash, redirect, url_for


editarOutros_routes = Blueprint('editarOutros',__name__)

""" Rotas de editar outros
    - / - Get - Retorna a página de editar outros
    - / - Post - 
"""
@editarOutros_routes.route('/editarOutros', methods=['GET','POST'])
def login():
    return render_template('editar_aluno.html')