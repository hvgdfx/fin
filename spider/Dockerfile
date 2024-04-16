
FROM python:3.9-alpine

WORKDIR /work

COPY . .

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories \
    && pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple/ \
    && pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/ \
    && echo "alias ll='ls -l'" >> ~/.bashrc \
    && cat /work/spider/all_spider/crontab >> /etc/crontabs/root


#CMD ["python3", "/work/spider/utils/ck_utils.py"]
#CMD ["python3", "/work/spider/job_shedule.py"]
#CMD ["python3", "/work/spider/request_test.py"]
#CMD ["python3", "/work/spider/db_create/create_table.py"]
CMD ["sh", "-c", "while true; do sleep 1; done"]
