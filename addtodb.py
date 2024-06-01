from pymongo import MongoClient

# Connection string
uri = "mongodb+srv://2100090162:manigaddam@deepsheild.kzgpo9p.mongodb.net/Movie_Library"

# Connect to the MongoDB cluster
client = MongoClient(uri)

# Select the database and collection
db = client.Movie_Library
collection = db.Movies

# Data to insert
movies_data = [
    # Rajkumar movies
    {"movie_name": "Bangarada Manushya", "year": "1972", "genre": "Drama", "cast": "Rajkumar", "Rating": "8.8", "link": "https://example.com/bangarada-manushya"},
    {"movie_name": "Shankar Guru", "year": "1978", "genre": "Drama", "cast": "Rajkumar", "Rating": "7.7", "link": "https://example.com/shankar-guru"},
    {"movie_name": "Haalu Jenu", "year": "1982", "genre": "Drama", "cast": "Rajkumar", "Rating": "8.1", "link": "https://example.com/haalu-jenu"},
    {"movie_name": "Kasturi Nivasa", "year": "1971", "genre": "Drama, Family", "cast": "Rajkumar", "Rating": "8.5", "link": "https://example.com/kasturi-nivasa"},
    {"movie_name": "Bhakta Prahlada", "year": "1983", "genre": "Drama, Family", "cast": "Rajkumar", "Rating": "8.2", "link": "https://example.com/bhakta-prahlada"},
    {"movie_name": "Nagarahavu", "year": "1972", "genre": "Drama, Fantasy", "cast": "Rajkumar", "Rating": "8.1", "link": "https://example.com/nagarahavu"},
    {"movie_name": "Babruvahana", "year": "1977", "genre": "Drama, Fantasy", "cast": "Rajkumar", "Rating": "7.7", "link": "https://example.com/babruvahana"},
    {"movie_name": "Mayura", "year": "1975", "genre": "Drama", "cast": "Rajkumar", "Rating": "7.5", "link": "https://example.com/mayura"},
    {"movie_name": "Ranadheera Kanteerava", "year": "1960", "genre": "Drama, History", "cast": "Rajkumar", "Rating": "7.3", "link": "https://example.com/ranadheera-kanteerava"},
    {"movie_name": "Sampathige Savaal", "year": "1974", "genre": "Action, Drama", "cast": "Rajkumar", "Rating": "7.1", "link": "https://example.com/sampathige-savaal"},
    
    # Vishnuvardhan movies
    {"movie_name": "Nagarahavu", "year": "1972", "genre": "Action, Drama, Romance", "cast": "Vishnuvardhan", "Rating": "7.2", "link": "https://example.com/nagarahavu"},
    {"movie_name": "Muthina Haara", "year": "1990", "genre": "Drama, History, Romance", "cast": "Vishnuvardhan", "Rating": "8.9", "link": "https://example.com/muthina-haara"},
    {"movie_name": "Hombisilu", "year": "1978", "genre": "Drama", "cast": "Vishnuvardhan", "Rating": "7.7", "link": "https://example.com/hombisilu"},
    {"movie_name": "Bandhana", "year": "1984", "genre": "Drama, Romance", "cast": "Vishnuvardhan", "Rating": "8.4", "link": "https://example.com/bandhana"},
    {"movie_name": "Yajamana", "year": "2000", "genre": "Action, Drama", "cast": "Vishnuvardhan", "Rating": "8.1", "link": "https://example.com/yajamana"},
    {"movie_name": "Nagarahaavu", "year": "2002", "genre": "Action, Drama, Romance", "cast": "Vishnuvardhan", "Rating": "7.2", "link": "https://example.com/nagarahaavu"},
    {"movie_name": "Mutha Mestri", "year": "1993", "genre": "Action, Drama", "cast": "Vishnuvardhan", "Rating": "7.6", "link": "https://example.com/mutha-mestri"},
    {"movie_name": "Suprabhata", "year": "1988", "genre": "Drama, Family", "cast": "Vishnuvardhan", "Rating": "8.0", "link": "https://example.com/suprabhata"},
    {"movie_name": "Nishkarsha", "year": "1993", "genre": "Action, Crime, Drama", "cast": "Vishnuvardhan", "Rating": "7.4", "link": "https://example.com/nishkarsha"},
    {"movie_name": "Kotigobba", "year": "2001", "genre": "Action, Drama, Mystery", "cast": "Vishnuvardhan", "Rating": "7.1", "link": "https://example.com/kotigobba"},
    
    # Ambareesh movies
    {"movie_name": "Antha", "year": "1981", "genre": "Action, Drama, Romance", "cast": "Ambareesh", "Rating": "8.3", "link": "https://example.com/antha"},
    {"movie_name": "Chakravyuha", "year": "1983", "genre": "Action, Drama, Thriller", "cast": "Ambareesh", "Rating": "8.2", "link": "https://example.com/chakravyuha"},
    {"movie_name": "Naagarahaavu", "year": "1972", "genre": "Drama, Romance", "cast": "Ambareesh", "Rating": "7.4", "link": "https://example.com/naagarahaavu"},
    {"movie_name": "Ranganayaki", "year": "1981", "genre": "Drama, Romance", "cast": "Ambareesh", "Rating": "7.3", "link": "https://example.com/ranganayaki"},
    {"movie_name": "Olavina Udugore", "year": "1977", "genre": "Drama, Family, Romance", "cast": "Ambareesh", "Rating": "7.1", "link": "https://example.com/olavina-udugore"},
    {"movie_name": "Paduvaralli Pandavaru", "year": "1978","genre": "Drama, Family", "cast": "Ambareesh", "Rating": "6.8", "link": "https://example.com/paduvaralli-pandavaru"},
    {"movie_name": "Hrudaya Haadithu", "year": "1981", "genre": "Drama, Romance", "cast": "Ambareesh", "Rating": "6.7", "link": "https://example.com/hrudaya-haadithu"},
    {"movie_name": "Shubhamangala", "year": "1975", "genre": "Drama, Family", "cast": "Ambareesh", "Rating": "6.5", "link": "https://example.com/shubhamangala"},
    {"movie_name": "Devara Gudi", "year": "1975", "genre": "Drama, Romance", "cast": "Ambareesh", "Rating": "6.3", "link": "https://example.com/devara-gudi"},
    {"movie_name": "Huliya Haalina Mevu", "year": "1979", "genre": "Drama, Family", "cast": "Ambareesh", "Rating": "6.1", "link": "https://example.com/huliya-haalina-mevu"},
    
    # Puneeth Rajkumar movies
    {"movie_name": "Milana", "year": "2007", "genre": "Drama, Romance", "cast": "Puneeth Rajkumar", "Rating": "7.8", "link": "https://example.com/milana"},
    {"movie_name": "Raajakumara", "year": "2017", "genre": "Drama", "cast": "Puneeth Rajkumar", "Rating": "8.6", "link": "https://example.com/raajakumara"},
    {"movie_name": "Doddmane Hudga", "year": "2016", "genre": "Action, Drama", "cast": "Puneeth Rajkumar", "Rating": "7.3", "link": "https://example.com/doddmane-hudga"},
    {"movie_name": "Appu", "year": "2002", "genre": "Action, Drama", "cast": "Puneeth Rajkumar", "Rating": "7.2", "link": "https://example.com/appu"},
    {"movie_name": "Raj", "year": "2009", "genre": "Action, Drama", "cast": "Puneeth Rajkumar", "Rating": "7.1", "link": "https://example.com/raj"},
    {"movie_name": "Vamshi", "year": "2008", "genre": "Action, Drama", "cast": "Puneeth Rajkumar", "Rating": "6.8", "link": "https://example.com/vamshi"},
    {"movie_name": "Bhagyavantha", "year": "1981", "genre": "Drama", "cast": "Puneeth Rajkumar", "Rating": "6.7", "link": "https://example.com/bhagyavantha"},
    {"movie_name": "Prithvi", "year": "2010", "genre": "Action, Drama", "cast": "Puneeth Rajkumar", "Rating": "6.5", "link": "https://example.com/prithvi"},
    {"movie_name": "Chakravyuha", "year": "1983", "genre": "Action, Drama", "cast": "Puneeth Rajkumar", "Rating": "6.3", "link": "https://example.com/chakravyuha"},
    {"movie_name": "Anjani Putra", "year": "2017", "genre": "Action, Drama", "cast": "Puneeth Rajkumar", "Rating": "6.1", "link": "https://example.com/anjani-putra"},
    
    # Upendra movies
    {"movie_name": "A", "year": "1998", "genre": "Drama, Romance", "cast": "Upendra", "Rating": "7.7", "link": "https://example.com/a"},
    {"movie_name": "Upendra", "year": "1999", "genre": "Drama, Mystery, Thriller", "cast": "Upendra", "Rating": "7.4", "link": "https://example.com/upendra"},
    {"movie_name": "OM", "year": "1996", "genre": "Action, Crime, Drama", "cast": "Upendra", "Rating": "7.2", "link": "https://example.com/om"},
    {"movie_name": "Super", "year": "2010", "genre": "Action, Comedy, Drama", "cast": "Upendra", "Rating": "6.9", "link": "https://example.com/super"},
    {"movie_name": "Raa", "year": "2001", "genre": "Action, Crime, Drama", "cast": "Upendra", "Rating": "6.7", "link": "https://example.com/raa"},
    {"movie_name": "Kanyadanam", "year": "1998", "genre": "Drama, Romance", "cast": "Upendra", "Rating": "6.5", "link": "https://example.com/kanyadanam"},
    {"movie_name": "Brahma", "year": "2014", "genre": "Action, Comedy", "cast": "Upendra", "Rating": "6.3", "link": "https://example.com/brahma"},
    {"movie_name": "Gokarna", "year": "2003", "genre": "Drama, Romance", "cast": "Upendra", "Rating": "6.1", "link": "https://example.com/gokarna"},
    {"movie_name": "Aishwarya", "year": "2006", "genre": "Comedy, Romance", "cast": "Upendra", "Rating": "5.9", "link": "https://example.com/aishwarya"},
    {"movie_name": "Swasthik", "year": "1999", "genre": "Action, Crime, Drama", "cast": "Upendra", "Rating": "5.7", "link": "https://example.com/swasthik"},
    
    # Darshan movies
    {"movie_name": "Kariya", "year": "2003", "genre": "Action, Drama", "cast": "Darshan", "Rating": "7.2", "link": "https://example.com/kariya"},
    {"movie_name": "Majestic", "year": "2002", "genre": "Action, Drama", "cast": "Darshan", "Rating": "7.0", "link": "https://example.com/majestic"},
    {"movie_name": "Navagraha","year": "2008", "genre": "Action, Thriller", "cast": "Darshan", "Rating": "6.8", "link": "https://example.com/navagraha"},
    {"movie_name": "Shourya", "year": "2004", "genre": "Action, Drama", "cast": "Darshan", "Rating": "6.6", "link": "https://example.com/shourya"},
    {"movie_name": "Dinakara", "year": "2002", "genre": "Action, Drama", "cast": "Darshan", "Rating": "6.4", "link": "https://example.com/dinakara"},
    {"movie_name": "Gaja", "year": "2008", "genre": "Action, Drama", "cast": "Darshan", "Rating": "6.2", "link": "https://example.com/gaja"},
    {"movie_name": "Viraat", "year": "2016", "genre": "Action, Drama", "cast": "Darshan", "Rating": "6.0", "link": "https://example.com/viraat"},
    {"movie_name": "Anatharu", "year": "2007", "genre": "Action, Drama", "cast": "Darshan", "Rating": "5.8", "link": "https://example.com/anatharu"},
    {"movie_name": "Arjun", "year": "2008", "genre": "Action, Drama", "cast": "Darshan", "Rating": "5.6", "link": "https://example.com/arjun"},
    {"movie_name": "Kalasipalya", "year": "2005", "genre": "Action, Drama", "cast": "Darshan", "Rating": "5.4", "link": "https://example.com/kalasipalya"},
    {"movie_name": "Porki", "year": "2010", "genre": "Action, Drama", "cast": "Darshan", "Rating": "5.2", "link": "https://example.com/porki"},
    {"movie_name": "Saarathi", "year": "2011", "genre": "Action, Drama", "cast": "Darshan", "Rating": "5.0", "link": "https://example.com/saarathi"},
    
    # Yash movies
    {"movie_name": "KGF Chapter 1", "year": "2018", "genre": "Action, Drama", "cast": "Yash", "Rating": "8.2", "link": "https://example.com/kgf-chapter-1"},
    {"movie_name": "Mr. and Mrs. Ramachari", "year": "2014", "genre": "Action, Drama, Romance", "cast": "Yash", "Rating": "7.7", "link": "https://example.com/mr-and-mrs-ramachari"},
    {"movie_name": "Masterpiece", "year": "2015", "genre": "Action, Crime, Drama", "cast": "Yash", "Rating": "7.4", "link": "https://example.com/masterpiece"},
    {"movie_name": "Gajakesari", "year": "2014", "genre": "Action, Drama", "cast": "Yash", "Rating": "7.1", "link": "https://example.com/gajakesari"},
    {"movie_name": "Rocky", "year": "2008", "genre": "Action, Drama", "cast": "Yash", "Rating": "6.8", "link": "https://example.com/rocky"},
    {"movie_name": "Googly", "year": "2013", "genre": "Comedy, Romance", "cast": "Yash", "Rating": "6.6", "link": "https://example.com/googly"},
    {"movie_name": "Santhu Straight Forward", "year": "2016", "genre": "Action, Drama, Romance", "cast": "Yash", "Rating": "6.4", "link": "https://example.com/santhu-straight-forward"},
    {"movie_name": "Chandra", "year": "2013", "genre": "Action, Drama", "cast": "Yash", "Rating": "6.2", "link": "https://example.com/chandra"},
    {"movie_name": "Raja Huli", "year": "2013", "genre": "Action, Comedy", "cast": "Yash", "Rating": "6.0", "link": "https://example.com/raja-huli"},
    {"movie_name": "Kirataka", "year": "2011", "genre": "Action, Comedy, Drama", "cast": "Yash", "Rating": "5.8", "link": "https://example.com/kirataka"}
]





# Insert data into the collection
collection.insert_many(movies_data)




