from flask_app import app
from flask import render_template, redirect, request, session, flash
from datetime import datetime
from flask_app.models.recipe import Recipe
from flask_app.models.user import User



@app.route('/save/recipe', methods=['POST'])
def save_recipe():
    print(request.form)
    data = {
        'name': request.form['name'],
        'user_id': session['user'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'made_on': request.form['made_on'],
        'is_under_30': request.form['is_under_30']
    }
    Recipe.save(data)
    return redirect('/dashboard')

@app.route('/one/recipe/<int:recipe_id>')
def display_one(recipe_id):
    user_data = {
        'id': session['user']
    }
    recipe_data = {
        'id': recipe_id
    }
    active_recipe = Recipe.get_by_id(recipe_data)
    print(active_recipe)
    active_user = User.get_user_by_id(user_data)
    return render_template('one_recipe.html', active_user=active_user, active_recipe=active_recipe)

@app.route('/delete/<int:recipe_id>')
def delete_recipe(recipe_id):
    data = {
        'id': recipe_id
    }
    Recipe.delete(data)
    return redirect('/dashboard')

@app.route('/edit/<int:recipe_id>')
def display_edit_page(recipe_id):
    data = {
        'id': recipe_id
    }
    active_recipe = Recipe.get_by_id(data)
    print(active_recipe.made_on)
    return render_template('edit.html', active_recipe=active_recipe)

@app.route('/edit/recipe/<int:recipe_id>', methods=['POST'])
def edit_recipe(recipe_id):
    data = {
        'name': request.form['name'],
        'id': recipe_id,
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'made_on': request.form['made_on'],
        'is_under_30': request.form['is_under_30']
    }
    Recipe.edit(data)
    return redirect('/dashboard')