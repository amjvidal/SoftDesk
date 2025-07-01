from flask import Flask

app = Flask(__name__)

#exemplo de criação de rotas
#from routes.home import home_routes
#app.register_blueprint(home_routes)


app.run(debug=True)