# iot_school_cassandra

## Ex 0: database initialization
* Execute `docker-compose up -d` to start Cassandra
* Execute `python InitDB.py` to create tables and indexes
* Connect to Cassandra with `docker exec -it iot_school_cassandra_cassandra_1 cqlsh` and verify that the tables are created with cql commands (https://cassandra.apache.org/doc/latest/cql/index.html)

## Ex 1: Inject data
* Unzip data.zip and execute:
  * `docker cp restaurants.csv iot_school_cassandra_cassandra_1:/`
  * `docker cp restaurants_inspections.csv iot_school_cassandra_cassandra_1:/`
* Import data in tables with cqlsh
```
use resto_NY;
COPY Restaurant (id, name, borough, buildingnum, street, zipcode, phone, cuisinetype) FROM '/restaurants.csv' WITH DELIMITER=',';
COPY Inspection (idrestaurant, inspectiondate, violationcode, violationdescription, criticalflag, score, grade) FROM '/restaurants_inspections.csv' WITH DELIMITER=',';
```
* Count the number of restaurants in the table `Restaurant`
* Count the number of inspection in the table `Inspection`

## Ex 2: request data with python
1. Print first ten restaurants
2. Print names of restaurants
3. Print the name and the borough of restaurant `41569764`
4. Print dates and grades of inspections of restaurant `41569764`
5. Print names of restaurant with french cooking
6. Print names of restaurant in Brooklyn
7. Print grades and scores given for an inspection for restaurant no. `41569764` with a score of at least 10.
8. Print grades ( not null) of inspections with a score higher than 30.
9. Print number of rows returned by the previous query.