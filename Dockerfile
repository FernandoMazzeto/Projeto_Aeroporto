# Etapa 1: imagem base
FROM python:3.11-slim

# Etapa 2: diretório de trabalho
WORKDIR /app

# Etapa 3: copiar dependências e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 4: copiar o projeto para dentro do container
COPY app ./app

# Etapa 5: expor a porta da API
EXPOSE 5000

# Etapa 6: comando para rodar o servidor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
