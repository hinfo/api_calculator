"""API"""
# *-* coding:utf-8 -*-
from flask import Flask
from flask import jsonify
from flask import request
from flask_swagger import swagger

app = Flask(__name__)


#  = "/api/components/schemas"


class Messages():
    EMPTY = "Dados vazios"
    NONE = "Resultado não encontrado!"
    CREATED = "Criado com sucesso!"
    UPDATED = "Atualizado com sucesso!"
    DELETED = "Removido com sucesso!"


@app.route("/spec")
def spec():
    """Interface para o swagger"""
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "API Calculator"
    return jsonify(swag)


@app.route("/")
def home():
    """Home"""
    return "API Calculator"


@app.route("/soma/<numero_1>/<numero_2>", methods=['GET'])
def get_soma(numero_1, numero_2):
    """Soma dois numeros"""
    response = int(numero_1) + int(numero_2)
    return jsonify({'resultado': response})


if __name__ == '__main__':
    app.run(port=5000, debug=True,
            host="0.0.0.0")
