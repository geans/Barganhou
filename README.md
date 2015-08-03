Barganhou
=========
Aplicativo para catálogo e comparação de preços

Objetivos
---------
* Fazer registro de preços de produtos
* Manter estatísticas da média e variância desses preços
* Fazer previsão de gastos em compras

Divisão do projeto
------------------
* Classe para interação com o banco de dados
* Classe para cálculos estatísticos
* Classe para interface com usuário (comandos)
* Classe para interface gráfica
* Classe para testes

Diretivas
---------------------------
Para o projeto serão utilizados:
* Linguagem Python 3
* Django
* AngularJS
* Mysql
* Repositório no GitHub

A seguir estão os principais comandos do git a serem execultados no terminal.

**Principais comandos do github**

Copia repositório para o diretório local
> git clone https://github.com/geans/barganhou

Para verificar arquivos alterados e adicionados ou não no Stage
> git status

Adicionando diretórios ou arquivos novos ou modificados no Stage
> git add arquivo.txt

Remove arquivos no Stage
> git rm arquivo.txt

Remove diretório (e seu conteúdo)
> git rm -r diretório

Remove arquivos que já foram adicionados para commit
> git rm --cached arquivo.txt

Apenas arquivos no Stage podem ser commitados (o primeiro comando abrirá o editor padrão para escrita da mensagem)
> git commit
> git commit -m "Mensagem"

Para mandar os arquivos "commitados" para o repositório, será pedido usuário e senha
> git push

Atualizar cópia do repositório
> git pull

Ambiente de Desenvolvimento
---------------------------


Características do projeto
--------------------------
* Interface web para adesão de instância no banco de dados através de um formulário