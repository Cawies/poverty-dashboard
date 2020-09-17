FROM python:3.7-slim-buster

WORKDIR /app
ADD ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
ADD . /app

EXPOSE 8050

ENTRYPOINT ["python"]

CMD ["app.py"]