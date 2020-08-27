from flask import Flask, request, redirect, session
import flask as f
import json
import uuid
import os
import review_db as db

app = Flask(__name__)
app.secret_key = "any random string"


def save_review(review_id, review_to_save):
    file_name = os.path.join("reviews", review_id + ".json")
    f = open(file_name, "w")
    json.dump(review_to_save, f, indent=4, sort_keys=True)
    f.close()


def read_users_dict():
    users_file = open("users.json", "r")
    users = json.load(users_file)
    users_file.close()
    return users


users = read_users_dict()


def save_users_dict(users):
    f = open("users.json", "w")
    json.dump(users, f)
    f.close()


@app.route("/view/<review_id>")
def show_review(review_id):
    review_file = "reviews/" + review_id + ".json"
    review = db.read_review_file(review_file)
    return f.render_template("view_review.html", review=review)


@app.route("/")
def show_login_page():
    if 'username' in session:
        return goto_welcome(session['username'])
    return redirect("/static/login.html")


@app.route("/login", methods=["post"])
def do_login():
    email = request.form['login[username]']
    password = request.form['login[password]']
    if email in users:
        stored_password = users[email]
        if stored_password == password:
            return goto_welcome(email)
    return f.render_template("login_failed.html")


def goto_welcome(email):
    session['username'] = email
    reviews = db.get_review_list()
    return f.render_template("welcome.html", user_email=email, reviews=reviews)


@app.route("/submit_review", methods=["post"])
def do_submit_review():
    if not ('username' in session):
        return show_login_page()
    username = session['username']
    game = request.form['games']
    title = request.form['title']
    stars = request.form['stars']
    stars = int(stars)
    review = request.form['review']
    if game == "Invaild":
        return f.render_template("Invaild_game_choice.html")
    elif stars == 0:
        return f.render_template("Invaild_game_choice.html")
    else:
        review_id = uuid.uuid1()
        review_id = str(review_id)
        review_to_save = {'id': review_id, 'game': game, 'title': title, 'stars': stars, 'username': username,
                          'review': review}
        save_review(review_id, review_to_save)
        return f.render_template("thanks_for_review.html")


@app.route("/game_review")
def do_game_review():
    if not ('username' in session):
        return redirect("/static/login.html")
    username = session['username']

    return f.render_template("/game_review.html", username=username)


@app.route("/sign_up", methods=["post"])
def do_sign_up():
    form = request.form
    print(form)
    email = request.form['login[username]']
    password = request.form['login[password]']
    users = read_users_dict()
    if email in users:
        return f.render_template("Sign_up_Email_used.html", email=email
                                 )
    else:
        users[email] = password
        save_users_dict(users)
        return f.render_template("welcome.html", user_email=email)


@app.route("/logout", methods=["post"])
def logout():
    session.pop["username"]
    if not ('username' in session):
        return show_login_page()
    else:
        return f.render_template("Something_went_wrong.html")


if __name__ == '__main__':
    app.run(host='localhost', port=8181, debug=True)
