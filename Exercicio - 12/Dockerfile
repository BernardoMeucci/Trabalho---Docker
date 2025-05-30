# Dockerfile com BOAS PRÁTICAS

# 1. Usar uma imagem mais atual e leve
FROM python:3.12-slim

# Criar diretório de trabalho
WORKDIR /app


# 2. Criar um usuário e grupo não-root dedicados
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

# 3. Otimizar cache de dependências: copiar só o necessário primeiro
COPY requirements.txt .
# Instalar dependências. 
RUN pip install -r requirements.txt

COPY app.py .

# 5. Mudar para o usuário não-root
USER appuser

# Expõe a porta que a aplicação usa
EXPOSE 5001

# 6. Usar "exec form" para CMD
CMD ["python", "./app.py"]