from flask import Flask
import  flask as f

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/welcome/<email>")
def do_welcome(email):
    print("Email supplied:{}".format(email))

    file_contents = f.render_template("welcome.html", user_name=email)
    return file_contents

if __name__ == '__main__':
    app.run(host='localhost', port=8181)