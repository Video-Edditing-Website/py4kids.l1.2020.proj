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

@app.route('/')
def hello_world():
    return  redirect("/static/sign_up.html")


@app.route("/login", methods=['POST'])
def do_login():
    form = request.form
    print(form)
    email = request.form['login[username]']
    password = request.form['login[password]']
    users = read_users_dict()
    users[email] = password
    save_users_dict(users)


@app.route("/welcome/<email>")
def do_welcome(email):
    print("Email supplied:{}".format(email))

    file_contents = f.render_template("welcome.html", user_name=email)
    return file_contents

if __name__ == '__main__':
   app.run(host='localhost', port=8181)