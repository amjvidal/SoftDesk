"""
main.py
- Este arquivo principal contém a inicialização da aplicação Flask,
- a configuração da chave secreta e o registro de todos os Blueprints
- (módulos de rota) da aplicação. Ele serve como o ponto de entrada
- para rodar o servidor web do SoftDesk IFPE.
"""

from flask import Flask
"""
- Inicialização da aplicação Flask
"""
app = Flask(__name__)
"""
- Configura a chave secreta da aplicação.
- A chave secreta é essencial para a segurança de sessões e proteção CSRF.
"""
app.secret_key = 'softdeskifpe'

"""
- Importação e registro dos Blueprints da aplicação.
- Cada Blueprint agrupa rotas e funcionalidades relacionadas,
- promovendo a modularidade e organização do código.
"""
#Bloco de autenticação e registro de usuários.

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

# Bloco de gerenciamento de perfil do usuário.
from routes.perfil import perfil_bp
from routes.perfil_editavel import perfil_ed

# Registra os Blueprints na aplicação principal.
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

#Função principal para executar a aplicação Flask.
"""
- Inicia o servidor de desenvolvimento do Flask.
- Configura o host para '0.0.0.0' para ser acessível externamente e a porta para 5000.
- O modo de depuração (debug=True) é ativado para facilitar o desenvolvimento,
- permitindo recarregamento automático e um depurador interativo.
"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)