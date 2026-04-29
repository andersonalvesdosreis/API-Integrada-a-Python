#importando os requisitos!
#No teerminal >>> pip install requests
import requests
import os
import time
print('='*30,'Seja Bem vindo a Previsão do Tempo','='*24)
#link:
link = 'http://api.weatherapi.com/v1/current.json'
#api_key:
print('Faça um cadastro no https://www.weatherapi.com/')
print('Após o Cadastro copie a sua api_key.')
print('E digite a sua api_key para que o codigo possa funcionar com sucesso!')
print('='*90)
api_key = str(input('Digite aqui sua API_Key: ')).strip()
time.sleep(1)
#limpar o terminal
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_terminal()
#Variaveis
print('='*20,'Veja quantos °C esta no seu lugar','='*20)
nome = str(input('Qual seu nome? ')).strip()
pergunta = str(input('Onde Você mora? ')).strip()
print('='*60)
#Esses são os parametros da api
parametros = {
    'key': api_key,
    'q': pergunta,
    'lang': 'pt'
}
#
resposta = requests.get(link , params=parametros)
#
if resposta.status_code == 200:
    dados_requisicao = resposta.json()
    temp = dados_requisicao["current"]["temp_c"]
#Saida de dados
print(f'Olá {nome}, A temperatura em {pergunta} está {temp}°C')
#253d131753514ed3a2b175743262904