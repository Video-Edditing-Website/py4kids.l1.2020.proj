from flask import Flask, request, redirect
import flask as f
import json
import uuid
import os

app = Flask(__name__)


def save_review(review_id, review_to_save):
    file_name = os.path.join("reviews", review_id + ".json")
    f = open(file_name, "w")
    json.dump(review_to_save, f)
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

def get_all_review_titles():
    return []


@app.route("/")
def show_login_page():
    return redirect("/static/login.html")


@app.route("/login", methods=["post"])
def do_login():
    email = request.form['login[username]']
    password = request.form['login[password]']

    if email in users:
        stored_password = users[email]
        if stored_password == password:
            title_list = get_all_review_titles()
            return f.render_template("welcome.html", user_email=email, titles=title_list)

    return f.render_template("login_failed.html")


@app.route("/submit_review", methods=["post"])
def do_submit_review():
    game = request.form['games']
    title = request.form['title']
    stars = request.form['stars']
    stars = int(stars)
    review = request.form['review']
    #if game == "Other":
        #return f.render_template("other=what.html")
    print("The game is {}.".format(game))
    print("Title: {}.".format(title))
    print("Stars: {}.".format(stars))
    print("{}".format(review))
    review_id = uuid.uuid1()
    review_id = str(review_id)
    review_to_save = {'game': game, 'title': title, 'stars': stars, 'review': review}
    save_review(review_id, review_to_save)
    return f.render_template("thanks_for_review.html")


@app.route("/game_review")
def do_game_review():
    return f.render_template("game_review.html")


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





if __name__ == '__main__':
    app.run(host='localhost', port=8181, debug=True)