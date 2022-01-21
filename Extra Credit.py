import pymongo
connection = pymongo.MongoClient("class-mongodb.cims.nyu.edu", 27017,
                                username="as12936",
                                password="B7JhKLyR",
                                authSource="as12936")
collection = connection["as12936"]["listings"]

# the collection variable will be a reference to your collection
docs = collection.find()

for i in docs:
    if i.get("beds") != "":
        if (i.get("neighbourhood_cleansed") == "Pacific Heights" and float(i.get("beds"))>float(2)):
            print(str(i.get("name")) + "," + str(i.get("beds")) + "," + str(i.get("neighbourhood_cleansed")) + "," + str(i.get("review_scores_rating")) + "," + str(i.get("price")))
