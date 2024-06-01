from pymongo import MongoClient

# Connection string
uri = "mongodb+srv://2100090162:manigaddam@deepsheild.kzgpo9p.mongodb.net/Movie_Library"

# Connect to the MongoDB cluster
client = MongoClient(uri)

# Select the database and collection
db = client.Movie_Library
collection = db.Movies

# Aggregate pipeline to find and remove duplicates
pipeline = [
    {"$group": {"_id": "$movie_name", "unique_ids": {"$addToSet": "$_id"}, "count": {"$sum": 1}}},
    {"$match": {"count": {"$gt": 1}}},
]

# Iterate over the duplicates and delete them
for doc in collection.aggregate(pipeline):
    # Keep one document with the smallest _id and delete the rest
    delete_ids = doc['unique_ids'][1:]
    collection.delete_many({"_id": {"$in": delete_ids}})

print("Duplicate documents based on 'movie_name' field have been deleted.")
