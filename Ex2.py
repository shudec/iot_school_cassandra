from EcoleIotCassandra import session

session.execute("USE resto_NY;")

# 1. Print top ten restaurants
restos = session.execute("select * from restaurant")
print("\n1. Top ten restaurant :")
for resto in restos[:10]:
    print("  - restaurant #{}: {}".format(resto[0], resto))

# 2. Print top ten names of restaurants
resto_names = session.execute("select name from restaurant")
print("\n2. Top ten restaurant names:")
for resto_name in resto_names[:10]:
    print("  - {}".format(resto_name[0]))

# 3. Print the name and the borough of restaurant `41569764`
resto_41569764 = session.execute("select name, borough from restaurant where id=41569764")
print("\n3. Name and borough of restaurant `41569764`:")
print("  - name: {}".format(resto_41569764[0][0]))
print("  - borough: {}".format(resto_41569764[0][1]))

# 4. Print dates and grades of inspections of restaurant `41569764`
inspections_resto_41569764 = session.execute("select inspectiondate, grade from inspection where idrestaurant=41569764")
print("\n4. Dates and grades of restaurant `41569764`:")
for inspect in inspections_resto_41569764:
    print("  - date: {}, grade: {}".format(inspect[0], inspect[1]))

# 5. Print top ten names of restaurant with french cooking
french_restaurant = session.execute("select name from restaurant where cuisinetype='French'")
print("\n5. Name of french restaurants:")
for resto in french_restaurant[:10]:
    print("  - name: {}".format(resto[0]))

# 6. Print top ten names of restaurant in Brooklyn
""" ALLOW FILTERING is necessary due to the lack of borough index, so the number of results is not predictable by Cassandra """
brooklyn_restaurant = session.execute("select name from restaurant where borough='BROOKLYN' ALLOW FILTERING")
print("\n6. Name of Brooklyn restaurants:")
for resto in brooklyn_restaurant[:10]:
    print("  - name: {}".format(resto[0]))

# 7. Print grades and scores given for an inspection for restaurant no. `41569764` with a score of at least 10.
inspections_resto_41569764 = session.execute("select grade, score from inspection where idrestaurant=41569764 and score>9 ALLOW FILTERING")
print("\n7. Grades and scores given for an inspection for restaurant no. `41569764` with a score of at least 10:")
for inspect in inspections_resto_41569764:
    print("  - grade: {}, score: {}".format(inspect[0], inspect[1]))

# 8. Print grades ( not null) of inspections with a score higher than 30.
high_scores = session.execute("select grade from inspection where score>30 ALLOW FILTERING")
print("grades (not null) of inspections with a score higher than 30")
for score in high_scores:
    if score[0] is not None: print("  - grade: {}".format(score[0]))

# 9. Print number of rows returned by the previous query.
high_scores_count = session.execute("select count(*) from inspection where score>30 ALLOW FILTERING")
print("\nnumber of grades (not null) of inspections with a score higher than 30")
print("  - number of grades: {}".format(high_scores_count[0][0]))