from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = 'https://api.npoint.io/9eb1cc2d1dabaa1cdbec'
    response = requests.get(blog_url)
    all_post = response.json()
    return render_template("index.html",posts=all_post)

@app.route('/about')
def get_about():
    return render_template("about.html")

@app.route('/contact')
def get_contact():
    return render_template("contact.html")

@app.route('/post/<idx>')
def get_post(idx):
    blog_url = 'https://api.npoint.io/9eb1cc2d1dabaa1cdbec'
    response = requests.get(blog_url)
    post = response.json()[int(idx)-1]
    return render_template("post.html",post=post)

if __name__ == "__main__":
    app.run(debug=True)