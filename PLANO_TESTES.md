# Plano de Testes — TecRegistro

## 1. Introdução

Este documento apresenta o planejamento de testes do sistema TecRegistro, desenvolvido para apoiar o gerenciamento de atendimentos técnicos e materiais da LF Segurança Eletrônica.

## 2. Objetivo

Definir cenários de teste para verificar o funcionamento das principais funcionalidades do sistema e orientar futuras atividades de validação.

## 3. Ambiente de desenvolvimento

- Linguagem: Python 3.12.
- Framework: Django 5.2.
- Banco de dados: SQLite.
- Ambiente de desenvolvimento: PyCharm.
- Controle de versão: Git e GitHub.
- Interface administrativa: Django Admin.

## 4. Escopo dos testes

Os testes deverão abranger:

- Autenticação de usuários.
- Cadastro de atendimentos.
- Consulta de atendimentos.
- Associação de materiais aos serviços.
- Registro de materiais danificados.
- Integridade dos dados armazenados.

## 5. Casos de teste planejados

| Código | Cenário | Resultado esperado |
|---|---|---|
| CT01 | Acessar o painel administrativo sem autenticação | Redirecionamento para a página de login |
| CT02 | Acessar o painel com administrador autorizado | Acesso permitido |
| CT03 | Cadastrar um atendimento com informações válidas | Atendimento salvo no banco de dados |
| CT04 | Consultar um atendimento cadastrado | Registro apresentado no painel |
| CT05 | Associar um material a um atendimento | Material vinculado ao atendimento correto |
| CT06 | Registrar quantidade de material utilizada | Quantidade armazenada corretamente |
| CT07 | Registrar quantidade de material danificada | Quantidade armazenada corretamente |
| CT08 | Alterar o status de um atendimento | Novo status salvo corretamente |
| CT09 | Consultar registros utilizando os filtros administrativos | Exibição dos registros correspondentes |
| CT10 | Registrar informações obrigatórias incompletas | Aplicação das validações configuradas no sistema |

## 6. Testes unitários

Os testes unitários deverão verificar o comportamento individual dos modelos e das regras de validação.

Exemplos:

- Criação de registros de atendimento.
- Associação de materiais aos atendimentos.
- Armazenamento das quantidades utilizadas.
- Armazenamento das quantidades danificadas.

## 7. Testes de integração

Os testes de integração deverão verificar o funcionamento conjunto dos componentes do sistema.

Exemplos:

- Cadastro de atendimento e persistência no banco de dados.
- Associação de materiais a atendimentos existentes.
- Consulta dos registros pelo painel administrativo.

## 8. Automação de testes

O Django oferece uma estrutura de testes que pode ser executada pelo comando:

```bash
python manage.py test
```

A execução automática deverá ser configurada futuramente no GitHub Actions para verificar alterações enviadas ao repositório.

## 9. Critérios de aceitação

Os testes serão considerados aprovados quando:

- O resultado obtido corresponder ao resultado esperado.
- Os dados forem armazenados corretamente.
- As relações entre atendimentos e materiais forem preservadas.
- As funcionalidades administrativas respeitarem as permissões configuradas.

## 10. Registro de evidências

As evidências dos testes deverão incluir:

- Data de execução.
- Cenário avaliado.
- Resultado obtido.
- Situação de aprovação ou falha.
- Capturas de tela ou registros do terminal, quando aplicável.

## 11. Situação atual

Este documento registra o **planejamento dos testes**.

A implementação dos testes automatizados, a execução dos cenários e a configuração do GitHub Actions são atividades posteriores e não são consideradas concluídas apenas pela criação deste documento.

## 12. Considerações finais

O planejamento de testes contribui para a qualidade do TecRegistro, permitindo identificar problemas, orientar correções e acompanhar a evolução do sistema.
