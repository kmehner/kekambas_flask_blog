from app import app
from flask import render_template

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


@app.route('/signup')
def signup():
    title = 'Sign Up'
    return render_template('signup.html', title=title)


@app.route('/login')
def login():
    title = 'Log In'
    return render_template('login.html', title=title)