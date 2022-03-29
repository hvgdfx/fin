
FROM python:3.7-alpine
MAINTAINER 007

WORKDIR /work

COPY . .

# runtime environment
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
