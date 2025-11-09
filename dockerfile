FROM python:3.12-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY . .

RUN pip3 install -r requirements/dev.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]