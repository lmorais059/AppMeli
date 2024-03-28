# Use a imagem oficial do Python
FROM python:3.9-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie os arquivos necessários para o contêiner
COPY requirements.txt ./
COPY app.py ./
COPY main.py ./
COPY test_routes.py ./


# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta 5000 (porta padrão do Flask)
EXPOSE 5000

# Comando para iniciar a aplicação Flask quando o contêiner for executado
CMD ["python", "app.py"]
