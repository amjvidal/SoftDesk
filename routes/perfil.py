from flask import Blueprint, render_template

# Cria um Blueprint para as rotas da página de visualização de perfil.

perfil_bp = Blueprint('perfil_bp', __name__, template_folder='../templates')


@perfil_bp.route('/perfil', methods=['GET'])
def exibir_perfil():
    """
    Esta função exibe a página de perfil do usuário no modo de visualização
    Define uma variável booleana que pode ser usada no template para controlar
    a visibilidade de elementos de edição (mesmo que esta rota seja para visualização,
    pode haver lógica condicional no HTML).
    """
    pode_editar = True 
    return render_template('perfil_visualizar.html', pode_editar=pode_editar)