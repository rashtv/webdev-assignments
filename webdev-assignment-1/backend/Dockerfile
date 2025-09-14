FROM python:3.12-slim-bookworm


WORKDIR /src

COPY requirements.txt /src/

RUN pip install -r requirements.txt

COPY . /src

CMD ["python3", "app/main.py"]
