#Marcos Gabriel de Sousa Ferreira    TSI-P5

from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados voláteis para simular armazenamento
produtos = []
usuarios = []
setores = []
categorias = []
id_counter = 1


def encontrar_por_id(lista, item_id):  # Função para encontrar um item pelo ID em uma lista de itens
    for item in lista:
        if item['id'] == item_id:
            return item
    return None


@app.route('/produtos', methods=['GET', 'POST']) # Endpoint para listar todos os produtos ou adicionar um novo produto
def gerenciar_produtos():
    global id_counter
    if request.method == 'GET':
        return jsonify(produtos)
    elif request.method == 'POST':
        data = request.get_json()
        novo_produto = {'id': id_counter, 'nome': data['nome']}
        produtos.append(novo_produto)
        id_counter += 1
        return jsonify(novo_produto), 201


@app.route('/usuarios', methods=['GET', 'POST']) # Endpoint para obter ou adicionar um usuário
def gerenciar_usuarios():
    global id_counter
    if request.method == 'GET':
        return jsonify(usuarios)
    elif request.method == 'POST':
        data = request.get_json()
        novo_usuario = {'id': id_counter, 'nome': data['nome']}
        usuarios.append(novo_usuario)
        id_counter += 1
        return jsonify(novo_usuario), 201


@app.route('/setores', methods=['GET', 'POST']) # Endpoint para obter ou adicionar um setor
def gerenciar_setores():
    global id_counter
    if request.method == 'GET':
        return jsonify(setores)
    elif request.method == 'POST':
        data = request.get_json()
        novo_setor = {'id': id_counter, 'nome': data['nome']}
        setores.append(novo_setor)
        id_counter += 1
        return jsonify(novo_setor), 201


@app.route('/categorias', methods=['GET', 'POST']) # Endpoint para obter ou adicionar uma categoria
def gerenciar_categorias():
    global id_counter
    if request.method == 'GET':
        return jsonify(categorias)
    elif request.method == 'POST':
        data = request.get_json()
        nova_categoria = {'id': id_counter, 'nome': data['nome']}
        categorias.append(nova_categoria)
        id_counter += 1
        return jsonify(nova_categoria), 201


# Caminho raiz para retornar uma mensagem de boas-vindas
@app.route('/')
def index():
    return 'Bem-vindo ao serviço REST do Supermercado!'


if __name__ == '__main__':
    app.run(debug=True)