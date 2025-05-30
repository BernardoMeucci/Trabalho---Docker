# Use uma imagem base Node.js leve (baseada em Alpine)
FROM node:18-alpine

# a. Criar um grupo e um usuário não-root (sintaxe do Alpine Linux)
#    -S: cria um usuário/grupo de sistema
#    -G: adiciona o usuário ao grupo especificado
RUN addgroup -S appgroup && adduser -S -G appgroup appuser

# Define o diretório de trabalho padrão para a aplicação
# É uma convenção comum usar /usr/src/app para apps Node.js
WORKDIR /usr/src/app

# Copia o script Node.js para o diretório de trabalho
COPY app.js .

# b. Definir o usuário não-root como o padrão para os comandos subsequentes
USER appuser

# Define o comando padrão para executar o script quando o contêiner iniciar
CMD ["node", "./app.js"]