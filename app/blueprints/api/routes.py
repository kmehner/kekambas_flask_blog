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

# Edit a Single Post by ID
@api.route('/edit-posts/<post_id>', methods=["GET", "POST"])
@token_auth.login_required
def edit_post(post_id):
    if not request.is_json:
        return jsonify({'error': 'Your request content-type must be application/json'}), 400

    # Get data from request body
    data = request.json
    # check that all are make sense
    for field in data:
        if field not in ['title', 'body']:
        # if not return a 400 response with error (edit)
            return jsonify({'error': f'{field} must be in request body'}), 400

    post = Post.query.get_or_404(post_id)

    # Get fields from data dict
    user_id = token_auth.current_user().id

    # if post author is not current user
    if post.author != user_id:
        return jsonify({'error': f'You must be the author to edit this post'}), 400

    # post update (prev post.update(**form.data) thinking we can pass through individual stuff as kwargs)
    edit_post = post.update(**data)
        
    return jsonify(edit_post.to_dict())

@api.route('/delete-posts/<post_id>')
@token_auth.login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    user_id = token_auth.current_user().id

    # Check if the user is the author
    if post.author != user_id:
       return jsonify({'error':'You do not have delete access to this post'}), 400
    else:
        post.delete()

    return 204
