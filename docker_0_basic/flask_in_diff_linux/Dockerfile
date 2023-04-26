FROM python:3.7-alpine
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
WORKDIR /
COPY app.py app.py
RUN pip3 install -i https://mirrors.aliyun.com/pypi/simple/ flask
CMD ["flask", "run", "--port", "8080"]