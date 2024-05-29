from flask import Flask, render_template, session, url_for, flash, redirect, request
from flask_pymongo import PyMongo


app=Flask(__name__)
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
            session['name']=firstname
            return redirect(url_for('home'))
        else:
            error = 'Invalid username or password'

    return render_template('login.html', error=error)

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

        flash('SIGN UP SUCCESSFUL...YOU CAN NOW LOGIN HERE...',
              'success')  # Flash success message
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/logout')
def logout():
    session.pop('email', None)  
    flash('You have been logged out', 'success') 
    return redirect(url_for('login'))


if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)