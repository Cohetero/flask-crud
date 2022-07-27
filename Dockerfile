FROM python:3.11.0b4-alpine3.16

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 3000

CMD ["python", "src/app.py"]
