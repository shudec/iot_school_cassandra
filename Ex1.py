from EcoleIotCassandra import session

session.execute("USE resto_NY;")

# 1. Count the number of restaurants in the table `Restaurant`
nb_restos = session.execute("select count(*) from restaurant")
print(f"\n1. Nb of restaurants : {nb_restos}")

# 2. Count the number of inspection in the table `Inspection`
nb_inspections = session.execute("select count(*) from inspection")
print(f"\n1. Nb of inspections : {nb_inspections}")