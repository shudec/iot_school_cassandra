from EcoleIotCassandra import session

session.execute("CREATE KEYSPACE IF NOT EXISTS resto_NY WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor': 1};")
session.execute("USE resto_NY;")

session.execute(""" CREATE TABLE IF NOT EXISTS Restaurant (
   id INT, Name VARCHAR, borough VARCHAR, BuildingNum VARCHAR, Street VARCHAR,
   ZipCode INT, Phone text, CuisineType VARCHAR,
   PRIMARY KEY ( id )
 ) ; """)

session.execute("CREATE INDEX IF NOT EXISTS fk_Restaurant_cuisine ON Restaurant ( CuisineType ) ;")

session.execute("""CREATE TABLE IF NOT EXISTS Inspection (
   idRestaurant INT, InspectionDate date, ViolationCode VARCHAR,
   ViolationDescription VARCHAR, CriticalFlag VARCHAR, Score INT, GRADE VARCHAR,
   PRIMARY KEY ( idRestaurant, InspectionDate )
 ) ;""")

session.execute("CREATE INDEX IF NOT EXISTS fk_Inspection_Restaurant ON Inspection ( Grade ) ; ")