import json, os, subprocess, sys, logging
from datetime import datetime
from rich import print
from rich.console import Console

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ARQUIVO_BASE = os.path.join(BASE_DIR, "base", "ativos.json")
console = Console()

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
lista_status = ("Disponível", "Alocado", "Manutenção", "Inutilizado")

# FUNÇÕES DE MENU
def cadastrar_ativo(): # Coleta e cadastra informações do ativo
    global lista_status
    global setores

    id = dados["proximo_id"]
    nome = input("Digite o nome do produto: ").strip()

    for index, st in enumerate(lista_status):
        print(f"[{index}] {st}")
    status = int(input("Digite o numero do status: ").strip())

    for index, se in enumerate(setores):
        print(f"[{index}] {se}")
    setor = int(input("Digite o setor correspondente [ex: 1]: ").strip())

    numero_serie = input("Digite o número de série: ").strip().upper()
    data_cadastro = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    dados["ativos"].append({"id": id, "nome": nome, "status": lista_status[status], "setor": setores[setor], "data_cadastro": data_cadastro, "numero_serie": numero_serie})
    dados["proximo_id"] += 1

    salvar_ativos(dados)

def listar_ativos(): # Lista todos os ativos cadastrados
    for produto in dados["ativos"]:
        print(f"ID: {produto["id"]}")
        print(f"Nome: {produto["nome"]}")
        print(f"Status: {produto["status"]}")
        print(f"Setor: {produto["setor"]}")
        print(f"Número de Série: {produto["numero_serie"]}")
        print(f"Criado em: {produto["data_cadastro"]}")
        print("==========")

def buscar_ativo(): # Filtra ativos por ID
    busca = int(input("Digite o ID do produto: ").strip())

    for ativo in dados["ativos"]:
        if ativo["id"] == busca:
            print(f"ID: {ativo["id"]}")
            print(f"Nome: {ativo["nome"]}")
            print(f"Status: {ativo["status"]}")
            print(f"Setor: {ativo["setor"]}")
            print(f"Número de Série: {ativo["numero_serie"]}")
            print(f"Criado em: {ativo["data_cadastro"]}")

def editar_ativo(): # Edita ativo cadastrado/existente
    print("N/A")

def remover_ativo(): # Remove ativo cadastrado
    print("N/A")

def alocar_ativo(): # Define uso de ativo para um setor
    print("N/A")

def menu_principal():
    while True:
        console.print("[1] Cadastrar novo ativo")
        console.print("[2] Listar todos os ativos")
        console.print("[3] Buscar ativo por ID")
        console.print("[4] Editar ativo")
        console.print("[5] Excluir Ativo")
        console.print("[6] Abrir dashboard")
        console.print("[0] Sair\n")

        opcao = int(input("Digite uma opção do menu: "))

        if opcao == 1:
            cadastrar_ativo()
        elif opcao == 2:
            listar_ativos()
        elif opcao == 3:
            buscar_ativo()
        elif opcao == 4:
            editar_ativo()
        elif opcao == 5:
            remover_ativo()
        elif opcao == 6:
            print("N/A")
        elif opcao == 0:
            break
        else:
            console.print("Opção inválida")

# dados["ativos"].append({"id": "AT-001", "nome": "Notebook", "status": "", "setor": "", "data_cadastro": "", "numero_serie": ""})
# dados["proximo_id"] += 1
# salvar_ativos(dados)

