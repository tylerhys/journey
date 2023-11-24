from flask import Flask, render_template, request
import requests
import smtplib
my_email = "tylerhystesting@gmail.com"
password = "wayj oidp xnpt jihp"

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/9eb1cc2d1dabaa1cdbec").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['POST','GET'])
def contact():
    if request.method == 'POST':
        body = f"Subject:Form from Blog\n\n\
                    Name: {request.form['name']}\n\
                    Address:{request.form['email']}\n\
                    Phone:{request.form['phone']}\n\
                    Message:\n\
                    {request.form['message']}"
        print(body)
        
        with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email,password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs='',
                    msg=body
                    )
    return render_template("contact.html", method = request.method)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
