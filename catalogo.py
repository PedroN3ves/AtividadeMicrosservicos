from flask import Flask, jsonify

app = Flask(__name__)

produtos = {
    "1": {"nome": "Placa Arduino Uno", "preco": 150.00},
    "2": {"nome": "Sensor Ultrassónico HC-SR04", "preco": 25.50},
    "3": {"nome": "Sensor Ótico TCRT5000", "preco": 15.00},
    "4": {"nome": "Motor DC com Caixa de Redução", "preco": 35.00}
}

@app.route('/produtos', methods=['GET'])
def listar_produtos():
    return jsonify(produtos)

@app.route('/produtos/<id_produto>', methods=['GET'])
def obter_produto(id_produto):
    produto = produtos.get(id_produto)
    if produto:
        return jsonify(produto)
    return jsonify({"erro": "Produto não encontrado"}), 404

if __name__ == '__main__':
    app.run(port=5001)