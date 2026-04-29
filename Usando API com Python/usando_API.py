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
cidade = str(input('Onde Você mora? ')).strip()
#Esses são os parametros da api
parametros = {
    'key': api_key,
    'q': cidade,
    'lang': 'pt'
}
try:
    resposta = requests.get(link, params=parametros)
    # Verifica se a requisição foi bem sucedida
    if resposta.status_code == 200:
        dados = resposta.json()
        temp = dados["current"]["temp_c"]
        condicao = dados["current"]["condition"]["text"]
        data_completa = dados["location"]["localtime"]
        data, hora = data_completa.split(' ')
        
        print('\n' + '='*40)
        print(f'Olá, {nome}!')
        print(f'Em {cidade}, o tempo está: {condicao}')
        print(f'A temperatura atual é de {temp}°C')
        print(f'Hoje é dia {data}')
        print(f'O horário em {cidade} é {hora}')
        print('='*40)
    else:
        print(f'\n[ERRO] Não conseguimos encontrar a cidade "{cidade}". Verifique sua chave ou o nome do lugar.')

except Exception as e:
    print(f'Ocorreu um erro de conexão: {e}')
#253d131753514ed3a2b175743262904
print(resposta.json())