from flask import Blueprint, render_template, request
from firebase import db
# Cria um Blueprint para as rotas de detalhes de demanda.
home_detalhes_demanda_routes = Blueprint('homeDetalhesDemanda', __name__)

@home_detalhes_demanda_routes.route('/homeDetalhesDemanda/<demanda_id>')
def homeDetalhesDemanda(demanda_id):
    """
    Esta função exibe os detalhes de uma demanda específica, identificada pelo 'demanda_id'.
    Busca os detalhes da demanda no nó "demandas" do Firebase Realtime Database
    usando o 'demanda_id' fornecido na URL.
    """

    try:
        demanda = db.child("demandas").child(demanda_id).get().val()
        if not demanda:
            return "Demanda não encontrada", 404
        demanda['id'] = demanda_id
    except Exception as e:
        print("Erro ao buscar detalhes da demanda:", e)
        return "Erro interno", 500

    return render_template('home_detalhes_demanda.html', demanda=demanda)
