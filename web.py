from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import os

app = Flask(__name__)
app.debug = True

#Criar GetByID: http://blog.luisrei.com/articles/flaskrest.html
@app.route('/api/v1/filmes/multicine', methods=['GET'])
def EmCartazMulticine():
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'
    html_doc = urlopen(Request("https://www.filmesnocinema.com.br/cinemas/multicine-timon", headers={'User-Agent': user_agent})).read()

    soup = BeautifulSoup(html_doc, "html.parser")

    data = []
    for dataBox in soup.find_all("li", class_="movies-list__item"):
        titleObj = dataBox.find("div", class_="movie-info").find("h2")
        imgObj = dataBox.find("picture")

        data.append({ 'nome': titleObj.text.strip(),
                      'image': imgObj.img['data-original'].strip()})



    return jsonify({'filmes': data})

@app.route('/api/v1/filmes/cinemateresina', methods=['GET'])
def EmCartazCinemateresina():
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'
    html_doc = urlopen(Request("https://www.filmesnocinema.com.br/cinemas/cinemas-teresina", headers={'User-Agent': user_agent})).read()

    soup = BeautifulSoup(html_doc, "html.parser")

    data = []
    for dataBox in soup.find_all("li", class_="movies-list__item"):
        titleObj = dataBox.find("div", class_="movie-info").find("h2")
        imgObj = dataBox.find("picture")

        data.append({ 'nome': titleObj.text.strip(),
                      'image': imgObj.img['data-original'].strip()})


    return jsonify({'filmes': data})

@app.route('/api/v1/filmes/cinepolisriopoty', methods=['GET'])
def EmCartazCinepolisriopoty():
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'
    html_doc = urlopen(Request("https://www.filmesnocinema.com.br/cinemas/cinepolis-rio-poty", headers={'User-Agent': user_agent})).read()

    soup = BeautifulSoup(html_doc, "html.parser")

    data = []
    for dataBox in soup.find_all("li", class_="movies-list__item"):
        titleObj = dataBox.find("div", class_="movie-info").find("h2")
        imgObj = dataBox.find("picture")

        data.append({ 'nome': titleObj.text.strip(),
                      'image': imgObj.img['data-original'].strip()})


    return jsonify({'filmes': data})

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    # Tem que ser 0.0.0.0 para rodar no Heroku
    app.run(host='127.0.0.1', port=port)
