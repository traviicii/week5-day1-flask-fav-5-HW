from flask import redirect, render_template, request, url_for
from app import app

@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html')

@app.route('/fav_5')
def fav5():

    artists = ['Gorillaz', 'Daft Punk', 'Beyonce', 'Boy Harsher', 'Blawan']

    return render_template('fav_5.html', artists = artists)