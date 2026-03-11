import json, os, subprocess, sys, logging
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ARQUIVO_BASE = os.path.join(BASE_DIR, "base", "ativos.json")

# MANIPULAÇÃO JSON
def carregar_ativos(): # Lê arquivo JSON de base de dados
    if not os.path.exists(ARQUIVO_BASE):
        return {"ativos": []}  # Se não existir, retorna vazio
    
    with open(ARQUIVO_BASE, "r", encoding="utf-8") as base_json:
        return json.load(base_json)

def salvar_ativos(dados): # Salva dados no arquivo JSON
    with open(ARQUIVO_BASE, "w", encoding="utf-8") as base_json:
        json.dump(dados, base_json, indent=4, ensure_ascii=False)

dados = carregar_ativos()
setores = ("TI", "RH", "Comercial", "Financeiro", "Gerência")
status = ("Disponível", "Alocado", "Manutenção", "Inutilizado")

# FUNÇÕES DE MENU
def cadastrar_ativo(): # Coleta informações de cadastro
    global status
    global setores

    id = dados["proximo_id"]
    nome = input("Digite o nome do produto: ")

    for index, st in enumerate(status):
        print(f"[{index}] {st}")
    status = input("Digite o numero do status: ")

    for index, se in enumerate(setores):
        print(f"[{index}] {se}")
    setor = input("Digite o setor correspondente [ex: 1]: ")
    numero_serie = input("Digite o número de série: ")

def listar_ativos(): # Lista todos os ativos cadastrados
    print("N/A")

def buscar_ativo(): # Filtra ativos por ID, Nome ou Setor
    print("N/A")

def editar_ativo(): # Edita ativo cadastrado/existente
    print("N/A")

def remover_ativo(): # Remove ativo cadastrado
    print("N/A")

def alocar_ativo(): # Define uso de ativo para um setor
    print("N/A")

# dados["ativos"].append({"id": "AT-001", "nome": "Notebook", "status": "", "setor": "", "data_cadastro": "", "numero_serie": ""})
# dados["proximo_id"] += 1
# salvar_ativos(dados)

cadastrar_ativo()