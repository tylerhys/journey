from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    all_post = response.json()
    return render_template("index.html",posts=all_post)

@app.route('/post/<num>')
def get_blog(num):
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    post = response.json()[int(num)-1]
    return render_template("post.html",post=post)

if __name__ == "__main__":
    app.run(debug=True)
