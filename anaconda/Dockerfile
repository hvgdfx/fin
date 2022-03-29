

FROM continuumio/anaconda3
WORKDIR /work

COPY . .

RUN conda create --name anaconda3_env python=3.7
RUN conda activate anaconda3_env
RUN FOR /F "delims=~" %f in (requirements.txt) DO conda install --yes "%f"

