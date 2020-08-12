from flask import Flask, request, redirect
import flask as f
import json

app = Flask(__name__)
def read_users_dict():
    f = open("users.json", "r")
    users = json.load(f)
    f.close()
    return users


def save_users_dict(users):
    f = open("users.json", "w")
    json.dump(users, f)
    f.close()

@app.route("/")
def do_login():
    return redirect("/static/login.html")


@app.route("/login", methods=['POST'])
def do_sign_up():
    form = request.form
    print(form)
    email = request.form['login[username]']
    password = request.form['login[password]']
    users = read_users_dict()
    users[email] = password
    save_users_dict(users)
    return f.render_template("welcome.html")



if __name__ == '__main__':
   app.run(host='localhost', port=8181)