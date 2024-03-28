# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from main import get_ofertas_do_dia

app = Flask(__name__)

@app.route('/ofertas-do-dia', methods=['GET'])
def ofertas_do_dia():
    ofertas = get_ofertas_do_dia()
    if ofertas:
        return jsonify(ofertas)
    else:
        return jsonify({'error': 'Falha ao obter ofertas do Mercado Livre'}), 500

@app.route('/produto/<int:id>', methods=['GET'])
def get_produto(id):
    # Implementação da nova rota
    ofertas_do_dia = get_ofertas_do_dia()
    # Procura o produto na lista de ofertas pelo ID fornecido
    for oferta in ofertas_do_dia:
        if oferta['id'] == id:
            return jsonify(oferta)

    # Se o produto não for encontrado, retorna uma mensagem de erro
    return jsonify({'error': 'Produto não encontrado'}), 404

#if __name__ == '__main__':
#    app.run(debug=True)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
