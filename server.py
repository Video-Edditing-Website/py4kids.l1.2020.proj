from flask import Flask, request, redirect
import flask as f
import json

app = Flask(__name__)
def read_users_dict():
    flask = open("users.json", "r")
    users = json.load(flask)
    flask.close()
    return users

users = read_users_dict()

def save_users_dict(users):
    f = open("users.json", "w")
    json.dump(users, f)
    f.close()

@app.route("/")
def show_login_page():
    return  redirect("/static/login.html")


@app.route("/login", methods=["post"])
def do_login():
    email = request.form['login[username]']
    password = request.form['login[password]']
    if email in users:
        stored_password = users[email]
        if stored_password == password:
            return f.render_template("welcome.html", user_email=email)

    return f.render_template("login_failed.html")


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
   app.run(host='localhost', port=8181)