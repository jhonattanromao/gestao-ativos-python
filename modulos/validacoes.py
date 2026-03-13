from rich.console import Console
console = Console()

def validaId(dados, id): # VALIDA SE ID JÁ EXISTE
    for ativo in dados["ativos"]:
        if ativo["id"] == id:
            return False
    return True

def validaCampoVazio(campo): # VALIDA SE O USUÁRIO DEIXOU INPUT EM BRANCO
    if not campo.strip():
        console.print("ERRO: Este campo não pode ser vazio!", style="white on red")
        return False

def validaCampoInt(campo): # VALIDA SE USUÁRIO DIGITOU UM NUMERO INTEIRO
    try:
        campo = int(campo)
        return True
    except ValueError as e:
        console.print("ERRO: Digite um número válido.", style="white on red")
        return False

def validaIndex(lista, campo): # VALIDA SE EXISTE O INDEX DE UMA LISTA
    campo = int(campo)
    if not campo in range(len(lista)):
        console.print("ERRO: Digite um número da lista.", style="white on red")
        return False
        

