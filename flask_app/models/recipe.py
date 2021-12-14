from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.made_on = data['made_on']
        self.is_under_30 = data['is_under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (user_id, name, description, instructions, made_on, is_under_30) VALUES(%(user_id)s, %(name)s, %(description)s, %(instructions)s, %(made_on)s, %(is_under_30)s);"
        recipe_id = connectToMySQL('recipes').query_db(query, data)
        return recipe_id

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM recipes WHERE recipes.id = %(id)s;"
        recipe = connectToMySQL('recipes').query_db(query, data)
        if recipe:
            return cls(recipe[0])
        return False

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes"
        recipes_in_db = connectToMySQL('recipes').query_db(query)
        recipes_cls = []
        for recipe in recipes_in_db:
            recipes_cls.append(cls(recipe))
        return recipes_cls

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE recipes.id = %(id)s"
        result = connectToMySQL('recipes').query_db(query, data)
        return result

    @classmethod
    def edit(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, made_on = %(made_on)s, is_under_30 = %(is_under_30)s  WHERE id = %(id)s;"
        result = connectToMySQL('recipes').query_db(query, data)
        return result