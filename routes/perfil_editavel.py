from flask import Blueprint, render_template

# Cria um Blueprint para as rotas do perfil editável.

perfil_ed = Blueprint('perfil_ed', __name__, template_folder='../templates')


@perfil_ed.route('/perfileditavel', methods=['GET'])
def exibir_perfil():
    """
    Esta função é responsável por exibir a página de perfil em modo editável.
    Define uma variável booleana para indicar que o perfil pode ser editado.
    """
    pode_editar = True 
    return render_template('perfil_editavel.html', pode_editar=pode_editar)