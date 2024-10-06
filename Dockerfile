FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip3 install --no-cache-dir -r requirements.txt
RUN chmod +x run.sh
CMD [ "bash","run.sh" ]