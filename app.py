# API - É um lugar para disponibilizar recursos e/ou funcionalidades
# 1. Objetivo - Criar uma API que disponibiliza a consulta, criação, edição e exclusão de livros
# 2. URL base - localhost
# 3. Endpoints - Localhost/livros (GET) - obter todos os livros
#                -localhost/livros (POST) - adicionar um livro
#                -localhost/livros/id (GET) - obter um livro por id
#                -localhost/livro/id (PUT) - alterar um livro por id
#                -localhost/livro/id (DELETE) - deletar um livro por id
# 4. Quais recursos - Livros

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título' : 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor' : 'J.R.R Tolkien'
    },

    {
        'id': 2,
        'título' : 'Harry Potter a Pedra Filosofal',
        'autor' : 'J.K Howling'
    },

    {
        'id': 3,
        'título' : 'Hábitos Atômicos',
        'autor' : 'James Clear'
    }
]

#Consultar(todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

#Consultar(id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
       if livro.get('id') == id:
           return jsonify(livro)

#Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get("id") == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
#criar
@app.route('/livros', methods=['POST'])
def incluit_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)
#Excluir
@app.route('/livros/<int:id>',methods=['DELETE'])
def exluir_livro(id):
    for indice, livro in enumerate(livros):
            if livro.get('id') == id:
                del livros[indice]

    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)