from flask import Blueprint, render_template, request, redirect, url_for

home_routes = Blueprint('home', __name__)

@home_routes.route('/home')
def home():
    return render_template('home.html')