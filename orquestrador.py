import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/resumo_compra/<id_usuario>', methods=['GET'])
def resumo_compra(id_usuario):
    try:
        resp_carrinho = requests.get(f'http://127.0.0.1:5002/carrinho/{id_usuario}')
        if resp_carrinho.status_code != 200:
            return jsonify({"erro": "Falha na comunicação com o serviço de carrinho"}), 500
    except requests.exceptions.ConnectionError:
        return jsonify({"erro": "Serviço de carrinho em baixo"}), 503
        
    carrinho = resp_carrinho.json()
    itens_ids = carrinho.get("itens", [])
    
    if not itens_ids:
        return jsonify({"mensagem": "O carrinho está vazio", "valor_total": 0.0}), 200

    total = 0.0
    detalhes_itens = []
    
    for item_id in itens_ids:
        try:
            resp_produto = requests.get(f'http://127.0.0.1:5001/produtos/{item_id}')
            if resp_produto.status_code == 200:
                produto = resp_produto.json()
                detalhes_itens.append(produto)
                total += produto['preco']
            else:
                detalhes_itens.append({"id": item_id, "erro": "Produto não encontrado"})
        except requests.exceptions.ConnectionError:
            return jsonify({"erro": "Serviço de catálogo em baixo"}), 503

    return jsonify({
        "usuario": id_usuario,
        "detalhes_compra": detalhes_itens,
        "valor_total": round(total, 2)
    })

if __name__ == '__main__':
    app.run(port=5000)