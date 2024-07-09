FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt ./

RUN pip install --upgrade pip

RUN pip install -r "requirements.txt"

COPY . .

CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
