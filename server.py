from flask import Flask, request, redirect
import flask
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
def do_login():
    return redirect("/static/login.html")
    email = request.form['login[username]']
    password = request.form['login[password]']
    if email and password in users:
        return flask.render_template("welcome.html")
    else:
        return flask.render_template("login_failed.html")



@app.route("/static/sign_up.html")
def do_sign_up():
    form = request.form
    print(form)
    email = request.form['login[username]']
    password = request.form['login[password]']
    users = read_users_dict()
    users[email] = password
    save_users_dict(users)
    return flask.render_template("welcome.html")



if __name__ == '__main__':
   app.run(host='localhost', port=8181)