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
        sensacao = dados['current']['feelslike_c']
        data_completa = dados["location"]["localtime"]
        data, hora = data_completa.split(' ')
        
        print('\n' + '='*40)
        print(f'Olá, {nome}!')
        print(f'Em {cidade}, o tempo está: {condicao}')
        print(f'A temperatura atual é de {temp}°C')
        print(f'Mesmo a temperatura sendo {temp}°C a sensação termica é {sensacao}')
        print(f'Hoje é dia {data}')
        print(f'O horário em {cidade} é {hora}')
        print('='*40)
    else:
        print(f'\n[ERRO] Não conseguimos encontrar a cidade "{cidade}". Verifique sua chave ou o nome do lugar.')

except Exception as e:
    print(f'Ocorreu um erro de conexão: {e}')
while True:
    pergunta = str(input(f'Me fale {nome}, Você esta sentindo que está calor ou frio? ')).strip().lower()
    if pergunta in 'calor,quente':
        print(f'Nossa {nome} e nesse calor seria bom mesmo um açai né?')
        pergunta011 = str(input(f'Você gosta de açai {nome}? ')).strip().lower()
        if pergunta011 in 'sim,ss,s,simm':
            print('Que legal!')
            break
        else:
            print('Ah que pena')
            break
    elif pergunta in 'frio,gelado':
        print(f'Nossa {nome} em um frio desse seria uma boa um chocolate quente né?')
        pergunta021 = str(input('Você gosta de chocolate quente? ')).strip().lower()
        if pergunta021 in 'sim,ss,s,simm':
            print('Que legal!')
            break
        else:
            print('Ah que pena')
            break
    else:
        print(f'{nome} não consegui entender oque você quis falar, pode repetir?')
        continue
#print(resposta.json())