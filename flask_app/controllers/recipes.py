from flask_app import app
from flask import render_template, redirect, request, session, flash
from datetime import datetime
from flask_app.models.recipe import Recipe


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