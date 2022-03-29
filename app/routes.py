from app import app
from flask import redirect, render_template, url_for
from app.forms import SignUpForm
from app.models import User

@app.route('/')
def index():
    title = 'Home'
    user = {'id': 1, 'username': 'bstanton', 'email': 'brians@codingtemple.com'}
    posts = [
        {
            'id': 1,
            'title': 'March Madness',
            'body': 'The NCAA tournament never seems to disappoint!',
            'author': 'cbbfan'
        },
        {
            'id': 2,
            'title': 'Oscars',
            'body': 'I think that Coda might win Best Picture this year. I cried the whole time.',
            'author': 'BuffMovieBuff123'
        },
        {
            'id': 3,
            'title': 'Python',
            'body': 'Python is by far my favorite programming language. It is so neat!',
            'author': 'code_is_life'
        },
        {
            'id': 4,
            'title': 'Flask',
            'body': 'My favorite microframework! And this is only the beginning.',
            'author': 'CodingTemple4L'
        }
    ]
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
        # Create a new user instance with form data
        new_user = User(email=email, username=username, password=password)
        return redirect(url_for('index'))

    return render_template('signup.html', title=title, form=form)


@app.route('/login')
def login():
    title = 'Log In'
    return render_template('login.html', title=title)

