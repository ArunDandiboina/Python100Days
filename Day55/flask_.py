from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App!"

@app.route('/template')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return "Hello, World!"

@app.route('/<name>')
def get_item(name):
    return f"You requested the item: {name}"

@app.route('/<int:id>')
def get_item_by_id(id):
    return f"You requested the item with ID: {id}"


@app.route('/<path:subpath>')
def get_subpath(subpath):
    return f"You requested the subpath: {subpath}"



if __name__ == '__main__':
    app.run(debug=True)