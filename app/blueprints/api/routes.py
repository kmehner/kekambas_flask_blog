from . import api
from .auth import basic_auth, token_auth
from flask import jsonify, request
from app.blueprints.blog.models import Post

@api.route('/posts')
@basic_auth.login_required
def index():
    user = basic_auth.current_user
    token = user.get_token()
    return jsonify({'token': token, 'expiration': user.token_expiration})


# Get all posts
@api.route('/posts')
def get_posts():
    posts = Post.query.all()
    return jsonify([p.to_dict() for p in posts])

# get a single post by id
@api.route('/posts/<int:post_id>')
def get_single_post(post_id):
    post = Post.query.get_or_404(post_id)
    return jsonify(post.to_dict())

# Create a post
@api.route('/posts/create', methods=['POST'])
@token_auth.login_required
def create_post():
    if not request.is_json:
        return jsonify({'error': 'Your request content-type must be application/json'}), 400
    # Get data from request body
    data = request.json
    # Check to make sure all required fields are present
    for field in ['title', 'body']:
        if field not in data:
            # if not return a 400 response with error
            return jsonify({'error': f'{field} must be in request body'}), 400
    # Get fields from data dict
    title = data['title']
    body = data['body']
    user_id = token_auth.current_user().id
    new_post = Post(title=title, body=body, user_id=user_id)
    return jsonify(new_post.to_dict())