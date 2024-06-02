from pymongo import MongoClient

# Connection string
uri = "mongodb+srv://2100090162:manigaddam@deepsheild.kzgpo9p.mongodb.net/Movie_Library"

# Connect to the MongoDB cluster
client = MongoClient(uri)

# Select the database and collection
db = client.Movie_Library
collection = db.Movies

# Define the filter to match documents where the Cast field contains "Christian Bale"
filter_criteria = {"cast": {"$regex": ".*Hrithik Roshan*"}}

# Define the update operation to set the Link field
update_operation = {"$set": {"link": "https://img.indiaforums.com/media/640x0/49/6405-hrithik-roshan.jpg"}}

# Update the documents matching the filter criteria
result = collection.update_many(filter_criteria, update_operation)

# Output the number of documents updated
print("Number of documents updated:", result.modified_count)
