# Projeto de Aprendizado: Docker & Docker Compose 

## Introdução

Este projeto é uma compilação de 13 exercícios práticos desenvolvidos como parte de um trabalho acadêmico, com o objetivo de explorar e demonstrar proficiência nas tecnologias Docker e Docker Compose. Todo o desenvolvimento, incluindo a edição de arquivos e a execução de comandos, foi realizado utilizando o Visual Studio Code e seu terminal integrado.

Para uma melhor organização, os exercícios que envolvem a criação de múltiplos arquivos (`Dockerfile`, scripts de aplicação, arquivos de configuração, etc.) estão contidos em pastas dedicadas (ex: `Exercicio-01/`, `Exercicio-06/`). Exercícios que consistiram primariamente na execução de comandos Docker diretamente no terminal são documentados em detalhe nas suas respectivas seções neste README, incluindo os comandos utilizados e as interações esperadas.

## Pré-requisitos

Para replicar os exercícios deste projeto, é necessário ter o seguinte software instalado:

* **Docker Desktop** (ou Docker Engine no Linux)
* **Docker Compose** (geralmente incluído no Docker Desktop)
* **Visual Studio Code** (ou outro editor/terminal de sua preferência)
* **Git** (necessário para clonar os projetos base dos exercícios 6 e 7)
* (Opcional) Instalações locais de Python, Node.js, Go, se desejar executar as aplicações fora dos contêineres Docker.

## Estrutura do Projeto

O projeto está organizado da seguinte forma, com pastas dedicadas para exercícios que envolvem a criação de arquivos específicos. Exercícios que foram puramente interações no terminal (03, 04, 05, 11) são detalhados diretamente neste README.

Analyzing PDF Conversion Options

I'm currently thinking about how to help with PDF creation.  I've realized I can't directly generate a PDF file. So, I need to find a suitable workaround to convert the user's README.md to a printable format. This could involve recommending third-party tools or providing instructions on how to accomplish it.

Refining PDF Conversion Approaches

I understand the need for a PDF version of the README.md content. It's clear I can't directly create a PDF, so I'm focusing on providing practical solutions. I'm leaning toward suggesting VS Code extensions and online converters as the most user-friendly options, but I also want to mention Pandoc for those with more technical expertise. I'll provide detailed instructions and relevant links for each method to ensure the user can easily implement the conversion. Privacy concerns are a factor, which I will advise on.

Exploring Conversion Recommendations

I've been thinking about the best methods to suggest for converting the user's Markdown to PDF. I'm focusing on options that are both user-friendly and produce a high-quality result, such as the print-to-PDF method via GitHub, which offers a great combination of ease and visual fidelity. I've also identified VS Code extensions, online converters, Pandoc, and copy-pasting as potential routes, tailoring the recommendations based on the user's likely familiarity with the tools. I will advise on privacy concerns if relevant.

Devising Markdown-to-PDF Strategy

I'm now focusing on actionable steps. I'll explain my inability to generate PDFs and offer solutions. My primary recommendation will be using GitHub's "Print to PDF" function, as it's simple and preserves the Markdown formatting. A VS Code extension will be my secondary suggestion for local conversion. I'll also provide the Markdown text in a clean block for easy copying.

Eu, como inteligência artificial, não consigo gerar diretamente um arquivo PDF para você. No entanto, posso te dar o texto completo do README.md novamente e te mostrar algumas maneiras fáceis de convertê-lo para PDF para que você possa imprimir.

A maneira mais comum e que geralmente resulta em uma boa formatação (especialmente se você já enviou para o GitHub) é usar a função de impressão do navegador na página do GitHub, ou usar uma extensão no VS Code.

Opção 1: Gerar PDF a partir da Página do GitHub (Recomendado após o Push)
Esta opção garante que o PDF terá a mesma aparência que seu professor verá online.

Envie o README.md para o GitHub: Siga os passos que discutimos para fazer o git add README.md, git commit, e git push.
Abra o Repositório no Navegador: Vá para a página principal do seu repositório no GitHub. O README.md será exibido formatado.
Use a Função "Imprimir" do Navegador:
No seu navegador (Chrome, Firefox, Edge, etc.), vá em Arquivo > Imprimir (ou pressione Ctrl + P / Cmd + P).
Na janela de impressão, em vez de selecionar uma impressora física, procure por uma opção como:
"Salvar como PDF"
"Microsoft Print to PDF"
"Guardar como PDF"
Ajuste as opções de layout se necessário (ex: orientação, margens) e salve o arquivo PDF.
Opção 2: Usar uma Extensão do VS Code
Existem extensões no VS Code que convertem Markdown para PDF diretamente. Uma popular é a "Markdown PDF".

Instale a Extensão (se ainda não tiver):
No VS Code, vá para a aba de Extensões (ícone de blocos no menu lateral).
Procure por Markdown PDF (do autor yzane).
Clique em "Instalar".
Converta o Arquivo:
Abra seu arquivo README.md no VS Code.
Clique com o botão direito dentro do editor de texto do arquivo.
No menu de contexto, você deverá ver opções como "Markdown PDF: Export (pdf)" ou similar.
Siga as instruções da extensão para gerar o PDF.
Opção 3: Conversores Online
Existem muitos sites que convertem Markdown para PDF.

Procure no Google por "markdown to pdf online converter".
Escolha um site, copie o conteúdo do seu README.md (o texto bruto que vou te passar abaixo) e cole no conversor.
Baixe o PDF gerado. (Tenha cuidado com informações sensíveis se usar esta opção, embora para este README não deva ser um problema).
Opção 4: Copiar para um Editor de Texto Avançado
Copie o conteúdo do README.md.
Cole em um editor como Microsoft Word, Google Docs ou LibreOffice Writer.
Ajuste a formatação se necessário (especialmente para blocos de código).
Use a função "Salvar como PDF" ou "Exportar para PDF" desses programas.
Conteúdo Completo do README.md para Você Copiar:
Aqui está o texto completo novamente. Copie tudo a partir da linha abaixo de --- COPIE DAQUI PARA BAIXO --- e cole no seu arquivo README.md local ou em uma das ferramentas de conversão:

--- COPIE DAQUI PARA BAIXO ---

Markdown

# Projeto de Aprendizado: Docker & Docker Compose 🐳

## Introdução

Este projeto é uma compilação de 13 exercícios práticos desenvolvidos como parte de um trabalho acadêmico, com o objetivo de explorar e demonstrar proficiência nas tecnologias Docker e Docker Compose. Todo o desenvolvimento, incluindo a edição de arquivos e a execução de comandos, foi realizado utilizando o Visual Studio Code e seu terminal integrado.

Para uma melhor organização, os exercícios que envolvem a criação de múltiplos arquivos (`Dockerfile`, scripts de aplicação, arquivos de configuração, etc.) estão contidos em pastas dedicadas (ex: `Exercicio-01/`, `Exercicio-06/`). Exercícios que consistiram primariamente na execução de comandos Docker diretamente no terminal são documentados em detalhe nas suas respectivas seções neste README, incluindo os comandos utilizados e as interações esperadas.

## Pré-requisitos

Para replicar os exercícios deste projeto, é necessário ter o seguinte software instalado:

* **Docker Desktop** (ou Docker Engine no Linux)
* **Docker Compose** (geralmente incluído no Docker Desktop)
* **Visual Studio Code** (ou outro editor/terminal de sua preferência)
* **Git** (necessário para clonar os projetos base dos exercícios 6 e 7)
* (Opcional) Instalações locais de Python, Node.js, Go, se desejar executar as aplicações fora dos contêineres Docker.

## Estrutura do Projeto

O projeto está organizado da seguinte forma, com pastas dedicadas para exercícios que envolvem a criação de arquivos específicos. Exercícios que foram puramente interações no terminal (03, 04, 05, 11) são detalhados diretamente neste README.

/ (Raiz do Projeto "Trabalho Docker")
├── Exercicio-01/
│   └── Dockerfile
├── Exercicio-02/
│   └── index.html
├── Exercicio-06/ (Conteúdo do projeto GS PING após clonagem)
│   ├── main.go
│   ├── go.mod
│   └── Dockerfile (Adaptado do Dockerfile.multistage)
├── Exercicio-07/ (Conteúdo do projeto React-Express-MongoDB após clonagem)
│   ├── frontend/
│   ├── backend/
│   └── docker-compose.yml
├── exercicio-08/
│   ├── .env
│   └── docker-compose.yml
├── Exercicio-09/
│   └── material-kit/ (Contendo o site e o Dockerfile)
├── Exercicio-10/
│   ├── app.js (ou app.py, conforme a versão feita)
│   └── Dockerfile
├── Exercicio-12/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── Exercicio-13/
│   ├── app.py
│   └── Dockerfile
└── README.md (este arquivo)



## Exercício 01: Olá, Docker!

* **Objetivo:** Criar uma imagem Docker mínima baseada em Alpine que imprime "Olá, Docker!" ao ser executada.
* **Conceitos Praticados:** `Dockerfile` (básico), `FROM`, `CMD`, `docker build`, `docker run`.
* **Arquivos e Estrutura:** Uma pasta `Exercicio-01/` contendo um `Dockerfile`.
* **Passos e Comandos Executados:**
    1.  Navegar para a pasta: `cd Exercicio-01`
    2.  Conteúdo do `Dockerfile`:

        ```dockerfile
        FROM alpine
        CMD ["echo", "Olá, Docker!"]
        ```
    3.  Construir a imagem:

        ```bash
        docker build -t meu-echo .
        ```
    4.  Executar o contêiner:

        ```bash
        docker run --rm meu-echo
        ```
* **Saída Esperada:** `Olá, Docker!`
* **Resumo:** Primeiro contato com a criação de uma imagem Docker, entendendo as instruções básicas e o ciclo de build/run.

---

## Exercício 02: Servidor Nginx com Página Customizada

* **Objetivo:** Servir uma página `index.html` customizada usando um contêiner Nginx e um bind mount.
* **Conceitos Praticados:** Bind Mounts (`-v`), mapeamento de portas (`-p`), modo detached (`-d`), imagens oficiais.
* **Arquivos e Estrutura:** Uma pasta `Exercicio-02/` contendo um arquivo `index.html`.
* **Passos e Comandos Executados:**
    1.  Navegar para a pasta: `cd Exercicio-02`
    2.  Criar um `index.html` com conteúdo personalizado.
    3.  Executar o contêiner Nginx:

        ```bash
        docker run --rm -d --name meu-site-nginx -p 80:80 -v "${pwd}:/usr/share/nginx/html" nginx
        ```
        *(No PowerShell, `${pwd}` refere-se ao diretório atual).*
    4.  Acessar `http://localhost` no navegador.
* **Saída Esperada:** A página `index.html` customizada é exibida no navegador.
* **Resumo:** Aprendizado sobre como montar volumes do host para o contêiner, permitindo desenvolvimento iterativo e servindo arquivos locais.

---

## Exercício 03: Terminal Interativo com Ubuntu

* **Objetivo:** Iniciar um contêiner Ubuntu, obter um terminal interativo e instalar o pacote `curl`.
* **Conceitos Praticados:** Modo interativo (`-it`), contêineres efêmeros (`--rm`), gerenciamento de pacotes (`apt-get`) dentro de um contêiner.
* **Arquivos e Estrutura:** Este exercício foi executado diretamente no terminal.
* **Passos e Comandos Executados:**
    1.  Iniciar contêiner interativo:

        ```bash
        docker run -it --rm ubuntu bash
        ```
    2.  Interação dentro do contêiner (o prompt mudará para `root@<id_container>:/#`):

        ```bash
        # Atualizar lista de pacotes
        apt-get update

        # Instalar curl (o -y confirma automaticamente)
        apt-get install -y curl

        # Verificar instalação
        curl --version

        # Sair do contêiner
        exit
        ```
* **Saída Esperada:** Informações da versão do `curl` e retorno ao terminal do host.
* **Resumo:** Demonstração do uso de contêineres como ambientes Linux isolados e temporários para executar comandos ou instalar software.

---

## Exercício 04: Banco de Dados MySQL com Dados Persistentes

* **Objetivo:** Rodar um contêiner MySQL e garantir que os dados criados persistam usando um volume nomeado.
* **Conceitos Praticados:** Volumes Nomeados, persistência de dados, variáveis de ambiente (`-e`), `docker exec`.
* **Arquivos e Estrutura:** Este exercício foi executado diretamente no terminal.
* **Passos e Comandos Executados:**
    1.  Iniciar o contêiner MySQL:

        ```bash
        docker run --name meu-mysql -d -v mysql-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=senha_forte mysql:5.7
        ```
    2.  Conectar ao MySQL dentro do contêiner e criar um banco (o prompt do terminal muda):

        ```bash
        docker exec -it meu-mysql mysql -u root -p
        # (Digitar 'senha_forte' quando solicitado)
        ```
        Dentro do prompt `mysql>`:
        ```sql
        CREATE DATABASE meu_banco_de_teste;
        SHOW DATABASES;
        exit;
        ```
    3.  Parar e iniciar o contêiner para testar a persistência:

        ```bash
        docker stop meu-mysql
        docker start meu-mysql
        ```
    4.  Reconectar e verificar se o banco de dados ainda existe (o prompt do terminal muda):

        ```bash
        docker exec -it meu-mysql mysql -u root -p
        # (Digitar 'senha_forte')
        ```
        Dentro do prompt `mysql>`:
        ```sql
        SHOW DATABASES; 
        exit;
        ```
* **Saída Esperada:** O `meu_banco_de_teste` deve estar listado após reiniciar o contêiner.
* **Resumo:** Uso de volume nomeado para desvincular os dados do ciclo de vida do contêiner, garantindo a persistência dos dados do banco.

---

## Exercício 05: Variáveis de Ambiente

* **Objetivo:** Passar uma variável de ambiente customizada para um contêiner e ler seu valor de dentro dele.
* **Conceitos Praticados:** Variáveis de ambiente (`-e`), acesso a variáveis em um shell (`$VAR_NAME`).
* **Arquivos e Estrutura:** Este exercício foi executado diretamente no terminal.
* **Passos e Comandos Executados:**

    ```bash
    docker run --rm -e MEU_NOME="Meu Nome Completo" alpine sh -c 'echo "O nome guardado na variável é: $MEU_NOME"'
    ```
* **Saída Esperada no Terminal:**

    `O nome guardado na variável é: Meu Nome Completo`
* **Resumo:** Demonstração da configuração de contêineres em tempo de execução usando variáveis de ambiente.

---

## Exercício 06: Otimização de Imagem Go com Multi-Stage Build (GS PING)

* **Objetivo:** Otimizar o tamanho da imagem de uma aplicação Go (projeto GS PING do GitHub) usando multi-stage builds.
* **Conceitos Praticados:** Multi-stage builds (`FROM ... AS builder`, `COPY --from=...`), otimização de imagem, clonagem Git.
* **Arquivos e Estrutura:** Código clonado do repositório `olliefr/docker-gs-ping`. O `Dockerfile.multistage` foi usado como base, idealmente renomeado para `Dockerfile`.
* **Passos e Comandos Executados:**
    1.  Clonar o repositório:

        ```bash
        git clone [https://github.com/olliefr/docker-gs-ping.git](https://github.com/olliefr/docker-gs-ping.git)
        ```
    2.  Navegar para a pasta:

        ```bash
        cd docker-gs-ping
        ```
    3.  (Opcional/Recomendado) Renomear `Dockerfile.multistage` para `Dockerfile`:
        *(Exemplo no PowerShell: `ren Dockerfile.multistage Dockerfile`)*
    4.  Construir a imagem:

        ```bash
        docker build -t meu-gs-ping .
        # Se não renomeou: docker build -f Dockerfile.multistage -t meu-gs-ping .
        ```
    5.  Verificar o tamanho da imagem (`docker images`).
    6.  Executar o contêiner:

        ```bash
        docker run --rm -p 8080:8080 meu-gs-ping
        ```
* **Saída Esperada:** Aplicação acessível em `http://localhost:8080` (exibindo "Hello, Docker! <3" ou "pong", dependendo da versão do código no repo).
* **Resumo:** Utilização do `Dockerfile.multistage` do projeto GS PING para construir uma imagem Go otimizada, demonstrando a redução significativa de tamanho ao separar o ambiente de compilação do ambiente de execução.

---

## Exercício 07: Full-Stack com Docker Compose (React + Express + MongoDB)

* **Objetivo:** Utilizar Docker Compose para orquestrar uma aplicação full-stack (React, Express, MongoDB) a partir do exemplo `react-express-mongodb` do repositório `docker/awesome-compose`.
* **Conceitos Praticados:** Docker Compose (`docker-compose.yml`), múltiplos serviços, `build` vs. `image` em Compose, networking entre contêineres por nome de serviço, volumes nomeados, `depends_on`.
* **Arquivos e Estrutura:** Código clonado de `docker/awesome-compose` e navegação para a subpasta `react-express-mongodb`.
* **Passos e Comandos Executados:**
    1.  Clonar o repositório:

        ```bash
        git clone [https://github.com/docker/awesome-compose.git](https://github.com/docker/awesome-compose.git)
        ```
    2.  Navegar para a pasta do exemplo:

        ```bash
        cd awesome-compose/react-express-mongodb
        ```
    3.  Subir o ambiente (construindo as imagens e rodando em background):

        ```bash
        docker-compose up --build -d
        ```
    4.  Para parar e remover os contêineres e rede:

        ```bash
        docker-compose down
        ```
        *(Adicionar `-v` para remover volumes de dados do MongoDB).*
* **Saída Esperada:** Frontend acessível em `http://localhost:3000` (ou conforme definido nos `ports` do serviço frontend no `docker-compose.yml`), interagindo com o backend e o banco de dados.
* **Resumo:** Utilização de um exemplo do `docker/awesome-compose` para subir uma aplicação full-stack. O `docker-compose.yml` define e conecta os serviços de frontend (React), backend (Express) e banco de dados (MongoDB), demonstrando a facilidade de gerenciar múltiplos contêineres interconectados.

---

## Exercício 08: PostgreSQL + pgAdmin com Docker Compose

* **Objetivo:** Configurar um banco de dados PostgreSQL e a interface de gerenciamento pgAdmin usando Docker Compose e um arquivo `.env` para configurações.
* **Conceitos Praticados:** Docker Compose, arquivos `.env` para configuração de senhas e usuários, volumes nomeados, `depends_on`, conexão entre serviços.
* **Arquivos e Estrutura:** Uma pasta `exercicio-08/` contendo `docker-compose.yml` e `.env`.
* **Passos e Comandos Executados:**
    1.  Criar o arquivo `.env` com as variáveis: `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`, `PGADMIN_DEFAULT_EMAIL`, `PGADMIN_DEFAULT_PASSWORD`.
    2.  Criar `docker-compose.yml` definindo os serviços `postgres` e `pgadmin`, referenciando as variáveis do `.env` (ex: `${POSTGRES_USER}`), mapeando portas e volumes.
    3.  Na pasta `exercicio-08/`, executar:

        ```bash
        docker-compose up -d
        ```
    4.  Acessar pgAdmin (ex: `http://localhost:5050`) e configurar a conexão ao servidor, usando `postgres` (ou o nome do serviço do DB no `docker-compose.yml`) como "Host name/address".
* **Saída Esperada:** Interface do pgAdmin acessível via navegador e conectada com sucesso ao banco de dados PostgreSQL.
* **Resumo:** Configuração de um ambiente de banco de dados com uma ferramenta de administração, com configurações seguras em `.env` e demonstrando a comunicação entre serviços no Docker Compose.

---

## Exercício 09: Site Estático com Nginx (Landing Page Creative Tim)

* **Objetivo:** Empacotar e servir um site HTML/CSS/JS estático usando um contêiner Nginx.
* **Conceitos Praticados:** `Dockerfile` para site estático, `COPY` de múltiplos arquivos/pastas, imagem `nginx`.
* **Arquivos e Estrutura:** Uma pasta `Exercicio-09/material-kit/` (após obter os arquivos do site) contendo os arquivos do site e um `Dockerfile`.
* **Passos e Comandos Executados:**
    1.  Navegar para `Exercicio-09/material-kit/`.
    2.  Conteúdo do `Dockerfile`:

        ```dockerfile
        FROM nginx:stable-alpine
        COPY . /usr/share/nginx/html
        EXPOSE 80
        ```
    3.  Construir a imagem:

        ```bash
        docker build -t meu-site-creativetim .
        ```
    4.  Executar o contêiner (escolha uma porta livre no host, ex: `8088`):

        ```bash
        docker run --rm -d -p 8088:80 --name landing-page meu-site-creativetim
        ```
* **Saída Esperada:** Site acessível em `http://localhost:8088`.
* **Resumo:** Empacotamento de um site estático completo em uma imagem Nginx para fácil distribuição e hospedagem.

---

## Exercício 10: Aplicação com Usuário Não-Root

* **Objetivo:** Criar uma imagem Docker para uma aplicação simples (Python ou Node.js) configurada para rodar com um usuário não-root, por segurança.
* **Conceitos Praticados:** Segurança em contêineres, `USER` no `Dockerfile`, criação de usuários/grupos (`adduser`/`addgroup`).
* **Arquivos e Estrutura:** Uma pasta `Exercicio-10/` com um script de aplicação (ex: `app.js` ou `app.py`) e um `Dockerfile`.
* **Passos e Comandos Executados (exemplo Node.js):**
    1.  Criar `app.js` que roda continuamente (com `setInterval`) e o `Dockerfile`.
        * Conteúdo do `app.js`:
            ```javascript
            // Exercicio-10/app.js
            const process = require('process');
            console.log(` Olá do script Node.js!`);
            console.log(`   Rodando como UID: ${process.getuid()}, GID: ${process.getgid()}`);
            setInterval(() => {}, 3600 * 1000); 
            ```
        * Conteúdo do `Dockerfile`:
            ```dockerfile
            FROM node:18-alpine
            RUN addgroup -S appgroup && adduser -S -G appgroup appuser
            WORKDIR /usr/src/app
            COPY app.js .
            USER appuser
            # Usamos -u para que os prints do Node.js apareçam nos logs imediatamente
            CMD ["node", "-u", "./app.js"] 
            ```
    2.  Construir a imagem (ex: `node-app-nonroot` ou `meu-app-python`):

        ```bash
        docker build -t node-app-nonroot .
        ```
    3.  Rodar o contêiner:

        ```bash
        docker run -d --name meu-node-app node-app-nonroot
        ```
    4.  Verificar o usuário:

        ```bash
        docker exec meu-node-app whoami
        ```
* **Saída Esperada:** O comando `whoami` deve retornar `appuser`. Os logs do contêiner (`docker logs meu-node-app`) devem mostrar as mensagens do script.
* **Resumo:** Implementação da prática de segurança de menor privilégio, garantindo que a aplicação dentro do contêiner não execute com permissões de root.

---

## Exercício 11: Análise de Vulnerabilidades com Trivy

* **Objetivo:** Analisar uma imagem Docker pública em busca de vulnerabilidades conhecidas usando o Trivy.
* **Conceitos Praticados:** Segurança de imagens, ferramentas de scan de vulnerabilidades, interpretação de relatórios, sugestão de mitigações.
* **Arquivos e Estrutura:** Este exercício foi executado diretamente no terminal.
* **Passos e Comandos Executados:**
    1.  Executar Trivy via Docker para escanear a imagem `python:3.9-slim`:

        ```bash
        docker run --rm aquasec/trivy:latest image python:3.9-slim
        ```
        *(O comando mais completo com cache e acesso ao docker.sock também foi discutido: `docker run --rm -v trivy-cache:/root/.cache/ -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:latest image python:3.9-slim`)*
    2.  Analisar a saída do Trivy, focando nas vulnerabilidades com severidade `HIGH` e `CRITICAL`.
* **Saída Esperada (Exemplo para `python:3.9-slim`):**
    Um sumário como `Total: 92 (UNKNOWN: 1, LOW: 60, MEDIUM: 17, HIGH: 5, CRITICAL: 1)`, seguido da lista detalhada das vulnerabilidades. Foram identificados pacotes do sistema operacional como `zlib1g` (CRITICAL), `libc-bin`, `libc6`, `libsystemd0`, `libudev1`, `perl-base` (HIGH).
* **Resumo:** Aprendizado sobre como utilizar ferramentas de scan para identificar riscos de segurança em imagens Docker. A principal ação de mitigação sugerida para vulnerabilidades na imagem base é atualizá-la para uma tag mais recente e segura (ex: baseada no Debian "Bookworm").

---

## Exercício 12: Refatorar Dockerfile com Más Práticas

* **Objetivo:** Melhorar um `Dockerfile` comumente encontrado com más práticas para uma aplicação Python Flask, tornando-o mais seguro (usuário não-root) e enxuto (imagem base leve, otimização de cache).
* **Conceitos Praticados:** Otimização de `Dockerfile`, imagens base leves (`-slim`), usuário não-root, cache de camadas (`COPY requirements.txt` antes), "exec form" para `CMD`, variáveis de ambiente (`ENV PYTHONDONTWRITEBYTECODE`, `PYTHONUNBUFFERED`).
* **Arquivos e Estrutura:** Uma pasta `Exercicio-12/` com `app.py` (Flask "Hello, World!"), `requirements.txt` (`Flask==3.0.0`), e `Dockerfile`.
* **Passos e Comandos Executados:**
    1.  Criar os arquivos da aplicação e o `Dockerfile` otimizado:
        * Conteúdo do `app.py`:
            ```python
            from flask import Flask
            app = Flask(__name__)
            @app.route("/")
            def hello_world():
                return "<p>Hello, World!</p>"
            if __name__ == '__main__':
                app.run(host='0.0.0.0', port=5000)
            ```
        * Conteúdo do `Dockerfile`:
            ```dockerfile
            FROM python:3.12-slim # Ou python:3.12-slim-bookworm
            ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
            WORKDIR /app
            RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
            COPY requirements.txt .
            RUN pip install --no-cache-dir -r requirements.txt
            COPY --chown=appuser:appgroup app.py .
            USER appuser
            EXPOSE 5000
            CMD ["python", "./app.py"]
            ```
    2.  Construir a imagem (ex: `imagem-python`):

        ```bash
        docker build -t imagem-python .
        ```
    3.  Rodar o contêiner (usando uma porta livre no host, ex: `5001`, e nome `meu-flask`):

        ```bash
        docker run -d --rm -p 5001:5000 --name meu-flask imagem-python
        ```
* **Saída Esperada:** Aplicação Flask acessível em `http://localhost:5001` exibindo "Hello, World!", e `docker exec meu-flask whoami` retornando `appuser`.
* **Resumo:** Aplicação de diversas boas práticas para criar uma imagem Docker final mais profissional, segura e eficiente para uma aplicação web Python.

---

## Exercício 13: Script Python com Argumentos via Docker

* **Objetivo:** Criar um script Python que aceita argumentos passados através do comando `docker run`, utilizando `ENTRYPOINT` e `CMD` para definir o comportamento padrão e permitir sobrescrita.
* **Conceitos Praticados:** `ENTRYPOINT`, `CMD` (para argumentos padrão), passagem de argumentos ao contêiner na execução.
* **Arquivos e Estrutura:** Uma pasta `Exercicio-13/` com `app.py` e `Dockerfile`.
* **Passos e Comandos Executados:**
    1.  Criar `app.py` em `Exercicio-13/`:
        ```python
        import sys
        if len(sys.argv) > 1:
            name = " ".join(sys.argv[1:]) 
        else:
            # Este else não será atingido se CMD no Dockerfile tiver um argumento padrão
            name = "Mundo (Padrão Script)" 
        print(f"Olá, {name}, do contêiner!")
        ```
    2.  Criar `Dockerfile` em `Exercicio-13/`:
        ```dockerfile
        FROM python:3.12-slim
        WORKDIR /app
        COPY app.py .
        ENTRYPOINT ["python", "./app.py"]
        CMD ["Convidado Padrão Dockerfile"] 
        ```
    3.  Construir a imagem:

        ```bash
        docker build -t python-args-app ./Exercicio-13 
        # ou apenas 'docker build -t python-args-app .' se estiver dentro da pasta Exercicio-13
        ```
    4.  Executar o contêiner:
        * Com argumento padrão do `CMD` do Dockerfile:

            ```bash
            docker run --rm python-args-app
            ```
        * Com argumento customizado fornecido no `docker run`:

            ```bash
            docker run --rm python-args-app "Bernardo Desenvolvedor Full Stack"
            ```
* **Saída Esperada:**
    * Para o primeiro `run`: `Olá, Convidado Padrão Dockerfile, do contêiner!`
    * Para o segundo `run`: `Olá, Bernardo Desenvolvedor Full Stack, do contêiner!`
* **Resumo:** Demonstração de como usar `ENTRYPOINT` para definir o executável principal e `CMD` para fornecer argumentos padrão, que podem ser facilmente sobrescritos ao executar o contêiner com `docker run`.

---

Este `README.md` deve servir como uma excelente documentação para o seu trabalho. Lembre-se de usar a pré-visualização do VS Code (`Ctrl+Shift+V`) para checar a formatação antes de enviar para o GitHub!