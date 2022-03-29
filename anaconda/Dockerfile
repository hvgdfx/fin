

FROM continuumio/anaconda3
WORKDIR /work

# timezone
RUN apk add -U tzdata && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && apk del tzdata

COPY . .

RUN conda create --name anaconda3_env python=3.7
RUN conda activate anaconda3_env
RUN FOR /F "delims=~" %f in (requirements.txt) DO conda install --yes "%f"

