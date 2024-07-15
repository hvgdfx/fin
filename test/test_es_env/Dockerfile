FROM elasticsearch:8.14.3

WORKDIR /data
ADD . /data

# 生成私钥文件
# 生成证书签名请求文件（CSR）
# 生成自签名证书
# 生成 JKS 文件
# 将 PKCS12 文件导入到 JKS

# RUN openssl genrsa -out server.key 2048 \
#     && openssl req -new -key server.key -out server.csr \
    # && openssl req -new -key server.key -out server.csr -config openssl.cnf

#     && openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt \
#     && openssl pkcs12 -export -in server.crt -inkey server.key -out server.p12 -name "server" \
#     && /usr/share/elasticsearch/jdk/bin/keytool -importkeystore -srckeystore keystore.jks -destkeystore keystore.jks -deststoretype pkcs12 

# /usr/share/elasticsearch/jdk/bin/keytool -importkeystore -srckeystore server.p12 -srcstoretype PKCS12 -destkeystore keystore.jks -deststoretype JKS

CMD ["sh", "-c", "while true; do sleep 1; done"]