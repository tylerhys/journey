from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>\
            <p>This is a pingu</p>\
                <img src="https://t4.ftcdn.net/jpg/05/65/72/25/360_F_565722576_O1ukHVh1pIn2D3OS2grnG9w2RwwykPXf.jpg">'

@app.route("/bye")
def say_bye():
    return "Bye"

@app.route("/username/<name>/<int:number>")
def greet(name,number):
    return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)
