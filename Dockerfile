FROM python:3.12-alpine
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3", "-m", "gunicorn", "-b", "0.0.0.0", "main:app"]
