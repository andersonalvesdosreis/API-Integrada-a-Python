#pip install fastapi uvicorn
from fastapi import FastAPI
import sqlite3

conexao = sqlite3.connect('meu_projeto.txt')
cursor = conexao.cursor()

conexao.commit()
conexao.close()

print("Dados salvos com sucesso!")