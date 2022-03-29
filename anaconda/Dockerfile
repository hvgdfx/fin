

FROM continuumio/anaconda3
WORKDIR /work

COPY . .

# 配置源
RUN conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
RUN conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
RUN conda config --set show_channel_urls yes

# 创建python环境
RUN conda create --name anaconda3_env python=3.7
RUN /bin/bash -c conda activate anaconda3_env
RUN FOR /F "delims=~" %f in (requirements.txt) DO conda install --yes "%f"

