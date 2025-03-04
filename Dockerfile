
FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade --no-cache-dir "pip<24.1" setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=src/saludtech/api/__init__.py
ENV PYTHONPATH=/app/src

EXPOSE 5000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]

