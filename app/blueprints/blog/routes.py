from . import blog
from flask import redirect, render_template, url_for, flash
from flask_login import login_required, current_user
from .forms import PostForm
from .models import Post

@blog.route('/')
def index():
    title = 'Home'
    posts = Post.query.all()
    return render_template('index.html', title=title, posts=posts)


@blog.route('/create-post', methods=['GET', 'POST'])
@login_required
def create_post():
    title = 'Create A Post'
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        new_post = Post(title=title, body=body, user_id=current_user.id)
        flash(f"{new_post.title} has been created", 'secondary')
        return redirect(url_for('blog.index'))
    return render_template('create_post.html', title=title, form=form)


@blog.route('/my-posts')
@login_required
def my_posts():
    title = 'My Posts'
    posts = current_user.posts.all()
    return render_template('my_posts.html', title=title, posts=posts)


@blog.route('/posts/<post_id>')
def single_post(post_id):
    post = Post.query.get_or_404(post_id)
    title = post.title
    return render_template('post_detail.html', title=title, post=post)
