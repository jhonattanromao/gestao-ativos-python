import json, os, subprocess, sys, logging
from datetime import datetime
from rich import print
from rich.console import Console
import modulos.validacoes as validacoes

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ARQUIVO_BASE = os.path.join(BASE_DIR, "base", "ativos.json") # Arquivo de base de dados (JSON)
ARQUIVO_LOG = os.path.join(BASE_DIR, "base", "logs.log") # Arquivo de base de dados (JSON)
console = Console() # Instância Rich para estilização

# Configuração de Log utilizando módulo Logging
logging.basicConfig(
    filename=ARQUIVO_LOG,
    level=logging.INFO,
    format="%(asctime)s — %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
    encoding="utf-8"
)

def registrar_log(mensagem):
    logging.info(mensagem)

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
setores = ("TI", "RH", "Comercial", "Financeiro")
lista_status = ("Disponível", "Alocado", "Manutenção", "Inutilizado")

# FUNÇÕES DE MENU
def cadastrar_ativo(): # Coleta e cadastra informações do ativo
    global lista_status
    global setores

    id = dados["proximo_id"]
    if validacoes.validaId(dados, id) == False:
        console.print("ERRO: Este ID já está cadastrado!", style="white on red")
        return

    while True:
        nome = input("Digite o nome do produto: ").strip()
        if validacoes.validaCampoVazio(nome) == False:
            continue
        else:
            break

    for index, st in enumerate(lista_status):
        print(f"[{index}] {st}")

    while True:
        status = input("Defina o status: ").strip()
        if validacoes.validaCampoVazio(status) == False or validacoes.validaCampoInt(status) == False or validacoes.validaIndex(lista_status, status) == False:
            continue
        else:
            status = int(status)
            break

    for index, se in enumerate(setores):
        print(f"[{index}] {se}")

    while True:
        setor = input("Digite o setor: ").strip()
        if validacoes.validaCampoVazio(setor) == False or validacoes.validaCampoInt(setor) == False or validacoes.validaIndex(setores, status) == False:
            continue
        else:
            setor = int(setor)
            break

    while True:
        numero_serie = input("Digite o número de série: ").strip().upper()

        if validacoes.validaCampoVazio(numero_serie) == False:
            continue
        else:
            break

    data_cadastro = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    try:
        dados["ativos"].append({"id": id, "nome": nome, "status": lista_status[status], "setor": setores[setor], "data_cadastro": data_cadastro, "numero_serie": numero_serie})
        dados["proximo_id"] += 1
        salvar_ativos(dados)
        registrar_log(f"[CADASTRO] {id} - {nome}")
        console.print(f"Produto cadastrado com sucesso!", style="bold white on green")
    except Exception as e:
        registrar_log(f"[ERRO] {e}")
        console.print(f"ERRO: {e}", style="white on red")

def listar_ativos(): # Lista todos os ativos cadastrados
    if not dados["ativos"]:
        console.print("Nenhum produto cadastrado.", style="bold white on yellow")

    try:
        for produto in dados["ativos"]:
            console.print(f"[green bold]ID: [/green bold]{produto["id"]}")
            console.print(f"[green bold]Nome: [/green bold]{produto["nome"]}")
            console.print(f"[green bold]Status: [/green bold]{produto["status"]}")
            console.print(f"[green bold]Setor: [/green bold]{produto["setor"]}")
            console.print(f"[green bold]Número de Série: [/green bold]{produto["numero_serie"]}")
            console.print(f"[green bold]Criado em: [/green bold]{produto["data_cadastro"]}")
            console.print("==========")
    except Exception as e:
        console.print(f"ERRO: {e}", style="white on red")

def buscar_ativo(): # Filtra ativos por ID
    while True:
        busca = input("Digite o ID do produto: ").strip()
        if validacoes.validaCampoVazio(busca) == False or validacoes.validaCampoInt(busca) == False:
            continue
        else:
            busca = int(busca)
            break
    try:
        for ativo in dados["ativos"]:
            if ativo["id"] == busca:
                console.print(f"[green bold]ID: [/green bold]{ativo["id"]}")
                console.print(f"[green bold]Nome: [/green bold]{ativo["nome"]}")
                console.print(f"[green bold]Status: [/green bold]{ativo["status"]}")
                console.print(f"[green bold]Setor: [/green bold]{ativo["setor"]}")
                console.print(f"[green bold]Número de Série: [/green bold]{ativo["numero_serie"]}")
                console.print(f"[green bold]Criado em: [/green bold]{ativo["data_cadastro"]}")
                break
        else:
            console.print("Nenhum produto encontrado.", style="bold white on yellow")
    except Exception as e:  
        console.print(f"ERRO: {e}", style="white on red")

def editar_ativo(): # Edita ativo cadastrado/existente
    global lista_status
    global setores

    while True:
        busca = input("Digite o ID do produto: ").strip()
        if validacoes.validaCampoVazio(busca) == False or validacoes.validaCampoInt(busca) == False:
            continue
        else:
            busca = int(busca)
            break
        
    for ativo in dados["ativos"]:
        if ativo["id"] == busca:
            id = ativo["id"]
            nome = ativo["nome"]
            status = ativo["status"]
            setor = ativo["setor"]
            numero_serie = ativo["numero_serie"]

            console.print(f"[bold magenta]Nome Atual:[/bold magenta] {nome}")
            nome = input("Digite o novo nome: ").strip() or nome

            console.print(f"[bold magenta]Status Atual:[/bold magenta] {status}")
            for index, st in enumerate(lista_status):
                print(f"[{index}] {st}", end=" | ")
            while True:
                status = input("\nDigite o novo status: ")

                if validacoes.validaCampoInt(status) == False or validacoes.validaIndex(lista_status, status) == False:
                    continue
                else:
                    status = int(status)
                    break

            console.print(f"[bold magenta]Setor Atual:[/bold magenta] {setor}")
            for index, se in enumerate(setores):
                print(f"[{index}] {se}", end=" | ")
            while True:
                setor = input("\nDigite o novo setor: ")

                if validacoes.validaCampoInt(setor) == False or validacoes.validaIndex(setores, status) == False:
                    continue
                else:
                    setor = int(setor)
                    break

            console.print(f"[bold magenta]Nº de Série Atual:[/bold magenta] {numero_serie}")
            numero_serie = input("Digite o novo Nº de Série: ") or numero_serie

            try:
                ativo.update({"id": id, "nome": nome, "status": lista_status[status], "setor": setores[setor], "numero_serie": numero_serie})
                salvar_ativos(dados)
                registrar_log(f"[EDITADO] {id} - {nome}")
                console.print(f"Alterações salvas com sucesso!", style="bold white on green")
                break
            except Exception as e:
                registrar_log(f"[ERRO] {e}")
                console.print(f"ERRO: Não foi possível salvar as alterações", style="white on red")
                console.print(f"ERRO: {e}", style="white on red")
    else:
        console.print("Nenhum produto encontrado.", style="bold white on yellow")

def remover_ativo(): # Remove ativo cadastrado
    while True:
        busca = input("Digite o ID do produto: ").strip()
        if validacoes.validaCampoVazio(busca) == False or validacoes.validaCampoInt(busca) == False:
            continue
        else:
            busca = int(busca)
            break

    for ativo in dados["ativos"]:
        if ativo["id"] == busca:
            console.print(f"[green bold]ID: [/green bold]{ativo["id"]}")
            console.print(f"[green bold]Nome: [/green bold]{ativo["nome"]}")
            console.print(f"[green bold]Status: [/green bold]{ativo["status"]}")
            console.print(f"[green bold]Setor: [/green bold]{ativo["setor"]}")
            console.print(f"[green bold]Número de Série: [/green bold]{ativo["numero_serie"]}")
            console.print(f"[green bold]Criado em: [/green bold]{ativo["data_cadastro"]}")
            console.print("==========")
            
            while True:
                confirma = input("Confirmar exclusão de produto? [S/N]: ").upper()

                if validacoes.validaCampoVazio(confirma) == False:
                    continue

                if confirma == "S":
                    try:
                        dados["ativos"].remove(ativo)
                        salvar_ativos(dados)
                        registrar_log(f"[EXCLUÍDO] {ativo["id"]} - {ativo["nome"]}")
                        console.print(f"Ativo excluído com sucesso!", style="bold white on green")
                        break
                    except Exception as e:
                        registrar_log(f"[ERRO] {e}")
                        console.print(f"ERRO: {e}", style="white on red")
                break
            break
    else:
        console.print("Nenhum produto encontrado.", style="bold white on yellow")

def abrir_dashboard():
    subprocess.Popen(
        [sys.executable, "-m", "streamlit", "run", 
         os.path.join(BASE_DIR, "relatorios", "streamlit.py")],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    console.print("Dashboard aberto no navegador!", style="bold white on green")

def menu_principal(): # Exibe menu principal do programa
    while True:
        console.print("\n[1] Cadastrar Novo Ativo")
        console.print("[2] Listar Todos os Ativos")
        console.print("[3] Buscar Ativo por ID")
        console.print("[4] Editar Ativo")
        console.print("[5] Excluir Ativo")
        console.print("[6] Abrir Dashboard")
        console.print("[0] Sair\n")

        opcao = input("Digite uma opção do menu: ")
        if validacoes.validaCampoInt(opcao) == False:
            continue
        else:
            opcao = int(opcao)

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
            abrir_dashboard()
        elif opcao == 0:
            break
        else:
            console.print("Opção inválida")