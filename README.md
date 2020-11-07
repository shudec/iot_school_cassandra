# iot_school_cassandra

## Ex 0: database initialization
* Execute `docker-compose up -d` to start Cassandra
* Execute `python InitDB.py` to create tables and indexes
* Connect to Cassandra with `docker exec -it iot_school_cassandra_cassandra_1 cqlsh` and verify that the tables are created with cql commands (https://cassandra.apache.org/doc/latest/cql/index.html)

## Ex 1: Inject data
* Unzip data.zip and execute:
  * `docker cp restaurants.csv iot_school_cassandra_cassandra_1:/`
  * `docker cp restaurants_inspections.csv iot_school_cassandra_cassandra_1:/`