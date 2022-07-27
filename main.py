from flask import Flask, render_template
import requests

blog_url = 'https://api.npoint.io/4ac9c32a945d3983ac66'
blog_resp = requests.get(blog_url)

print(blog_resp)
all_posts = blog_resp.json()

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('/index.html')


@app.route('/index.html')
def home():
    return render_template('/index.html')


@app.route('/about.html')
def about():
    return render_template('/about.html')


@app.route('/contact.html')
def contact():
    return render_template('/contact.html')


@app.route("/post/<int:index>")
def show_post(index):
    post = all_posts[index-1]
    return render_template("post.html", post=post, image=post['image'])


if __name__ == '__main__':
    app.run(debug=True)
