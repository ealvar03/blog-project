from flask import Flask, render_template
import requests
from post import Post

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
posts = response.json()
posts_list = []
for post in posts:
    post_item = Post(post["id"], post["title"], post["subtitle"], post["body"])
    posts_list.append(post_item)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", all_posts=posts_list)


@app.route('/post/<int:blog_id>')
def get_blog(blog_id):
    requested_blog = None
    for post_entry in posts_list:
        if post_entry.id == blog_id:
            requested_blog = post_entry
    return render_template("post.html", post=requested_blog)


if __name__ == "__main__":
    app.run(debug=True)
