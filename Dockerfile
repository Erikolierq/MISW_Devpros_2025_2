
FROM python:3.13

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade --no-cache-dir "pip<24.1" setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=src/saludtech/api/__init__.py

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
