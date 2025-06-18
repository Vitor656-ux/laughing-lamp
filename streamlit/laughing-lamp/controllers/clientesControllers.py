import streamlit as st
import json
import os

clientes = 'data/data_clientes.json'

def carregar_clientes():
    if os.path.exists(clientes):
        with open(clientes, "r", encoding="uft-8") as arq_json:
            return json.load(arq_json)
    else:
        return []
def cadastrar_clientes(clientes):
    if not clientes:
        return "Não foi possivel cadastrar."
    else:
        with open(clientes, 'w', encoding='uft-8') as arq_json:
            json.dump(clientes, arq_json, indent=4, ensure_ascii=False)
        return 'Cadastro realizado com sucesso.'
