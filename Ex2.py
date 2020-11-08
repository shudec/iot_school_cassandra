from EcoleIotCassandra import session

session.execute("USE resto_NY;")

# 1. Print first ten restaurants
resto = session.execute("select * from restaurant")
print(resto[:10])

# 2. Print names of restaurants
# 3. Print the name and the borough of restaurant `41569764`
# 4. Print dates and grades of inspections of restaurant `41569764`
# 5. Print names of restaurant with french cooking
# 6. Print names of restaurant in Brooklyn
# 7. Print grades and scores given for an inspection for restaurant no. `41569764` with a score of at least 10.
# 8. Print grades ( not null) of inspections with a score higher than 30.
# 9. Print number of rows returned by the previous query.
