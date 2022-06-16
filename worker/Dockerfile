FROM python:3.10.4
WORKDIR /worker
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["celery", "-A", "main", "worker", "--loglevel=INFO", "--pool=gevent", "--concurrency=10"]