#!flask/bin/python
from flask import Flask, request
import requests
import json

app = Flask(__name__)

def getQuotation():
    request = requests.get('http://api.promasters.net.br/cotacao/v1/valores')
    quotation = json.loads(request.text)
    return quotation


@app.route('/cotacao/dollar/<string:dollar>', methods=['GET'])
def dollar_real(dollar):
    value = getQuotation()['valores']['USD']['valor']
    quotation = float(value)
    return str(float(dollar) * quotation)


@app.route('/cotacao/real/<string:real>', methods=['GET'])
def real_dollar(real):
    value = getQuotation()['valores']['USD']['valor']
    quotation = float(value)
    return str(float(real) / quotation)

if __name__ == '__main__':
    app.run(debug=True)
