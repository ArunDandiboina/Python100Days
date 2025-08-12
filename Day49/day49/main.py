from flask import Flask, render_template
import requests

blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'

try:
    response = requests.get(blog_url)
    response.raise_for_status()  # Check for HTTP errors
    all_posts = response.json()
except requests.exceptions.RequestException as e:
    all_posts = []

app = Flask(__name__)

@app.route('/')
def home():
    # print(all_posts)
    return render_template('index.html', posts=all_posts)

@app.route('/blog/<int:id>')
def blog_post(id):
    post = [post for post in all_posts if post['id'] == id]
    # print(post)
    return render_template('post.html', post=post[0])

if __name__ == "__main__":
    app.run(debug=True)
