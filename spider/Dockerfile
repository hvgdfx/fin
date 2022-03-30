
FROM python:3.9-alpine
MAINTAINER 007

WORKDIR /work

COPY ./requirements.txt .

# apk repository
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories

# runtime environment
RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple/
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/


CMD ["python3", "/work/spdier/spider/utils/ck_utils"]
