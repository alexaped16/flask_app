
from app import app
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required 
from app.forms import RegisterPhoneForm, SignUpForm, LoginForm
from app.models import PhoneBook, User, Post



@app.route('/')
def index():
    title="Home"
    posts = Post.query.all()
    return render_template('index.html', title=title, posts=posts)


@app.route('/register_phone', methods=["GET", "POST"])
@login_required
def phone(): 
    title = 'Register phone'
    form = RegisterPhoneForm()
    #check if a post request AND if the form is valid
    if form.validate_on_submit(): 
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone_number = form.phone_number.data
        address = form.address.data

        # Check if there is a user with email or username
        users_with_that_address = PhoneBook.query.filter((User.id==PhoneBook.id)|(PhoneBook.address==address)).all() 
        if users_with_that_address:
            flash(f"There is already a user with that address. Please try again", "danger")
            return render_template('signup.html', title=title, form=form)

        #create a new user instance with form data
        new_phone = PhoneBook(first_name=first_name, last_name=last_name, phone_number=phone_number, address=address)
        #flash message saying that they have registered their phone
        flash(f"Nice {new_phone.first_name}! You have successfully registed your phone number", "success")
        return redirect(url_for('index'))

    return render_template('register_phone.html', title=title, form=form)


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

        # Check if there is a user with email or username
        users_with_that_info = User.query.filter((User.username==username)|(User.email==email)).all() 
        if users_with_that_info:
            flash(f"There is already a user with that username and/or email. Please try again", "danger")
            return render_template('signup.html', title=title, form=form)

        # Create a new user instance with form data
        new_user = User(email=email, username=username, password=password)

        #flash message saying new user has been created
        flash(f"{new_user.username} has succesfully signed up.", "success")
        return redirect(url_for('index'))

    return render_template('signup.html', title=title, form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    title = 'Log In'
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        # Query for a user with that username
        user = User.query.filter_by(username=username).first()
        # Check if there is a user and the password is correct
        if user and user.check_password(password):
            # log the user in with flask-login
            login_user(user)
            # flash message that user has successfully logged in
            flash(f'{user} has successfully logged in', 'success')
            # redirect to the home page
            return redirect(url_for('index'))
        else:
            flash('Username and/or password is incorrect', 'danger')
            
    return render_template('login.html', title=title, form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('You have successfully logged out', 'primary')
    return redirect(url_for('index'))
    
