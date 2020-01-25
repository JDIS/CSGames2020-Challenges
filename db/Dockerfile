FROM python:3.7-alpine3.9

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

EXPOSE 5000

COPY . .

CMD [ "python", "main.py" ]