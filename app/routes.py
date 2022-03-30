from app import app
from flask import redirect, render_template, url_for, flash
from app.forms import SignUpForm
from app.models import User, Post

@app.route('/')
def index():
    title = 'Home'
    user = {'id': 1, 'username': 'bstanton', 'email': 'brians@codingtemple.com'}
    posts = Post.query.all()
    return render_template('index.html', current_user=user, title=title, posts=posts)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    title = 'Sign Up'
    form = SignUpForm()
    # check if a post request and that the form is valid
    if form.validate_on_submit():
        # Get data from the validated form
        email = form.email.data
        username = form.username.data
        password = form.password.data
        # Check if there is a user with that username or email
        users_with_that_info = User.query.filter((User.username==username)|(User.password==password))
        if users_with_that_info:
            # Create a new user instance with form data
            flash(f"There is already a user with that username and/or email. Please try again", "danger")
            return render_template('signup.html', title=title, form=form)

        new_user = User(email=email, username=username, password=password)
        # Flash message saying new user has been created
        flash(f"{new_user.username} has succesfully signed up.", "success")

        return redirect(url_for('index'))

    return render_template('signup.html', title=title, form=form)


@app.route('/login')
def login():
    title = 'Log In'
    return render_template('login.html', title=title)