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
@api.route('/posts/<int:post_id>')
def get_single_post(post_id):
    post = Post.query.get_or_404(post_id)
    return jsonify(post.to_dict())
