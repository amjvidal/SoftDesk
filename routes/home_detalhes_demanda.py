from flask import Blueprint, render_template, request, redirect, url_for

home_detalhes_demanda_routes = Blueprint('homeDetalhesDemanda', __name__)

@home_detalhes_demanda_routes.route('/homeDetalhesDemanda')
def homeDetalhesDemanda():
    return render_template('home_detalhes_demanda.html')