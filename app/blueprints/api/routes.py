from . import api
from flask import jsonify
from app.blueprints.blog.models import Post

@api.route('/')
def index():
    return jsonify({'test': 'This is a test'})



# Get all posts
@api.route('/posts')
def get_posts():
    posts = Post.query.all()
    return jsonify([p.to_dict() for p in posts])



# Get a single post by id
