from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
import modulos.crud as crud

console = Console()
crud.carregar_ativos()

titulo = Text()
titulo.append("⚙  Sistema de Gestão de Ativos\n", style="bold cyan")
titulo.append("Dev: github.com/jhonattanromao", style="dim white")

console.print()
console.print(Panel(
    Align.left(titulo),
    border_style="cyan",
    padding=(1, 2),
    width=50,
))

crud.menu_principal()