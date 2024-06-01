from pymongo import MongoClient

# Connection string
uri = "mongodb+srv://2100090162:manigaddam@deepsheild.kzgpo9p.mongodb.net/Movie_Library"

# Connect to the MongoDB cluster
client = MongoClient(uri)

# Select the database and collection
db = client.Movie_Library
collection = db.Movies

# Delete documents without the "year" field
deleted_docs = collection.delete_many({"year": {"$exists": False}})

print(f"{deleted_docs.deleted_count} documents without the 'year' field have been deleted.")
