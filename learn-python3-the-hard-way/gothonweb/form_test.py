from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


# @app.route("/hello")
@app.route("/hello", methods=['POST', 'GET'])
def index():
    '''
    name = request.args.get('name', 'Nobody')

    if name:
        greeting = f"Hello, {name}"
    else:
        greeting = "Hello World"

    return render_template("index.html", greeting=greeting)
    '''

    greeting = "Hello World"

    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        print(f">>>>{greet}, {name}")
        greeting = f"{greet}, {name}"
        return render_template("index.html", greeting=greeting)
    else:
        return render_template("hello_form.html")


if __name__ == "__main__":
    app.run()
