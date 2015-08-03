Barganhou
=========
Aplicativo para cat�logo e compara��o de pre�os

Objetivos
---------
* Fazer registro de pre�os de produtos
* Manter estat�sticas da m�dia e vari�ncia desses pre�os
* Fazer previs�o de gastos em compras

Divis�o do projeto
------------------
* Classe para intera��o com o banco de dados
* Classe para c�lculos estat�sticos
* Classe para interface com usu�rio (comandos)
* Classe para interface gr�fica
* Classe para testes

Diretivas
---------------------------
Para o projeto ser�o utilizados:
* Linguagem Python 3
* Django
* AngularJS
* Mysql
* Reposit�rio no GitHub

A seguir est�o os principais comandos do git a serem execultados no terminal.

**Principais comandos do github**

Copia reposit�rio para o diret�rio local
> git clone https://github.com/geans/barganhou

Para verificar arquivos alterados e adicionados ou n�o no Stage
> git status

Adicionando diret�rios ou arquivos novos ou modificados no Stage
> git add arquivo.txt

Remove arquivos no Stage
> git rm arquivo.txt

Remove diret�rio (e seu conte�do)
> git rm -r diret�rio

Remove arquivos que j� foram adicionados para commit
> git rm --cached arquivo.txt

Apenas arquivos no Stage podem ser commitados (o primeiro comando abrir� o editor padr�o para escrita da mensagem)
> git commit
> git commit -m "Mensagem"

Para mandar os arquivos "commitados" para o reposit�rio, ser� pedido usu�rio e senha
> git push

Atualizar c�pia do reposit�rio
> git pull

Ambiente de Desenvolvimento
---------------------------


Caracter�sticas do projeto
--------------------------
* Interface web para ades�o de inst�ncia no banco de dados atrav�s de um formul�rio