import os
import re
from flask import Flask, render_template, redirect, request, url_for, session, flash
import json
from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
 

from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.secret_key = "randomstring123"



if app.config['DEBUG'] == True:
    from config import dbconfig
    app.config["MONGO_DBNAME"] = 'dumpdinners'
    app.config["MONGO_URI"] = dbconfig()
else:
    app.config['MONGO_URI'] = os.environ.get("MONGO_URI")
    app.config['MONGO_DBNAME'] = os.environ.get("MONGO_DBNAME")

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    """Home page the gets 4 recipes from DB that have been viewed the most"""
    four_recipes = mongo.db.recipes.find().limit(4)
    return render_template('allrecipes1.html', recipes=four_recipes)     

@app.route('/allrecipes')
def allrecipes():
    recipes = mongo.db.recipes.find()
    return render_template('allrecipes.html', recipes=recipes)    
    
@app.route('/allrecipes1')
def allrecipes1():
    recipes = mongo.db.recipes.find()
    four_recipes = mongo.db.recipes.find().limit(4)
    return render_template('allrecipes1.html', recipes=four_recipes)        

@app.route('/add_recipe')
def add_recipe():
    recipes = mongo.db.recipes.find()
    return render_template('addrecipe.html',
        recipes=mongo.db.categories.find())   

    

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    flash ("Thank you, your recipe has been inserted!")
    return render_template('recipe.html', recipe=recipe)
   
         
    
    
@app.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    """Allows logged in user to edit their own recipes"""
    recipe_db = mongo.db.recipes.find_one_or_404({'_id': ObjectId(recipe_id)})
    all_categories =  mongo.db.categories.find()
    if request.method == 'GET':
        
        return render_template('editrecipe.html', recipe=recipe_db, categories=all_categories)
   

# referred to this article for advice on 'views' - https://stackoverflow.com/questions/5782311/mongodb-inc-embedded-value-syntax

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        '$set': {
            
        'recipe_name':request.form.get('recipe_name'),
        'ingredients':request.form.get('ingredients'),
        'image': request.form.get('image'),
        'category_name': request.form.get('category_name'),
        'username': request.form.get('username'),
        'methods': request.form.get('methods'),
        'short_description': request.form.get('short_description'),
        'date_added': request.form.get('date_added'),
        'is_vegetarian': request.form.get('is_vegetarian'),
        'views':1,
        'likes':1
        }
    })
    return redirect(url_for('allrecipes'))
    



@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('allrecipes'))
    
@app.route('/search')
def search():
    """Provides logic for search bar"""
    orig_query = request.args['query']
    # using regular expression setting option for any case
    query = {'$regex': re.compile('.*{}.*'.format(orig_query)), '$options': 'i'}
    # find instances of the entered word in title, tags or ingredients
    results = mongo.db.recipes.find({
        '$or': [
            {'recipe_name': query},
            {'ingredients': query},
            {'recipe_name': query}
        ]
    })
    return render_template('search.html', query=orig_query, results=results)


@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
   
    """Shows full recipe and increments view"""
    mongo.db.recipes.find_one_and_update(
        {'_id': ObjectId(recipe_id)},
        { '$inc': { 'views': 1}}
        
        
      
    )
    recipe_db = mongo.db.recipes.find_one_or_404({'_id': ObjectId(recipe_id)})
    return render_template('recipe.html', recipe=recipe_db)

# routing for likes

@app.route('/likes/<recipe_id>')
def likes(recipe_id):
   
    """Shows full recipe and increments view"""
    mongo.db.recipes.find_one_and_update(
        {'_id': ObjectId(recipe_id)},
        { '$inc': { 'likes': 1}}
        
        
      
    )
    recipe_db = mongo.db.recipes.find_one_or_404({'_id': ObjectId(recipe_id)})
    return redirect(url_for('allrecipes1'))

# routing for shares

@app.route('/shares1/<recipe_id>')
def shares1 (recipe_id):
   
    """Shows full recipe and increments view"""
    mongo.db.recipes.find_one_and_update(
        {'_id': ObjectId(recipe_id)},
        { '$inc': { 'shares1': 1}}
        
        
      
    )
    recipe_db = mongo.db.recipes.find_one_or_404({'_id': ObjectId(recipe_id)})
    return redirect(url_for('allrecipes1'))

   
    
#Copied routing for login from Deborah Thompson, student at Code Institute for login routing - #https://github.com/debbiect246/recipe-app#


@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == 'POST':
        login_user = mongo.db.register.find_one({'username': request.form['username']})
        form = request.form
        if login_user:
            if(form["password"] == login_user["password"]): # if password correct
                session['username'] = login_user["username"]
                return redirect(url_for('allrecipes',register_id = login_user["_id"]))
            else: # and if password is not correct
               flash("Incorrect password, please try again or register") 
        else:# if user does not exist
            flash("User does not exist")
            return redirect(url_for('register'))
    return render_template('login.html')            
    
    
#Copied routing for register from Deborah Thompson, student at Code Institute for login routing - #https://github.com/debbiect246/recipe-app#

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        register = mongo.db.register
        register_id = register.insert_one(request.form.to_dict())
        # print(register)
        object_id = register_id.inserted_id
        flash("Thank you for registering, please login to view more recipes and add your own!")
        return redirect(url_for('login'))
    return render_template('register.html')
              
    

 
#Copied routing for allrecipeslist from Deborah Thompson, student at Code Institute for login routing - #https://github.com/debbiect246/recipe-app#


@app.route('/logout')
def logout():
    """Clears session and redirects to home"""
    
    session.clear()
    flash ("Thank you, hope to see you again soon!")
    return redirect(url_for('login'))




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')))