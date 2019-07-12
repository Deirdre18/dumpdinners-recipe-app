import os
import re
from flask import Flask, render_template, redirect, request, url_for, session, flash

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
def index():
    recipes = mongo.db.recipes.find()
    return render_template("allrecipes.html", 
        recipes=mongo.db.recipes.find())

@app.route('/add_recipe')
def add_recipe():
    recipes = mongo.db.recipes.find()
    return render_template('addrecipe.html',
        categories=mongo.db.category.find())   

    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    flash ("Your recipe has been inserted")
    return redirect(url_for('allrecipes'))
    


@app.route('/allrecipes')
def allrecipes():
    recipes = mongo.db.recipes.find()
    return render_template('allrecipes.html', recipes=recipes)
    
        
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
        'views': 1
        
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
            {'tags': query},
            {'ingredients': query},
        ]
    })
    return render_template('search.html', query=orig_query, results=results)


@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    """Shows full recipe and increments view"""
    mongo.db.recipes.find_one_and_update(
        {'_id': ObjectId(recipe_id)},
        {'$inc': {'views': 1}}
    )
    recipe_db = mongo.db.recipes.find_one_or_404({'_id': ObjectId(recipe_id)})
    return render_template('recipe.html', recipe=recipe_db)




#ROUTES FOR CATEGORIES

#Its job is to do a find on the categories table. So categories.html is the template we're going to render. And our categories parameter will feed that from a direct call to MongoDB. So Mongo.db.categories.find.

@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
        categories=mongo.db.categories.find())
        

        
#ADDING ROUTE FOR DELETE TASK

#As a challenge, you could add a new key value property inside the tasks that maybe marks a task as being complete. Then when you display tasks, you'll only display tasks where complete is equal to false. But for now, we'll just delete a task once we're finished with it.. If you do accept the challenge and go on to mark a task as complete, then change the name of the function from delete_task to mark as complete.

#So we access the tasks collection, and we call remove. And we pass in the task_id as the parameter, so it's a very simple function. Again, we use the syntax as we have been using up until now. Key value pair inside the curly braces. We use the object ID to format or parse the task ID in a way that's acceptable to Mongo.  Once that's in place, we want to return or redirect. So we redirect to get tasks. Why? Because once that function is complete, we want to see it disappear. We want visual evidence to see that that task is no longer on our list. So we redirect to the get_tasks function. It's very straightforward. Now, you might need to clear your cache here for this to be picked up. Let's clear the browsing data. As I said earlier, you can use incognito mode if you wish. Click done, and that disappears. So they're marked as complete. As I mentioned, they're simply just deleted from the database. In reality, you would come up with a more sophisticated solution than that. So there we are, task complete.

#------------------------------------- DELETE CATEGORY CORRESPONDING FUNCTION

#create a function (delete_category) and pass in category_id as parameter to remove document from categories collection.
@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))

@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
    category=mongo.db.categories.find_one({'_id': ObjectId(category_id)}))



@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    categories = mongo.db.categories.update({'_id': ObjectId(category_id)},
         {'category_name': request.form.get('category_name')})
    return redirect(url_for('get_categories'))


@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = {'category_name': request.form.get('category_name')}
    mongo.db.categories.insert_one(category_doc)
    return redirect(url_for('get_categories'))


@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')
    


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
               flash("Incorrect password") 
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
        return redirect(url_for('allrecipes',register_id=object_id))
    return render_template('register.html')
              
    

 
#Copied routing for allrecipeslist from Deborah Thompson, student at Code Institute for login routing - #https://github.com/debbiect246/recipe-app#



@app.route('/logout')
def logout():
    """Clears session and redirects to home"""
    session.clear()
    return redirect(url_for('allrecipes'))




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')))