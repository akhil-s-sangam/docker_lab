FROM python:3.10-slim

WORKDIR /app

# Copy requirements from src folder
COPY src/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code
COPY src/ .

CMD ["python", "main.py"]
