from flask import Flask

app = Flask(__name__)
app.secret_key = 'softdeskifpe'

#exemplo de criação de rotas
#from routes.home import home_routes
#app.register_blueprint(home_routes)

from routes.login import login_routes
from routes.cadastro1 import cadastro_routes
from routes.recuperar import recuperar_routes
from routes.registro_aluno import registroAluno_routes
from routes.registro_outro import registroOutro_routes
from routes.editar_aluno import editarAluno_routes
from routes.editar_outros import editarOutros_routes
from routes.home import home_routes
from routes.home_demandas import home_demandas_routes
from routes.home_nova_demanda import home_nova_demanda_routes
from routes.home_detalhes_demanda import home_detalhes_demanda_routes
from routes.perfil import perfil_bp
from routes.perfil_editavel import perfil_ed

app.register_blueprint(login_routes)
app.register_blueprint(cadastro_routes)
app.register_blueprint(recuperar_routes)
app.register_blueprint(registroAluno_routes)
app.register_blueprint(registroOutro_routes)
app.register_blueprint(editarAluno_routes)
app.register_blueprint(editarOutros_routes)
app.register_blueprint(home_routes)
app.register_blueprint(home_demandas_routes)
app.register_blueprint(home_nova_demanda_routes)
app.register_blueprint(home_detalhes_demanda_routes)
app.register_blueprint(perfil_bp)
app.register_blueprint(perfil_ed)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)