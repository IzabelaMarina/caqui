## Caqui: Monitoramento de Voos
Website para sistema de monitoramento de status de voos escrito em Django.

Projeto da disciplina PCS3643 - Laboratório de Engenharia de Software I de 2022 da Escola Politécnica da USP desenvolvido por:
  * Izabela Marina F. da Silva - 11808092
  * Lucas Carvalho Ramos - 10693382
  * Nícolas Varela Auler - 11819900

## Visão Geral
Essa aplicação implementa um sistema de monitoramento de vôos, com controle de segurança baseado em logins e permissões de usuários e atualização de status baseada em inputs dos administradores.

Atualmente não há nenhuma funcionalidade implementada no site além de mensagens padrões nas páginas iniciais.

## Passos Iniciais
Para rodar esse projeto no seu computador:
1.  Inicialize um [ambiente virtual](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment) em Python.
2.  Rode os comandos (se estiver no Windows você deve usar  ```py``` ou ```py-3``` em vez de ```python3``` para iniciar o Python):
```
pip3 install -r requirements.txt
python3 manage.py runserver
```
3. Abra a url ```http://127.0.0.1:8000/admin/``` em um navegador da sua preferência para abrir a tela de admnistração.
4. Abra a url ```http://127.0.0.1:8000``` para abrir a página inicial.
5. Abra a url ```http://127.0.0.1:8000/flight``` para abrir a página de gerenciamento de voos.
6. Abra a url ```http://127.0.0.1:8000/report``` para abrir a página de geração de relatórios.
