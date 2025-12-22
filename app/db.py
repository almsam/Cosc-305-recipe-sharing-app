import sqlite3

connect = sqlite3.connect('database.db', check_same_thread=False)

connect.execute("""
CREATE TABLE IF NOT EXISTS Recipes(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    recipeBody TEXT
)
""")

connect.execute("""
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    bio TEXT
)
""")

def getRecipe(id):
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM Recipes WHERE id = ?", (id,))
    row = cursor.fetchone()
    return row

def getAllRecipes():
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM Recipes")
    return cursor.fetchall()

def addRecipe(title, description, recipeBody):
    cursor = connect.cursor()
    cursor.execute(
        "INSERT INTO Recipes(title, description, recipeBody) VALUES (?,?,?)",
        (title, description, recipeBody)
    )
    connect.commit()
    return cursor.lastrowid

def updateRecipe(id, title, description, recipeBody):
    cursor = connect.cursor()
    cursor.execute(
        "UPDATE Recipes SET title=?, description=?, recipeBody=? WHERE id=?",
        (title, description, recipeBody, id)
    )
    connect.commit()

def deleteRecipe(id):
    cursor = connect.cursor()
    cursor.execute("DELETE FROM Recipes WHERE id=?", (id,))
    connect.commit()

def addUser(username, password):
    cursor = connect.cursor()
    cursor.execute(
        "INSERT INTO Users(username, password) VALUES (?,?)",
        (username, password)
    )
    connect.commit()
    return cursor.lastrowid

def getUserByUsername(username):
    cursor = connect.cursor()
    cursor.execute(
        "SELECT * FROM Users WHERE username = ?",
        (username,)
    )
    return cursor.fetchone()

def updateUserBio(username, bio):
    cursor = connect.cursor()
    cursor.execute(
        "UPDATE Users SET bio=? WHERE username=?",
        (bio, username)
    )
    connect.commit()

def getUser(username):
    cursor = connect.cursor()
    cursor.execute(
        "SELECT id, username, password, bio FROM Users WHERE username=?",
        (username,)
    )
    return cursor.fetchone()

if __name__ == "__main__":
    print("Seeding database...")

    # Users
    addUser("testuser@gmail.com", "testpass")

    # Recipes
    addRecipe(
        "Chicken Biryani",
        "Fragrant, layered Indian rice dish.",
        """Chicken pieces
Yogurt
Biryani masala
Sliced onions
Basmati rice
Saffron milk
Oil
Salt
===
Marinate chicken with yogurt, masala, and salt.
Fry sliced onions until golden.
Add chicken and cook halfway.
Parboil basmati rice until 70% cooked.
Layer rice over chicken in a pot.
Add saffron milk.
Cover tightly and steam for 20 minutes."""
    )

    addRecipe(
        "Pancakes",
        "Fluffy breakfast pancakes.",
        """Flour
Milk
Eggs
Sugar
Butter
Baking powder
Salt
===
Mix flour, sugar, baking powder, and salt.
Whisk milk and eggs in a separate bowl.
Combine wet and dry ingredients.
Heat a pan and melt butter.
Pour batter and cook until bubbles appear.
Flip and cook until golden.
Serve with syrup."""
    )

    addRecipe(
        "Spaghetti Bolognese",
        "Classic Italian meat pasta.",
        """Spaghetti pasta
Ground beef
Tomato sauce
Onion
Garlic
Olive oil
Salt and pepper
Parmesan cheese
===
Boil spaghetti until al dente.
Sauté onions and garlic in olive oil.
Add ground beef and cook until browned.
Pour in tomato sauce and season.
Simmer for 20 minutes.
Mix sauce with spaghetti.
Top with parmesan."""
    )

    addRecipe(
        "Caesar Salad",
        "Crisp lettuce tossed with creamy Caesar dressing.",
        """Romaine lettuce
Croutons
Parmesan cheese
Caesar dressing
Black pepper
Grilled chicken (optional)
===
Chop romaine lettuce.
Toss lettuce with Caesar dressing.
Add croutons and parmesan.
Top with grilled chicken if desired.
Season with black pepper."""
    )

    addRecipe(
        "Butter Chicken",
        "Rich and creamy tomato-based curry.",
        """Chicken breast
Yogurt
Butter
Tomato puree
Cream
Garlic
Ginger
Spices
===
Marinate chicken in yogurt and spices.
Cook chicken in a pan until lightly browned.
Prepare sauce with butter, tomato puree, garlic, and ginger.
Add cream and simmer.
Mix chicken into sauce and cook 10 minutes.
Serve with naan or rice."""
    )

    addRecipe(
        "French Toast",
        "Sweet and soft breakfast classic.",
        """Bread slices
Eggs
Milk
Sugar
Cinnamon
Butter
===
Whisk eggs, milk, sugar, and cinnamon.
Dip bread slices into mixture.
Heat butter on a pan.
Cook bread until golden on both sides.
Serve with berries or syrup."""
    )

    addRecipe(
        "Brownies",
        "Rich, fudgy chocolate brownies.",
        """Butter
Sugar
Flour
Eggs
Cocoa powder
Chocolate chips
Salt
===
Melt butter and mix with sugar.
Add eggs and whisk.
Stir in flour, cocoa powder, and salt.
Fold in chocolate chips.
Bake at 350°F for 25 minutes.
Cool before cutting."""
    )

    addRecipe(
        "Tacos",
        "Easy Mexican-style tacos.",
        """Tortillas
Ground beef or chicken
Taco seasoning
Lettuce
Cheese
Salsa
===
Cook meat with taco seasoning.
Warm tortillas.
Fill tortillas with meat.
Add lettuce, cheese, and salsa.
Serve with lime."""
    )

    addRecipe(
        "Veggie Stir Fry",
        "Healthy mix of vegetables sautéed with sauce.",
        """Broccoli
Bell peppers
Carrots
Soy sauce
Garlic
Sesame oil
===
Chop all vegetables.
Heat oil in a pan.
Stir fry vegetables on high heat.
Add soy sauce and garlic.
Cook until vegetables are crisp-tender.
Serve with rice or noodles."""
    )

    addRecipe(
        "Grilled Cheese Sandwich",
        "Golden, crispy grilled cheese.",
        """Bread slices
Cheddar cheese
Butter
===
Butter one side of each bread slice.
Place cheese between slices.
Cook on a pan until golden brown.
Flip and cook the other side.
Serve hot."""
    )
