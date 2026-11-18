# Documento de Requisitos — TecRegistro

## 1. Apresentação

O TecRegistro é um sistema web desenvolvido para apoiar a organização dos atendimentos técnicos da LF Segurança Eletrônica.

O projeto busca substituir registros informais, realizados principalmente por mensagens de WhatsApp, por um sistema centralizado, permitindo maior organização das informações sobre serviços e materiais.

## 2. Problema identificado

A comunicação informal dos atendimentos pode dificultar a localização de informações, o acompanhamento dos serviços e o controle dos materiais utilizados ou danificados.

## 3. Objetivo geral

Desenvolver um sistema para registrar, organizar e consultar atendimentos técnicos e seus respectivos materiais.

## 4. Público-alvo

- Equipe administrativa da LF Segurança Eletrônica.
- Técnicos responsáveis pelos atendimentos.
- Responsáveis pelo acompanhamento dos serviços.

## 5. Requisitos funcionais

### RF01 — Autenticação

O sistema deve permitir o acesso de usuários autorizados.

### RF02 — Cadastro de atendimentos

O sistema deve permitir o registro de:

- Cliente atendido.
- Técnico responsável.
- Data do atendimento.
- Descrição do serviço.
- Status do atendimento.

### RF03 — Controle de materiais

O sistema deve permitir o registro dos materiais associados aos atendimentos, incluindo:

- Nome do material.
- Quantidade utilizada.
- Quantidade danificada.
- Motivo do dano, quando aplicável.

### RF04 — Consulta de atendimentos

O sistema deve permitir a consulta dos registros para facilitar o acompanhamento administrativo.

### RF05 — Registro de localização

Funcionalidade prevista para versões futuras, mediante consentimento e avaliação das necessidades dos usuários.

## 6. Requisitos não funcionais

### RNF01 — Tecnologia

O sistema deve utilizar Python e Django.

### RNF02 — Persistência de dados

Os registros devem ser armazenados em banco de dados relacional.

### RNF03 — Organização

O código deve seguir uma estrutura que facilite a manutenção e a evolução do projeto.

### RNF04 — Segurança

O acesso às funcionalidades administrativas deve ser restrito a usuários autenticados e autorizados.

### RNF05 — Usabilidade

As funcionalidades devem ser organizadas de forma clara para facilitar o trabalho administrativo.

## 7. Tecnologias utilizadas

- Python 3.12.
- Django 5.2.
- SQLite para desenvolvimento.
- Git para controle de versões.
- GitHub para hospedagem do código-fonte.

## 8. Funcionalidades da versão atual

A versão acadêmica utiliza o Django Admin para realizar o cadastro e a consulta de atendimentos e materiais.

A interface exclusiva para técnicos ainda não foi implementada.

## 9. Melhorias futuras

- Desenvolver uma interface específica para técnicos.
- Melhorar os filtros de consulta.
- Ampliar os relatórios administrativos.
- Implementar testes automatizados.
- Configurar integração contínua.
- Avaliar funcionalidades de localização com consentimento.

## 10. Considerações finais

A documentação dos requisitos orienta a evolução do TecRegistro e permite acompanhar quais funcionalidades estão disponíveis e quais permanecem planejadas.
