Barganhou
=========
Aplicativo para catálogo e comparação de preços

Objetivos
---------
* Fazer registro de preços de produtos
* Manter estatísticas da média e variância desses preços

Divisão do projeto
------------------
* Classe para interação com o banco de dados
* Classe para cálculos estatísticos
* Classe para interface com usuário (comandos)
* Classe para interface gráfica
* Classe para testes

Orientações e recomendações
---------------------------
Para participar do projeto serão necessários conhecimentos em Java e no uso do GitHub.

Para desenvolver no Windows, recomendo o seguinte aplicativo do github: https://git-scm.com/downloads.
A seguir estão os principais comandos do git a serem execultados no terminal; para o Windows use o "Git Bash".

**Principais comandos do github**

Copia repositório para o diretório local
> git clone https://github.com/geans/barganhou

Para uso constante
> git status

Adicionando diretórios ou arquivos novos ou modificados no Stage
> git add arquivo.txt

Remove arquivos no Stage
> git rm arquivo.txt

Remove diretório (e seu conteúdo)
> git rm -r diretório

Remove arquivos que já foram adicionados para commit
> git rm --cached arquivo.txt

Apenas arquivos no Stage podem ser commitados (o primeiro abrirá um editor)
> git commit
> git commit -m "Mensagem"

Para mandar os arquivos "commitados" para o repositório, será pedido usuário e senha
> git push

Atualizar cópia do repositório
> git pull

Ambiente de Desenvolvimento
---------------------------
Eclipse.

**Importando o projeto para eclipse:**

1. File -> Import... -> General -> Existing Projects into Workspace  
2. Procure pelo diretório do projeto através do botão "Browse..."  
3. Clique em "Finish"  
