
FROM python:3.9-alpine
MAINTAINER 007

WORKDIR /work

COPY . .

# apk repository
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories

# runtime environment
RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple/
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/


#CMD ["python3", "/work/spider/utils/ck_utils.py"]
#CMD ["python3", "/work/spider/job_shedule.py"]
#CMD ["python3", "/work/spider/request_test.py"]
#CMD ["python3", "/work/spider/db_create/create_table.py"]
CMD ["sh", "-c", "while true; do sleep 1; done"]
