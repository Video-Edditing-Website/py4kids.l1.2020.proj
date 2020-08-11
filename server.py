from flask import Flask, request
import flask as f

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/login", methods=['POST'])
def do_login():
    email = request.form['email']
    password = request.form['password']

    if not (password == "abc123") :
        return f.render_template("login_failed.html")
    else:
        return f.render_template("welcome.html", user_name=email)


@app.route("/welcome/<email>")
def do_welcome(email):
    print("Email supplied:{}".format(email))

    file_contents = f.render_template("welcome.html", user_name=email)
    return file_contents

if __name__ == '__main__':
    app.run(host='localhost', port=8181)