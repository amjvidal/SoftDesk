from flask import Blueprint, render_template


perfil_ed = Blueprint('perfil_ed', __name__, template_folder='../templates')


@perfil_ed.route('/perfileditavel', methods=['GET'])
def exibir_perfil():

    pode_editar = True 
    return render_template('perfil_editavel.html', pode_editar=pode_editar)