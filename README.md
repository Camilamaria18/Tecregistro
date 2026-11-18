# TecRegistro

## Sobre o projeto

O **TecRegistro** é um sistema web desenvolvido em Python e Django para auxiliar a **LF Segurança Eletrônica** no gerenciamento de atendimentos técnicos.

O projeto surgiu da necessidade de organizar as informações dos serviços realizados pelos técnicos, que anteriormente eram comunicadas de maneira informal, principalmente pelo WhatsApp.

O objetivo é facilitar o registro, a organização e a consulta dos atendimentos, incluindo os materiais utilizados e danificados durante os serviços.

## Objetivos

- Centralizar as informações dos atendimentos técnicos.
- Facilitar o registro dos serviços realizados.
- Organizar os materiais utilizados e danificados.
- Melhorar a consulta dos históricos de atendimento.
- Apoiar o trabalho administrativo da empresa.

## Tecnologias utilizadas

- **Python:** linguagem de programação.
- **Django:** framework para desenvolvimento web.
- **SQLite:** banco de dados utilizado no desenvolvimento.
- **HTML:** estrutura das interfaces planejadas.
- **Git:** controle de versões.
- **GitHub:** armazenamento e acompanhamento do código-fonte.

## Funcionalidades implementadas

### Cadastro de atendimentos

Registro das informações dos atendimentos técnicos, incluindo cliente, técnico responsável, data, descrição e status.

### Controle de materiais

Registro dos materiais utilizados nos atendimentos, incluindo quantidades utilizadas e danificadas.

### Painel administrativo

Utilização do Django Admin para cadastrar, consultar e gerenciar os registros do sistema.

## Estrutura do projeto

- `atendimentos/` — aplicação responsável pelos registros de atendimentos e materiais.
- `config/` — configurações principais do Django.
- `manage.py` — gerenciamento e execução do projeto.
- `.gitignore` — definição dos arquivos que não devem ser enviados ao repositório.
- `README.md` — documentação do projeto.

## Como executar o projeto

### 1. Requisitos

- Python 3.12
- Django 5.2
- Git

### 2. Baixar o projeto

```bash
git clone https://github.com/Camilamaria18/Tecregistro.git
```

### 3. Acessar a pasta

```bash
cd Tecregistro
```

### 4. Instalar o Django

```bash
python -m pip install "Django==5.2"
```

### 5. Preparar o banco de dados

```bash
python manage.py migrate
```

### 6. Iniciar o servidor

```bash
python manage.py runserver 8001
```

### 7. Acessar o sistema

Abra o navegador e acesse:

http://127.0.0.1:8001/admin/

Para acessar o painel administrativo, utilize uma conta de administrador previamente criada.

Caso seja necessário criar uma conta, execute:

```bash
python manage.py createsuperuser
```

## Controle de versão

O código-fonte é gerenciado com Git e disponibilizado no GitHub. O histórico de commits permite acompanhar as alterações realizadas durante o desenvolvimento.

## Melhorias futuras

- Desenvolvimento de uma interface específica para os técnicos.
- Ampliação dos recursos de consulta.
- Implementação de testes automatizados.
- Configuração de integração contínua.
- Aprimoramento da experiência dos usuários.

## Status do projeto

**Protótipo acadêmico em desenvolvimento.**

A versão atual permite o gerenciamento básico de atendimentos e materiais por meio do painel administrativo do Django.

## Projeto acadêmico

Desenvolvido para a atividade **Projeto de Software – Experiência Prática 3**, com foco na implementação de software, controle de versão, testes e validação de soluções tecnológicas.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f3170299-528b-41dd-ba09-e3eff485df67" />

