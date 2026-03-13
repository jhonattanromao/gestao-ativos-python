# ⚙️ Sistema de Gestão de Ativos

> Aplicação CLI para gerenciamento de ativos corporativos com dashboard interativo.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Rich](https://img.shields.io/badge/Rich-CLI-blueviolet)
![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-ff4b4b?logo=streamlit&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

---

## 📌 Sobre o Projeto

Este é um sistema de gestão de ativos de TI desenvolvido em Python, com interface de terminal estilizada utilizando Rich e dashboard visual simples com Streamlit. Permite cadastrar, listar, buscar, editar e remover ativos corporativos, com salvamento em arquivo JSON e registro de logs automático utilizando o módulo Logging.

Projeto desenvolvido como exercício prático de lógica, estruturação de código e uso de bibliotecas Python.

---

## 🚀 Funcionalidades

- ✅ Cadastro de ativos com validação de campos
- ✅ Listagem completa de ativos
- ✅ Busca por ID
- ✅ Edição de ativos existentes
- ✅ Exclusão com confirmação
- ✅ Dashboard interativo com gráficos (Streamlit + Pandas)
- ✅ Registro de logs com data e hora
- ✅ Salvamento de dados em JSON

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Uso |
|---|---|
| Python 3.12 | Linguagem principal |
| Rich | Interface estilizada no terminal |
| Streamlit | Dashboard visual no navegador |
| Pandas | Manipulação de dados para relatórios |
| Logging | Registro de logs do sistema |
| JSON | Salvamento de dados |

---

## 📁 Estrutura do Projeto

```
sistema-gestao-ativos/
│
├── base/
│   ├── ativos.json         # Base de dados
│   └── logs.log            # Registro de logs
│
├── modulos/
│   ├── crud.py             # Funções principais
│   └── validacoes.py       # Validações de entrada
│
├── relatorios/
│   └── streamlit.py        # Dashboard interativo
│
├── main.py                 # Arquivo de inicialização
└── requirements.txt
```

---

## ⚙️ Como Executar

**1. Clone o repositório**
```bash
git clone https://github.com/jhonattanromao/sistema-gestao-ativos.git
cd sistema-gestao-ativos
```

**2. Instale as dependências**
```bash
pip install -r requirements.txt
```

**3. Execute o programa**
```bash
python main.py
```

> O dashboard abre automaticamente no navegador ao selecionar a opção **[6] Abrir Dashboard** no menu.

---

## 📷 Preview

> *Adicione aqui prints do terminal e do dashboard para deixar o README mais visual.*

---

## 👨‍💻 Autor

Desenvolvido por **Jhonattan Romao**  
[![GitHub](https://img.shields.io/badge/GitHub-jhonattanromao-181717?logo=github)](https://github.com/jhonattanromao)