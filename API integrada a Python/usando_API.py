import requests
import pprint
import os

link = 'http://api.weatherapi.com/v1/current.json'
api_key = '253d131753514ed3a2b175743262904'

pergunta = str(input('Onde Você mora?')).strip()

parametros = {
    'key': api_key,
    'q': pergunta,
    'lang': 'pt'
}

resposta = requests.get(link , params=parametros)

if resposta.status_code == 200:
    dados_requisicao = resposta.json()
    pprint.pprint(dados_requisicao)
    temp = dados_requisicao["current"]["temp_c"]
    descricao = dados_requisicao["current"]["conditional"]["texto"]
    print(temp)
    print(descricao)
