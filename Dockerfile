FROM python:3.9

WORKDIR /ExchangeAPI

COPY ./requirements.txt /ExchangeAPI/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /ExchangeAPI/requirements.txt

COPY ./app /ExchangeAPI/app

COPY ./Documents /ExchangeAPI/Documents

COPY ./README.md /ExchangeAPI/README.md

CMD ["uvicorn", "app.main:api", "--host", "0.0.0.0", "--port", "8080"]