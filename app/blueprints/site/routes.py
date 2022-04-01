from . import site
from flask import redirect, render_template, url_for, flash
from flask_login import login_required, current_user
from .forms import RegisterPhoneForm, SearchForm
from .models import PhoneBook, Post


@site.route('/')
def index():
    title="Home"
    posts = Post.query.all()
    return render_template('index.html', title=title, posts=posts)


@site.route('/register_phone', methods=["GET", "POST"])
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
        users_with_that_address = PhoneBook(first_name=first_name, last_name=last_name, phone_number=phone_number, address=address, user_id=current_user.id)
        if users_with_that_address:
            flash(f"There is already a user with that address. Please try again", "danger")
            return render_template('signup.html', title=title, form=form)

        #create a new user instance with form data
        addresses = PhoneBook(first_name=first_name, last_name=last_name, phone_number=phone_number, address=address)
        #flash message saying that they have registered their phone
        flash(f"Nice {addresses.first_name}! You have successfully registed your phone number", "success")
        return redirect(url_for('site.index'))

    return render_template('site.register_phone.html', title=title, form=form)

@site.route('/my-addresses')
@login_required
def my_addresses():
    title = 'My Addresses'
    addresses = current_user.addresses.all()
    return render_template('my_posts.html', title=title, addresses=addresses)


@site.route('/search-posts', methods=['GET', 'POST'])
def search_posts():
    title = 'Search'
    form = SearchForm()
    posts = []
    return render_template('search_posts.html', title=title, posts=posts, form=form)


