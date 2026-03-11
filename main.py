from rich import print
from rich.console import Console
import modulos.crud as crud

console = Console()
crud.carregar_ativos()

console.print("Bem-vindo ao sistema de Gestão de Ativos!\n", style="bold")
console.print("|===== Menu Principal =====|", style="bold yellow")
crud.menu_principal()