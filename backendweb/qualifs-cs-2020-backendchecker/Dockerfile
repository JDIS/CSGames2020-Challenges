FROM python:3.7-alpine3.9
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
COPY ./app .
CMD ['cd', 'app']
EXPOSE 80
ENV FLASK_APP=app.py
CMD [ "python", "app.py" ]