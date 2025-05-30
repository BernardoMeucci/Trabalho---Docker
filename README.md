Projeto de Aprendizado: Docker e Docker Compose 🐳
Introdução
Este projeto é uma compilação de 13 exercícios práticos desenvolvidos como parte de um trabalho acadêmico, com o objetivo de explorar e demonstrar proficiência nas tecnologias Docker e Docker Compose. Todo o desenvolvimento, incluindo a edição de arquivos e a execução de comandos, foi realizado utilizando o Visual Studio Code e seu terminal integrado.

Para uma melhor organização, os exercícios que envolvem a criação de múltiplos arquivos (Dockerfile, scripts de aplicação, arquivos de configuração, etc.) estão contidos em pastas dedicadas (ex: Exercicio-01/, Exercicio-06/). Exercícios que consistiram primariamente na execução de comandos Docker diretamente no terminal são documentados em detalhe nas suas respectivas seções neste README, incluindo os comandos utilizados e as interações esperadas.

Pré-requisitos
Para replicar os exercícios deste projeto, é necessário ter o seguinte software instalado:

Docker Desktop (ou Docker Engine no Linux)
Docker Compose (geralmente incluído no Docker Desktop)
Visual Studio Code (ou outro editor/terminal de sua preferência)
Git (necessário para clonar os projetos base dos exercícios 6 e 7)
(Opcional) Instalações locais de Python, Node.js, Go, se desejar executar as aplicações fora dos contêineres Docker.
Estrutura do Projeto
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
Exercício 01: Olá, Docker!
Objetivo: Criar uma imagem Docker mínima baseada em Alpine que imprime "Olá, Docker!" ao ser executada.
Conceitos Praticados: Dockerfile (básico), FROM, CMD, docker build, docker run.
Arquivos e Estrutura: Uma pasta Exercicio-01/ contendo um Dockerfile.
Passos e Comandos Executados:
Navegar para a pasta: cd Exercicio-01
Conteúdo do Dockerfile:
Dockerfile

FROM alpine
CMD ["echo", "Olá, Docker!"]
Construir a imagem: docker build -t meu-echo .
Executar o contêiner: docker run --rm meu-echo
Saída Esperada: Olá, Docker!
Resumo: Primeiro contato com a criação de uma imagem Docker, entendendo as instruções básicas e o ciclo de build/run.
Exercício 02: Servidor Nginx com Página Customizada
Objetivo: Servir uma página index.html customizada usando um contêiner Nginx e um bind mount.
Conceitos Praticados: Bind Mounts (-v), mapeamento de portas (-p), modo detached (-d).
Arquivos e Estrutura: Uma pasta Exercicio-02/ contendo um arquivo index.html.
Passos e Comandos Executados:
Navegar para a pasta: cd Exercicio-02
Criar um index.html com conteúdo personalizado.
Executar o contêiner Nginx:
Bash

docker run --rm -d --name meu-site-nginx -p 80:80 -v "${pwd}:/usr/share/nginx/html" nginx
(No PowerShell, ${pwd} refere-se ao diretório atual).
Acessar http://localhost no navegador.
Saída Esperada: A página index.html customizada é exibida no navegador.
Resumo: Aprendizado sobre como montar volumes do host para o contêiner, permitindo desenvolvimento iterativo e servindo arquivos locais.
Exercício 03: Terminal Interativo com Ubuntu
Objetivo: Iniciar um contêiner Ubuntu, obter um terminal interativo e instalar o pacote curl.
Conceitos Praticados: Modo interativo (-it), contêineres efêmeros (--rm), gerenciamento de pacotes (apt-get) dentro de um contêiner.
Arquivos e Estrutura: Este exercício foi executado diretamente no terminal.
Passos e Comandos Executados:
Iniciar contêiner interativo:
Bash

docker run -it --rm ubuntu bash
Dentro do contêiner (o prompt muda para root@<id_container>:/#):
Bash

# Atualizar lista de pacotes
apt-get update

# Instalar curl (o -y confirma automaticamente)
apt-get install -y curl

# Verificar instalação
curl --version

# Sair do contêiner
exit
Saída Esperada: Informações da versão do curl e retorno ao terminal do host.
Resumo: Demonstração do uso de contêineres como ambientes Linux isolados e temporários para executar comandos ou instalar software.
Exercício 04: Banco de Dados MySQL com Dados Persistentes
Objetivo: Rodar um contêiner MySQL e garantir que os dados criados persistam usando um volume nomeado.
Conceitos Praticados: Volumes Nomeados, persistência de dados, variáveis de ambiente (-e), docker exec.
Arquivos e Estrutura: Este exercício foi executado diretamente no terminal.
Passos e Comandos Executados:
Iniciar o contêiner MySQL:
Bash

docker run --name meu-mysql -d -v mysql-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=senha_forte mysql:5.7
Conectar ao MySQL dentro do contêiner e criar um banco:
Bash

docker exec -it meu-mysql mysql -u root -p
# (Digitar 'senha_forte' quando solicitado)
Dentro do prompt mysql>:
SQL

CREATE DATABASE meu_banco_de_teste;
SHOW DATABASES;
exit;
Parar e iniciar o contêiner para testar a persistência:
Bash

docker stop meu-mysql
docker start meu-mysql
Reconectar e verificar se o banco de dados ainda existe:
Bash

docker exec -it meu-mysql mysql -u root -p
# (Digitar 'senha_forte')
Dentro do prompt mysql>:
SQL

SHOW DATABASES; 
exit;
Saída Esperada: O meu_banco_de_teste deve estar listado após reiniciar o contêiner.
Resumo: Uso de volumes nomeados para desvincular os dados do ciclo de vida do contêiner, garantindo a persistência dos dados do banco.
Exercício 05: Variáveis de Ambiente
Objetivo: Passar uma variável de ambiente customizada para um contêiner e ler seu valor de dentro dele.
Conceitos Praticados: Variáveis de ambiente (-e), acesso a variáveis em um shell ($VAR_NAME).
Arquivos e Estrutura: Este exercício foi executado diretamente no terminal.
Passos e Comandos Executados:
Bash

docker run --rm -e MEU_NOME="Meu Nome Completo" alpine sh -c 'echo "O nome guardado na variável é: $MEU_NOME"'
Saída Esperada: O nome guardado na variável é: Meu Nome Completo
Resumo: Demonstração de como injetar configurações em contêineres no momento da sua execução usando variáveis de ambiente.
Exercício 06: Otimização de Imagem Go com Multi-Stage Build (GS PING)
Objetivo: Otimizar o tamanho da imagem de uma aplicação Go (projeto GS PING do GitHub) usando multi-stage builds.
Conceitos Praticados: Multi-stage builds (FROM ... AS builder, COPY --from=...), otimização de imagem, clonagem Git.
Arquivos e Estrutura: Código clonado do repositório olliefr/docker-gs-ping. O Dockerfile.multistage foi usado como base, renomeado para Dockerfile.
Passos e Comandos Executados:
Clonar o repositório: git clone https://github.com/olliefr/docker-gs-ping.git
Navegar para a pasta: cd docker-gs-ping
Renomear ou usar o Dockerfile.multistage: (Ex: mv Dockerfile.multistage Dockerfile no Linux/macOS ou ren Dockerfile.multistage Dockerfile no PowerShell)
Construir a imagem: docker build -t meu-gs-ping .
Verificar o tamanho da imagem (docker images).
Executar o contêiner: docker run --rm -p 8080:8080 meu-gs-ping
Saída Esperada: Aplicação acessível em http://localhost:8080 (exibindo "Hello, Docker! <3" ou "pong").
Resumo: Utilização de um Dockerfile.multistage para criar uma imagem Go de produção enxuta, separando o ambiente de compilação do ambiente de execução.
Exercício 07: Full-Stack com Docker Compose (React + Express + MongoDB)
Objetivo: Utilizar Docker Compose para orquestrar uma aplicação full-stack (React, Express, MongoDB) a partir do exemplo react-express-mongodb do repositório docker/awesome-compose.
Conceitos Praticados: Docker Compose (docker-compose.yml), múltiplos serviços, build vs. image em Compose, networking entre contêineres, volumes nomeados, depends_on.
Arquivos e Estrutura: Código clonado de docker/awesome-compose e navegação para a subpasta react-express-mongodb.
Passos e Comandos Executados:
Clonar o repositório: git clone https://github.com/docker/awesome-compose.git
Navegar para a pasta do exemplo: cd awesome-compose/react-express-mongodb
Subir o ambiente: docker-compose up --build -d
Para parar: docker-compose down (adicionar -v para remover volumes).
Saída Esperada: Frontend acessível em http://localhost:3000 (ou conforme definido no docker-compose.yml), interagindo com o backend e o banco.
Resumo: Demonstração da orquestração de uma aplicação multi-contêiner completa, incluindo frontend, backend e banco de dados, gerenciados por um único arquivo docker-compose.yml.
Exercício 08: PostgreSQL + pgAdmin com Docker Compose
Objetivo: Configurar um banco de dados PostgreSQL e a interface de gerenciamento pgAdmin usando Docker Compose e um arquivo .env para configurações.
Conceitos Praticados: Docker Compose, arquivos .env para configuração de senhas e usuários, volumes nomeados, depends_on.
Arquivos e Estrutura: Uma pasta exercicio-08/ contendo docker-compose.yml e .env.
Passos e Comandos Executados:
Criar o arquivo .env com as variáveis: POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB, PGADMIN_DEFAULT_EMAIL, PGADMIN_DEFAULT_PASSWORD.
Criar docker-compose.yml definindo os serviços postgres e pgadmin, referenciando as variáveis do .env (ex: ${POSTGRES_USER}), mapeando portas e volumes.
Na pasta exercicio-08/, executar: docker-compose up -d
Acessar pgAdmin (ex: http://localhost:5050) e configurar a conexão ao servidor, usando postgres (ou o nome do serviço do DB) como "Host name/address".
Saída Esperada: pgAdmin acessível e conectado ao banco de dados PostgreSQL.
Resumo: Configuração de um ambiente de banco de dados com uma ferramenta de administração, destacando o uso de .env para segurança e a comunicação entre serviços no Docker Compose.
Exercício 09: Site Estático com Nginx (Landing Page Creative Tim)
Objetivo: Empacotar e servir um site HTML/CSS/JS estático usando um contêiner Nginx.
Conceitos Praticados: Dockerfile para site estático, COPY de múltiplos arquivos/pastas, imagem nginx.
Arquivos e Estrutura: Uma pasta Exercicio-09/material-kit/ contendo os arquivos do site e um Dockerfile.
Passos e Comandos Executados:
Navegar para Exercicio-09/material-kit/.
Conteúdo do Dockerfile:
Dockerfile

FROM nginx:stable-alpine
COPY . /usr/share/nginx/html
EXPOSE 80
Construir a imagem: docker build -t meu-site-creativetim .
Executar o contêiner (escolha uma porta livre, ex: 8088):
Bash

docker run --rm -d -p 8088:80 --name landing-page meu-site-creativetim
Saída Esperada: Site acessível em http://localhost:8088.
Resumo: Criação de uma imagem Nginx customizada para servir um site estático completo.
Exercício 10: Aplicação com Usuário Não-Root
Objetivo: Criar uma imagem Docker para uma aplicação simples (Python ou Node.js) configurada para rodar com um usuário não-root, por segurança.
Conceitos Praticados: Segurança em contêineres, USER no Dockerfile, criação de usuários/grupos (adduser/addgroup).
Arquivos e Estrutura: Uma pasta Exercicio-10/ com um script de aplicação (ex: app.js) e um Dockerfile.
Passos e Comandos Executados (exemplo Node.js):
Criar app.js que roda continuamente (com setInterval) e o Dockerfile.
Dockerfile

# Dockerfile para Node.js
FROM node:18-alpine
RUN addgroup -S appgroup && adduser -S -G appgroup appuser
WORKDIR /usr/src/app
COPY app.js .
USER appuser
CMD ["node", "./app.js"]
Construir: docker build -t node-app-nonroot .
Rodar: docker run -d --name meu-node-app node-app-nonroot
Verificar usuário: docker exec meu-node-app whoami (Saída esperada: appuser).
Resumo: Aplicação do princípio de menor privilégio, executando a aplicação com um usuário dedicado e sem permissões de root dentro do contêiner.
Exercício 11: Análise de Vulnerabilidades com Trivy
Objetivo: Analisar uma imagem Docker pública em busca de vulnerabilidades conhecidas usando o Trivy.
Conceitos Praticados: Segurança de imagens, ferramentas de scan de vulnerabilidades, interpretação de relatórios, sugestão de mitigações.
Arquivos e Estrutura: Este exercício foi executado diretamente no terminal.
Passos e Comandos Executados:
Executar Trivy via Docker para escanear, por exemplo, python:3.9-slim:
Bash

docker run --rm aquasec/trivy:latest image python:3.9-slim
(O comando mais completo com cache e acesso ao docker.sock também foi discutido: docker run --rm -v trivy-cache:/root/.cache/ -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:latest image python:3.9-slim)
Analisar a saída, procurando por vulnerabilidades HIGH e CRITICAL.
Saída Esperada (Exemplo para python:3.9-slim): Um sumário como Total: 92 (UNKNOWN: 1, LOW: 60, MEDIUM: 17, HIGH: 5, CRITICAL: 1), seguido da lista detalhada das vulnerabilidades. Pacotes como zlib1g, libc-bin, libc6, libsystemd0, libudev1, perl-base foram identificados com vulnerabilidades.
Resumo: Aprendizado sobre como usar ferramentas de scan para identificar riscos de segurança em imagens Docker. A principal ação de mitigação é, geralmente, atualizar a imagem base para uma tag mais recente e segura (ex: baseada no Debian "Bookworm" em vez de "Bullseye" ou "Buster").
Exercício 12: Refatorar Dockerfile com Más Práticas
Objetivo: Melhorar um Dockerfile com más práticas para uma aplicação Python Flask, tornando-o mais seguro (usuário não-root) e enxuto (imagem base leve, otimização de cache).
Conceitos Praticados: Otimização de Dockerfile, imagens base leves (-slim), usuário não-root, cache de camadas, "exec form" para CMD.
Arquivos e Estrutura: Uma pasta Exercicio-12/ com app.py (Flask "Hello World!"), requirements.txt (Flask==3.0.0), e Dockerfile.
Passos e Comandos Executados:
Criar os arquivos da aplicação e o Dockerfile otimizado:
Dockerfile

# Dockerfile para Exercicio-12
FROM python:3.12-slim # Ou python:3.12-slim-bookworm
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=appuser:appgroup app.py . # Copia app.py
USER appuser
EXPOSE 5000 # Porta interna da aplicação Flask
CMD ["python", "./app.py"]
Construir a imagem: docker build -t imagem-python .
Rodar o contêiner (usando uma porta livre no host, ex: 5001):
Bash

docker run -d --rm -p 5001:5000 --name meu-flask imagem-python
Saída Esperada: Aplicação Flask acessível em http://localhost:5001 exibindo "Hello, World!", e docker exec meu-flask whoami retornando appuser.
Resumo: Transformação de um Dockerfile menos eficiente em uma versão que segue boas práticas de segurança, tamanho e eficiência de build.
Exercício 13: Script Python com Argumentos via Docker
Objetivo: Criar um script Python que aceita argumentos passados através do comando docker run, utilizando ENTRYPOINT e CMD.
Conceitos Praticados: ENTRYPOINT, CMD (para argumentos padrão), passagem de argumentos ao contêiner.
Arquivos e Estrutura: Uma pasta Exercicio-13/ com app.py e Dockerfile.
Passos e Comandos Executados:
Criar app.py:
Python

# Exercicio-13/app.py
import sys
if len(sys.argv) > 1:
    name = " ".join(sys.argv[1:]) # Junta todos os argumentos após o nome do script
else:
    name = "Mundo (Default)"
print(f"Olá, {name}, do contêiner!")
Criar Dockerfile:
Dockerfile

# Exercicio-13/Dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY app.py .
ENTRYPOINT ["python", "./app.py"]
# CMD pode ser usado para fornecer argumentos padrão se nenhum for passado no 'docker run'
CMD ["Convidado"] 
Construir a imagem: docker build -t python-args-app ./Exercicio-13
Executar o contêiner:
Com argumento padrão: docker run --rm python-args-app
Com argumento customizado: docker run --rm python-args-app "Seu Nome Aqui"
Saída Esperada:
Para o primeiro run: Olá, Convidado, do contêiner!
Para o segundo run: Olá, Seu Nome Aqui, do contêiner!
Resumo: Demonstração de como usar ENTRYPOINT para definir o executável principal e CMD para fornecer argumentos padrão, que podem ser sobrescritos no comando docker run.