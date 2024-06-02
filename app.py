from flask import Flask, render_template, session, flash, redirect, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = "1234"
app.config["MONGO_URI"] = "mongodb+srv://2100090162:manigaddam@deepsheild.kzgpo9p.mongodb.net/Movie_Library"
mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user_data = mongo.db.users.find_one({'email': email, 'password': password})
        if user_data:
            firstname = user_data['first_name']
            session['email'] = email
            session['name'] = firstname
            return redirect(url_for('home'))
        else:
            error = 'Invalid username or password'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('email', None)
    flash('You have been logged out', 'success')
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user_data = {
            'first_name': request.form.get('firstname'),
            'last_name': request.form.get('lastname'),
            'email': request.form.get('email'),
            'password': request.form.get('password')
        }
        mongo.db.users.insert_one(user_data)
        flash('SIGN UP SUCCESSFUL...YOU CAN NOW LOGIN HERE...', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/home')
def home():
    top_picks = mongo.db.Movies.find({"Rating": {"$gt": "8.5"}})
    ultratop = mongo.db.Movies.find({"Rating": {"$gt": "9"}})
    allmovies = mongo.db.Movies.find()
    watchlist = []
    if 'email' in session:
        watchlist = list(mongo.db.Watchlist.find({"email": session['email']}))
    return render_template('home.html', top_picks=top_picks, ultratop=ultratop, watchlist=watchlist, allmovies=allmovies)


@app.route('/tollywood')
def tollywood():
    tmovies=mongo.db.Movies.find()
    return render_template('tollywood.html',tmovies=tmovies)


@app.route('/hollywood')
def hollywood():
    return render_template('hollywood.html')


@app.route('/bollywood')
def bollywood():
    return render_template('bollywood.html')


@app.route('/kollywood')
def kollywood():
    return render_template('kollywood.html')
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if query:
        movies = list(mongo.db.Movies.find({
            "$or": [
                {"movie_name": {"$regex": query, "$options": "i"}},
                {"cast": {"$regex": query, "$options": "i"}},
                {"year": {"$regex": query, "$options": "i"}}
            ]
        }))
        return render_template('search_results.html', movies=movies, query=query)
    else:
        flash('Please enter a search query', 'warning')
        return redirect(url_for('home'))

@app.route('/search_results')
def search_results():
    avmovies = mongo.db.Movies.find()
    return render_template('search_results.html', avmovies=avmovies)

@app.route('/submit_movie', methods=['POST'])
def submit_movie():
    movie_name = request.form.get('movie_name')
    user_email = session.get('email')
    
    if movie_name and user_email:
        # Check if the movie already exists in the watchlist
        if mongo.db.Watchlist.find_one({"movie_name": movie_name, "email": user_email}):
            flash('Movie already added to the watchlist', 'warning')
        else:
            mongo.db.Watchlist.insert_one({'movie_name': movie_name, 'email': user_email})
            flash('Movie submitted successfully!', 'success')
    else:
        flash('Movie submission failed. Please Login!', 'danger')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
