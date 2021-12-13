from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
from datetime import datetime

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'user' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        data = {
            'id': session['user']
        }
        active_user = User.get_user_by_id(data)
        all_recipes = Recipe.get_all()
        return render_template('dashboard.html', active_user=active_user, all_recipes=all_recipes)
    else:
        flash("You are not logged in!", 'not-loggedin')
        return redirect('/')

@app.route('/register/user', methods=['POST'])
def register_user():
    if not User.validate_registation(request.form):
        return redirect('/')
    print(request.form)
    data = {
        'first_name': request.form['first_name'], 
        'last_name': request.form['last_name'], 
        'email': request.form['email'], 
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    session['user'] = User.save(data)
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    if User.validate_login(request.form):
        session['user'] = User.validate_login(request.form)
        return redirect('/dashboard')
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/create')
def create():
    data = {
        'id': session['user']
    }
    active_user = User.get_user_by_id(data)
    return render_template('create_recipe.html', active_user=active_user)