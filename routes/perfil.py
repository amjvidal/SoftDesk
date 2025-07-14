from flask import Blueprint, render_template


perfil_bp = Blueprint('perfil_bp', __name__, template_folder='../templates')


@perfil_bp.route('/perfil', methods=['GET'])
def exibir_perfil():

    pode_editar = True 
    return render_template('perfil_visualizar.html', pode_editar=pode_editar)