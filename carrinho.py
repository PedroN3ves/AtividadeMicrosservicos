from flask import Flask, jsonify

app = Flask(__name__)

carrinhos = {
    "Pedro Neves": ["1", "3", "3", "4", "4"],
    "Kelvin Santos": ["2", "4"]
}

@app.route('/carrinho/<id_usuario>', methods=['GET'])
def ver_carrinho(id_usuario):
    itens = carrinhos.get(id_usuario, [])
    return jsonify({"usuario": id_usuario, "itens": itens})

if __name__ == '__main__':
    app.run(port=5002)