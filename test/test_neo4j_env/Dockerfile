FROM neo4j:4.2.0

# 设置 Neo4j 监听所有网络接口
ENV NEO4J_dbms_connector_bolt_listen__address=0.0.0.0:7687
ENV NEO4J_dbms_connector_http_listen__address=0.0.0.0:7474
ENV NEO4J_dbms_connector_https_listen__address=0.0.0.0:7473

# 设置管理员密码（可根据需要修改）
ENV NEO4J_AUTH=neo4j/123

# CMD ["sh", "-c", "while true; do sleep 1; done"]

