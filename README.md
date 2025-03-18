# Simple Package Template
Este repositório contém um modelo básico para a criação de pacotes Python. Ele serve como ponto de partida para estruturar projetos de forma organizada e reutilizável.
Este modelo pode ser expandido para incluir múltiplos módulos e funcionalidades mais avançadas.

## Estrutura do Projeto

project_name/
│-- README.md
│-- setup.py
│-- requirements.txt
└── package_name/
    │-- __init__.py
    │-- file1_name.py
    └── file2_name.py

## Como Usar
### 1 - Clone o repositório

git clone https://github.com/ALLzyxx/image-processing-toolkit.git
cd simple-package-template

### 2 - Edite os arquivos

Renomeie project_name e package_name conforme necessário.
Adicione suas funções em file1_name.py e file2_name.py.

### 3 - Instale as dependências

pip install -r requirements.txt

### 4 - Crie o pacote

python setup.py sdist
