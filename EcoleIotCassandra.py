from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster

#ap = PlainTextAuthProvider(username="cassandra", password="cassandra")
#cluster = Cluster(auth_provider=ap)
cluster = Cluster()
session = cluster.connect()