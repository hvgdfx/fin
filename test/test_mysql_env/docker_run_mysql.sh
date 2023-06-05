
container_name="test_mysql_env"

docker ps -a | grep $container_name | awk '{print $1}' | xargs docker rm -f
docker run -itd \
  --name $container_name \
  -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=root \
  mysql/mysql-server:8.0



#sql
#create user 'test'@'%' identified by 'test';
#ALTER USER 'test' IDENTIFIED WITH mysql_native_password BY 'test';