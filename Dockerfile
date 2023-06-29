FROM mysql:8.0

ENV MYSQL_ROOT_PASSWORD=1234

EXPOSE 3306

COPY ./schema.sql /docker-entrypoint-initdb.d/

CMD ["mysqld"]
