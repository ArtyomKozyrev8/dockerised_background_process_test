FROM python:3.7-alpine

WORKDIR /usr/src/dockerised_background_process_test

ENV TZ=Europe/Moscow

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "main.py" ]