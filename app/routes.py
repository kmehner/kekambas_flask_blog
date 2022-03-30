from app import app
from flask import redirect, render_template, url_for, flash
from flask_login import login_required, current_user
from app.forms import PostForm
from app.models import Post

@app.route('/')
def index():
    title = 'Home'
    posts = Post.query.all()
    return render_template('index.html', title=title, posts=posts)


@app.route('/create-post', methods=['GET', 'POST'])
@login_required
def create_post():
    title = 'Create A Post'
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        new_post = Post(title=title, body=body, user_id=current_user.id)
        flash(f"{new_post.title} has been created", 'secondary')
        return redirect(url_for('index'))
    return render_template('create_post.html', title=title, form=form)


@app.route('/my-posts')
@login_required
def my_posts():
    title = 'My Posts'
    posts = current_user.posts.all()
    return render_template('my_posts.html', title=title, posts=posts)