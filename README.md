# Conversor de Excel para CSV - Automação de Produção

Este projeto foi criado para **facilitar a conversão de arquivos Excel para CSV**, uma tarefa que antes era feita manualmente.  
O objetivo principal é transformar os arquivos para utilização na **produção da Data Extension**, garantindo rapidez, precisão e padronização no processo.

---

## 📁 Estrutura do Projeto

meu_projeto_excel_csv/
│
├── .venv/ # Ambiente virtual Python
├── app.py # Script principal do Streamlit (painel web)
├── requirements.txt # Lista de dependências
├── Planilhas/ # Pasta opcional para arquivos temporários
└── README.md # Este arquivo

---

## ⚙️ Funcionalidades

- Upload de arquivos Excel (`.xlsx`) com múltiplas abas.  
- Conversão automática de todas as abas em um único CSV pronto para a Data Extension.  
- Download do CSV gerado diretamente pelo navegador.  
- Interface web simples e intuitiva, feita com Streamlit.  

---

## 💻 Pré-requisitos

- Python 3.10 ou superior  
- Pip  
- (Opcional) Visual Studio Code ou outro editor  

---

## 📌 Instalação e Execução

1. Clone ou baixe este repositório.  
2. Navegue até a pasta do projeto no terminal.  
3. Crie e ative o ambiente virtual:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1  # Para PowerShell
