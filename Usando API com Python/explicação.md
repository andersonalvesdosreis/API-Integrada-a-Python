# 🌤️ Previsão do Tempo Interativa em Python

Um script em Python divertido e interativo que consome dados da [WeatherAPI](https://www.weatherapi.com/) para mostrar a previsão do tempo em tempo real, além de interagir com o usuário com base no clima atual!

## 🚀 Funcionalidades

* **Integração com API:** Conecta-se à WeatherAPI para buscar dados climáticos precisos de qualquer cidade do mundo.
* **Dados Detalhados:** Exibe a temperatura atual, condição do clima (ex: Ensolarado, Chuvoso), sensação térmica, data e hora local da cidade pesquisada.
* **Tratamento de Erros (Try/Except):** O programa é seguro e não "quebra" se o usuário digitar uma cidade inexistente ou se houver problemas de conexão com a internet.
* **Chat Interativo:** Após exibir a previsão, o programa conversa com o usuário perguntando se ele está com calor ou frio, oferecendo sugestões divertidas (como Açaí ou Chocolate Quente).

## 🛠️ Tecnologias e Bibliotecas Utilizadas

* **Python 3**
* **Biblioteca `requests`:** Para fazer as requisições HTTP (comunicação com a API).
* **Biblioteca `os`:** Para limpar o terminal e deixar a interface de texto mais limpa.
* **Biblioteca `time`:** Para criar pausas (delays) na execução, melhorando a leitura do usuário.

## 📖 Como o código funciona (Passo a Passo)

1. **Configuração e Limpeza:** O programa começa importando as bibliotecas necessárias, pedindo a API Key do usuário e limpando a tela do terminal para uma melhor experiência visual.
2. **Coleta de Dados (Inputs):** O sistema solicita o nome do usuário e a cidade onde ele mora.
3. **Requisição à API:** Utilizando o método `requests.get()`, enviamos um dicionário de parâmetros (`params`) contendo a chave da API, a cidade pesquisada e o idioma desejado (`pt`).
4. **Manipulação do JSON:** Se a resposta do servidor for bem-sucedida (Status Code 200), o código converte o JSON recebido em um dicionário Python. A partir daí, navegamos pelas "chaves" (como `['current']['temp_c']` e `['location']['localtime']`) para extrair as informações exatas.
5. **Formatação de Strings:** Usamos o método `.split(' ')` para separar a string de data e hora que vem junta da API, permitindo exibi-las em linhas diferentes.
6. **Loop de Interação (While True):** No final, um loop infinito é iniciado para conversar com o usuário. Ele usa condicionais (`if/elif/else`) para ler respostas como "calor" ou "frio" e sugerir lanches adequados, quebrando o loop (`break`) apenas quando a conversa termina.

## 💻 Como executar na sua máquina

1. Certifique-se de ter o Python instalado.
2. Instale a biblioteca requests abrindo o terminal e digitando:
   `pip install requests`
3. Crie uma conta gratuita no site [WeatherAPI](https://www.weatherapi.com/) para gerar a sua API Key.
4. Execute o script, cole sua API Key quando solicitado e divirta-se!