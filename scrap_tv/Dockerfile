FROM mcr.microsoft.com/playwright/python:v1.45.0-jammy

# Diretório de trabalho
WORKDIR /app

# Copia o código
COPY app.py /app/app.py

# Instala dependências
RUN pip install --no-cache-dir fastapi==0.115.0 "uvicorn[standard]"==0.32.0 openpyxl==3.1.5

# Cria pasta para Excel
RUN mkdir -p /data

# Porta exposta
EXPOSE 8000

# Comando para rodar a API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1", "--proxy-headers"]