import sqlite3

connect = sqlite3.connect('database.db', check_same_thread=False)

# REMOVE WHEN DONE TESTING
connect.execute("DROP TABLE IF EXISTS Recipes")
connect.execute("DROP TABLE IF EXISTS Users")

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
