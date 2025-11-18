from flask import Flask, render_template, jsonify, request, redirect, url_for
from db import getRecipe, getAllRecipes, addRecipe, updateRecipe, deleteRecipe, addUser, getUserByUsername, getUser, updateUserBio

import db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

####################### recipe routes #######################

@app.route('/recipe/<int:recipe_id>')
def recipe(recipe_id):
    row = getRecipe(recipe_id)
    if not row:
        return "Not found", 404

    raw = row[3] or ""
    parts = raw.split("===\n")
    ingredients_list = parts[0].split("\n")
    steps_list = parts[1].split("\n") if len(parts) > 1 else []

    recipe = {
        "id": row[0],
        "title": row[1],
        "summary": row[2],
        "ingredients": ingredients_list,
        "steps": steps_list
    }

    return render_template("recipe.html", recipe_id=recipe_id, recipe=recipe)


####################### recipe routes #######################


@app.route('/recipes')
def recipes():
    return render_template('recipes.html')

@app.route('/recipes/new', methods=['GET','POST'])
def recipe_new():
    if request.method == 'POST':
        title = request.form['title']
        summary = request.form['summary']
        ingredients = request.form['ingredients']
        steps = request.form['steps']
        body = ingredients + "\n===\n" + steps
        new_id = addRecipe(title, summary, body)

        return redirect(url_for('recipe', recipe_id=new_id))
    return render_template('recipe_form.html', mode='create', recipe=None)



@app.route('/recipes/<int:recipe_id>/edit', methods=['GET','POST'])
def recipe_edit(recipe_id):
    if request.method == 'POST':
        title = request.form['title']
        summary = request.form['summary']
        ingredients = request.form['ingredients']
        steps = request.form['steps']
        body = ingredients + "\n===\n" + steps
        updateRecipe(recipe_id, title, summary, body)

        return redirect(url_for('recipe', recipe_id=recipe_id))

    row = getRecipe(recipe_id)
    if not row:
        return "Not found", 404
    raw = row[3] or ""
    parts = raw.split("===\n")
    ingredients_list = parts[0].split("\n")
    steps_list = parts[1].split("\n") if len(parts) > 1 else []

    recipe = {
        "id": row[0],
        "title": row[1],
        "summary": row[2],
        "ingredients": ingredients_list,
        "steps": steps_list
    }

    return render_template('recipe_form.html', mode='edit', recipe=recipe)



@app.route('/recipes/<int:recipe_id>/delete', methods=['GET','POST'])
def recipe_delete(recipe_id):
    if request.method == 'POST':
        deleteRecipe(recipe_id)
        return redirect(url_for('recipes'))

    row = getRecipe(recipe_id)
    if not row:
        return "Not found", 404
    return render_template("recipe.html", recipe_id=recipe_id, delete_confirm=True, recipe=None)


###########

@app.route('/api/recipes')
def api_recipes():
    rows = getAllRecipes()
    data = [{"id": r[0], "title": r[1], "summary": r[2]} for r in rows]
    q = request.args.get('q','').lower()
    if q:
        data = [r for r in data if q in r['title'].lower() or q in (r['summary'] or '').lower()]
    return jsonify(data)


####################### auth #######################

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = getUserByUsername(email)

        if not user:
            return render_template('login.html', error="User not found")

        stored_pw = user[2]
        if password != stored_pw:
            return render_template('login.html', error="Incorrect password")

        username = user[1]
        return redirect(url_for('profile', username=username))

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # backend insert
        addUser(email, password)
        return redirect(url_for('login'))
    return render_template('register.html')

# Profile
@app.route('/profile/<username>')
def profile(username):
    row = getUser(username)
    if not row:
        return "User not found", 404

    user = {
        "username": row[1],
        "bio": row[3] or "",
        "avatar": "/static/images/placeholder.png"
    }

    return render_template("profile.html", user=user)



@app.route('/profile/<username>/edit', methods=['GET','POST'])
def profile_edit(username):
    if request.method == 'POST':
        bio = request.form['bio']
        updateUserBio(username, bio)
        return redirect(url_for('profile', username=username))

    row = getUser(username)
    if not row:
        return "User not found", 404

    user = {
        "username": row[1],
        "bio": row[3] or "",
        "avatar": "/static/images/placeholder.png"
    }

    return render_template("profile_edit.html", user=user)




####################### util #######################


@app.route('/favorites')
def favorites():
    return render_template('favorites.html')


@app.route('/search')
def search():
    q = request.args.get('q', '')
    return render_template('search_results.html', q=q)


@app.route('/category/<string:name>')
def category(name):
    return render_template('category.html', category=name)


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
