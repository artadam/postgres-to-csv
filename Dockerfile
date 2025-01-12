FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#RUN apt-get update && apt-get install -y --no-install-recommends \
#    gcc libpq-dev && \
#    apt-get clean && \
#    rm -rf /var/lib/apt/lists/*

COPY ./app /app

ENTRYPOINT ["python", "main.py"]
