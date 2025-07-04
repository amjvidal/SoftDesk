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

app.register_blueprint(login_routes)
app.register_blueprint(cadastro_routes)
app.register_blueprint(recuperar_routes)
app.register_blueprint(registroAluno_routes)
app.register_blueprint(registroOutro_routes)


app.run(debug=True)