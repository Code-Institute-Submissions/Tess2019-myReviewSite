import os

from flask import(
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import  env 


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_boardgames")
def get_boardgames():
    boardgame = mongo.db.boardgames.find()
    return render_template("boardgames.html", boardgames=boardgame)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username alredy exists in db
        existing_user = mongo.db.user.find_one(
            {"username": request.form.get("username").lower()})

        # message for user and security hash
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
            # want dubblecheck password, check werkzeug for info
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Register successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")
    # after page reload the new user register in mongodb


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db.
        # the username input in lowercase method
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # find a match password of user input in db, werkzeug hash
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                # make user a validation
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username do not exist redirect to login
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # find user info
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    # if session user cookie is true
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


# Log out
@app.route("/logout")
def logout():
    flash("You have been logged out")
    # remove session
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/member_list")
def member_list():
    game = mongo.db.add_game.find()
    return render_template("member_list.html", add_game=game)


@app.route("/add_game", methods=["GET", "POST"])
def add_game():
    if request.method == "POST":
        game = {
            "category": request.form.get("category"),
            "category_name": request.form.get("category_name"),
            "game_description": request.form.get("game_description"),
            "user_note": request.form.get("user_form"),
            "created_by": session["user"]
        }
        mongo.db.add_game.insert_one(game)
        flash("Game Succesfully Added")
        return redirect(url_for("member_list"))

    game = list(mongo.db.add_game.find())
    return render_template("add_game.html", add_game=game)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
