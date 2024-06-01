from pymongo import MongoClient

# Connection string
uri = "mongodb+srv://2100090162:manigaddam@deepsheild.kzgpo9p.mongodb.net/Movie_Library"

# Connect to the MongoDB cluster
client = MongoClient(uri)

# Select the database and collection
db = client.Movie_Library
collection = db.Movies

# Data to insert
movies_data =[
    {"movie_name": "Dune", "year": "2021", "genre": "Action, Adventure, Drama", "cast": "Timothée Chalamet, Rebecca Ferguson, Zendaya", "Rating": "TBD", "link": ""},
    {"movie_name": "No Time to Die", "year": "2021", "genre": "Action, Adventure, Thriller", "cast": "Daniel Craig, Ana de Armas, Léa Seydoux", "Rating": "TBD", "link": ""},
    {"movie_name": "Black Widow", "year": "2021", "genre": "Action, Adventure, Sci-Fi", "cast": "Scarlett Johansson, Florence Pugh, David Harbour", "Rating": "TBD", "link": ""},
    {"movie_name": "Shang-Chi and the Legend of the Ten Rings", "year": "2021", "genre": "Action, Adventure, Fantasy", "cast": "Simu Liu, Awkwafina, Tony Chiu-Wai Leung", "Rating": "TBD", "link": ""},
    {"movie_name": "The Suicide Squad", "year": "2021", "genre": "Action, Adventure, Comedy", "cast": "Margot Robbie, Idris Elba, John Cena", "Rating": "TBD", "link": ""},
    {"movie_name": "Godzilla vs. Kong", "year": "2021", "genre": "Action, Sci-Fi, Thriller", "cast": "Alexander Skarsgård, Millie Bobby Brown, Rebecca Hall", "Rating": "TBD", "link": ""},
    {"movie_name": "Mortal Kombat", "year": "2021", "genre": "Action, Adventure, Fantasy", "cast": "Lewis Tan, Jessica McNamee, Josh Lawson", "Rating": "TBD", "link": ""},
    {"movie_name": "F9: The Fast Saga", "year": "2021", "genre": "Action, Adventure, Crime", "cast": "Vin Diesel, Michelle Rodriguez, Charlize Theron", "Rating": "TBD", "link": ""},
    {"movie_name": "Jungle Cruise", "year": "2021", "genre": "Action, Adventure, Comedy", "cast": "Dwayne Johnson, Emily Blunt, Edgar Ramírez", "Rating": "TBD", "link": ""},
    {"movie_name": "Free Guy", "year": "2021", "genre": "Action, Adventure, Comedy", "cast": "Ryan Reynolds, Jodie Comer, Taika Waititi", "Rating": "TBD", "link": ""},
    {"movie_name": "Cruella", "year": "2021", "genre": "Comedy, Crime", "cast": "Emma Stone, Emma Thompson, Joel Fry", "Rating": "TBD", "link": ""},
    {"movie_name": "Venom: Let There Be Carnage", "year": "2021", "genre": "Action, Adventure, Sci-Fi", "cast": "Tom Hardy, Woody Harrelson, Michelle Williams", "Rating": "TBD", "link": ""},
    {"movie_name": "Space Jam: A New Legacy", "year": "2021", "genre": "Animation, Adventure, Comedy", "cast": "LeBron James, Don Cheadle, Cedric Joe", "Rating": "TBD", "link": ""},
    {"movie_name": "Wrath of Man", "year": "2021", "genre": "Action, Crime, Thriller", "cast": "Jason Statham, Holt McCallany, Josh Hartnett", "Rating": "TBD", "link": ""},
    {"movie_name": "A Quiet Place Part II", "year": "2021", "genre": "Drama, Horror, Sci-Fi", "cast": "Emily Blunt, Millicent Simmonds, Cillian Murphy", "Rating": "TBD", "link": ""},
    {"movie_name": "Luca", "year": "2021", "genre": "Animation, Adventure, Comedy", "cast": "Jacob Tremblay, Jack Dylan Grazer, Emma Berman", "Rating": "TBD", "link": ""},
    {"movie_name": "Zack Snyder's Justice League", "year": "2021", "genre": "Action, Adventure, Fantasy", "cast": "Henry Cavill, Ben Affleck, Gal Gadot", "Rating": "TBD", "link": ""},
    {"movie_name": "The Mitchells vs. the Machines", "year": "2021", "genre": "Animation, Adventure, Comedy", "cast": "Abbi Jacobson, Danny McBride, Maya Rudolph", "Rating": "TBD", "link": ""},
    {"movie_name": "The Tomorrow War", "year": "2021", "genre": "Action, Adventure, Sci-Fi", "cast": "Chris Pratt, Yvonne Strahovski, J.K. Simmons", "Rating": "TBD", "link": ""},
    {"movie_name": "Army of the Dead", "year": "2021", "genre": "Action, Crime, Horror", "cast": "Dave Bautista, Ella Purnell, Ana de la Reguera", "Rating": "TBD", "link": ""}
]








# Insert data into the collection
collection.insert_many(movies_data)




